import re

import attr
from clldutils.misc import nfilter

from pyasjp.meanings import *

__all__ = ['Transcriber', 'Source', 'Word', 'Synset', 'Doculect', 'ASJPCODES', 'txt_header']

# see
# Brown, Cecil H., Eric W. Holman, Søren Wichmann, and Viveka Vilupillai. 2008.
# Automated classification of the world’s languages:
# a description of the method and preliminary results.
# STUF – Language Typology and Universals 61:285-308.
ASJPCODES = 'pbfvmw8tdszcnrlSZCjT5ykgxNqXh7L4G!ieE3auo'
MISSING_WORD = 'XXX'
LANGUAGE_LINE_PATTERN = re.compile(r'(?P<name>[^{]+){(?P<w>[^|]*)\|(?P<e>[^@}]*)(@(?P<g>[^\}]*))?\}?')


@attr.s
class Transcriber:
    id = attr.ib()
    name = attr.ib()


@attr.s
class Source:
    asjp_name = attr.ib()
    author = attr.ib()
    year = attr.ib()
    title_etc = attr.ib()
    list_made_by = attr.ib(converter=lambda s: nfilter([ss.strip() for ss in re.split('/|->', s)]))


@attr.s
class Word:
    form = attr.ib()
    loan = attr.ib(validator=attr.validators.instance_of(bool))

    @classmethod
    def from_txt(cls, txt):
        if txt.startswith('%'):
            return cls(form=txt[1:], loan=True)
        return cls(form=txt, loan=False)

    def __str__(self):
        return '%' + self.form if self.loan else self.form


@attr.s
class Synset:
    meaning_id = attr.ib(converter=int)
    words = attr.ib()
    comment = attr.ib()

    @classmethod
    def from_txt(cls, line):
        header, body = line.split('\t', 1)
        body = body.strip()
        comment = ''
        if re.search('  | //', body):
            body, comment = re.split('  | //', body, 1)
        comment = comment.strip()
        words = [word.strip() for word in body.split(',') if word.strip() != MISSING_WORD]
        number = header.split()[0]
        if number.endswith('.'):  # pragma: no cover
            number = number[:-1].strip()
        return cls(int(number), [Word.from_txt(w) for w in words], comment or None)

    @staticmethod
    def format(mid, form=MISSING_WORD, comment=None):
        return '{} {}\t{} //{}'.format(
            mid, MEANINGS_ALL[mid], form, ' ' + comment if comment else '')

    def __str__(self):
        return self.format(self.meaning_id, ', '.join(str(w) for w in self.words), self.comment)


def txt_header(synonyms=2, words=28, year=1700):
    """
     2    28  1700     3
(I4,20X,10A1)
    """
    rjust = lambda n, s=6: str(n).rjust(s)
    lines = ['%s%s%s%s%s%s' % tuple(map(rjust, (synonyms, words, year, 3, 92, 72))), '(I4,20X,10A1)']

    for mid, concept in sorted(MEANINGS_ALL.items(), key=lambda p: p[0]):
        lines.append('%s%s%s' % (rjust(mid, 4), 20 * ' ', concept))

    lines.append('')
    for char in ASJPCODES:
        lines.append(char)
    lines.append('')
    lines.append('')
    return '\n'.join(lines)


@attr.s
class Doculect:
    id = attr.ib()
    name = attr.ib()
    classification_wals = attr.ib()
    classification_ethnologue = attr.ib()
    classification_glottolog = attr.ib()
    latitude = attr.ib()
    longitude = attr.ib()
    number_of_speakers = attr.ib()
    recently_extinct = attr.ib()
    long_extinct = attr.ib()
    year_of_extinction = attr.ib()
    code_wals = attr.ib()
    code_iso = attr.ib()
    synsets = attr.ib(converter=lambda v: [vv for vv in v if vv.words])

    @property
    def asjp_name(self):
        name = self.name
        if '"' in name:
            name = name.split('"')[1]
        return name.replace("'", "").replace(" ", "_").replace("/", "_").upper()

    @property
    def wals_family(self):
        return self.classification_wals.split('.')[0] if self.classification_wals else None

    @property
    def wals_genus(self):
        return self.classification_wals.split('.')[1] if self.classification_wals else None

    @classmethod
    def from_txt(cls, txt, **kw):
        """
        The second line gives properties of the languages, in fixed format separated by blanks
        (not tabs), so the columns are important.

        Col. 2: 3 if the language is the first one in a new WALS family, 2 if it’s the first
        language in a new WALS genus, 1 otherwise.

        Col. 4-10, right justified: latitude in degrees and
        hundredths of a degree; minus means South.

        Col. 12-18, right justified: longitude in degrees a
        nd hundredths of a degree; minus means West.
        Latitudes and longitudes were ascertained from WALS, or from the maps in Ethnologue or
        Moseley and Asher (1994), or from information in the source for the list.

        Col. 19-30, right justified: number of speakers, from Ethnologue. This number always
        refers to the entire language, as defined in Ethnologue, even if the list itself
        refers to a dialect. The number is

            0 if the number of speakers is unknown;
            -1 if the language is recently extinct;
            -2 if the language is long extinct;
            or if the approximate date of extinction is known, the date is preceded by a minus
            sign.

        In the ASJP software, if there is a date in the first line of the entire file, lists
        with earlier extinction dates here are ignored, as are lists with -2; otherwise, all
        lists are read.

        Col. 34-36: three-letter WALS code, if any.

        Col. 40-42: three-letter ISO639-3 code, if any. This code is included for languages in
        previous editions of Ethnologue even if they aren’t in the 17th edition. Languages
        that lack an ISO639-3 code but can be placed in the Ethnologue classification are
        given a code consisting of two letters followed by the number 0 (for use in ASJP
        software).
        """
        lines = nfilter(txt.split('\n'))
        m = LANGUAGE_LINE_PATTERN.match(lines[0])
        assert m
        line = lines[1]
        try:
            lat = line[4:11].strip()
            lng = line[11:18].strip()
            nos = int(line[18:30].strip() or 0)
            code_wals = line[33:36].strip() or None
            code_iso = line[39:42].strip() or None
        except ValueError:  # pragma: no cover
            _, lat, lng, nos, code_wals, code_iso = line.strip().split()
            nos = int(nos)
        return cls(
            id=m.group('name'),
            name=' '.join(s.capitalize() for s in m.group('name').split('_')),
            classification_wals=m.group('w') if m.group('w') else None,
            classification_ethnologue=m.group('e') if m.group('e') else None,
            classification_glottolog=m.group('g') if m.group('g') else None,
            latitude=float(lat) if lat else None,
            longitude=float(lng) if lng else None,
            number_of_speakers=nos if nos >= 0 else 0,
            recently_extinct=nos == -1 or nos < -2,
            long_extinct=nos == -2,
            year_of_extinction=abs(nos) if nos < -2 else None,
            code_wals=code_wals,
            code_iso=code_iso,
            synsets=[Synset.from_txt(line) for line in lines[2:] if '\t' in line],
        )

    def __str__(self):
        return self.to_txt()

    def to_txt(self, add_missing=False, full_list=False, wals_marker='1'):
        """render the wordlist in the ASJP plain text format.
        """
        nos = self.number_of_speakers
        if self.year_of_extinction:
            nos = -self.year_of_extinction
        elif self.recently_extinct:
            nos = -1
        elif self.long_extinct:
            nos = -2
        lines = [
            '%s{%s|%s@%s}' % (
                self.id,
                self.classification_wals or '',
                self.classification_ethnologue or '',
                self.classification_glottolog or ''),
            '%s%s%s%s%s%s' % (
                wals_marker.rjust(2),
                ('' if self.latitude is None else ('%.2f' % self.latitude)).rjust(8),
                ('' if self.longitude is None else ('%.2f' % self.longitude)).rjust(8),
                str(nos).rjust(12),
                (self.code_wals or '').rjust(6),
                (self.code_iso or '').rjust(6))]
        synsets = {s.meaning_id: s for s in self.synsets}
        for mid, concept in sorted(MEANINGS_ALL.items(), key=lambda i: i[0]):
            if mid in synsets:
                lines.append(str(synsets[mid]))
            elif add_missing and ((mid in MEANINGS) or full_list):
                lines.append(Synset.format(mid))
        return '\n'.join(lines)