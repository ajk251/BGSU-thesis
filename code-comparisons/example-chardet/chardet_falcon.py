
import csv

from collections import defaultdict, namedtuple
from os import listdir
from os.path import dirname, isdir, join, realpath, relpath, splitext
from typing import List

from Falcon.predicates import predicate, on_fail_false
from Falcon.domains import domain

import iconv

import chardet
from languages import LANGUAGES                             # this is a chardet thing that contains metadata
# from chardet.metadata.languages import LANGUAGES


# -----------------------------------------------

# the directory of the test encodings
PATH = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/chardet/tests'

MISSING_ENCODINGS = {"iso-8859-2",
                     "iso-8859-6",
                     "windows-1250",
                     "windows-1254",
                     "windows-1256"}

# EXPECTED_FAILURES = {"tests/iso-8859-7-greek/disabled.gr.xml",
#                      "tests/iso-8859-9-turkish/_ude_1.txt",
#                      "tests/iso-8859-9-turkish/_ude_2.txt",
#                      "tests/iso-8859-9-turkish/divxplanet.com.xml",
#                      "tests/iso-8859-9-turkish/subtitle.srt",
#                      "tests/iso-8859-9-turkish/wikitop_tr_ISO-8859-9.txt"}

EXPECTED_FAILURES = {"disabled.gr.xml",
                     "_ude_1.txt",
                     "_ude_2.txt",
                     "divxplanet.com.xml",
                     "subtitle.srt",
                     "wikitop_tr_ISO-8859-9.txt"}

f_sample = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-chardet/lang-translation.csv'

# Aliases ---------------------------------------
# these are aliases for the language encodings, like windows-1255 ≡ cp1255      (that is no difference)
#   this also includes aliases for encodings that are practically similiar, but not equal, like iso-8859-1 ⇔ iso-8859-15
#   these have several small difference ￫ confusing them is inevitable, and for the purposees of this test, okay

# create a key-value mapping of codec -> alias & alias -> codec
# from this table:
#   https://docs.python.org/3/library/codecs.html#standard-encodings

# get the list of aliases
f_aliases = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-chardet/encoding-aliases.csv'

with open(f_aliases, 'r') as file:

    aliases = defaultdict(set)
    reader = csv.reader(file, delimiter=',')

    _ = next(reader)                # skip the header

    for codec, aliases_ in reader:

        values = aliases_.split(',')

        for alias in values:
            aliases[codec].add(alias)
            aliases[alias].add(codec)

# Domains ---------------------------------------

# the test file domains

@domain(alias='TestFiles')
def get_test_docs():
    """Yields tuples of paths and encodings to use for test_encoding_detection"""


    # these map specific encoding to langauge
    langs = {'euc-jp': 'japanese', 'big5': 'chinese', 'shift_jis': 'japanese',
             'gb2312': 'chinese', 'euc-kr': 'korean', 'euc-tw': 'taiwan', 'cp932': 'japanese', 
             'maccyrillic': 'russian', 'cp949': 'korean', 'tis-620': 'thai', 'iso-2022-jp': 'japanese',
             'iso-2022-kr': 'korean', 'ibm866': 'russian', 'ibm855': 'russian', 'kio8-r': 'russian'}

    # This was modified from the original Chardet Test
    
    base_path = PATH #relpath(join(dirname(realpath(__file__)), "tests"))

    for encoding in listdir(base_path):
        
        path = join(base_path, encoding)

        # Skip files in tests directory
        if not isdir(path):
            continue
        
        # Remove language suffixes from encoding if present
        encoding = encoding.lower()
        
        # encoding = encoding.split('-')[0]
        lang = encoding.split('-')[-1].capitalize()
        language = lang.lower() if lang in LANGUAGES.keys() else ''

        postfix = "-" + language.lower()
        
        if encoding.endswith(postfix):
            encoding = encoding.rpartition(postfix)[0]

        # can it be infered from the encoding label?
        if encoding in langs:
            language = langs[encoding]

        # Test encoding detection for each file we have of encoding for
        for file_name in listdir(path):
        
            ext = splitext(file_name)[1].lower()
        
            if ext not in [".html", ".txt", ".xml", ".srt"]:
                continue

            language = None if language == '' else language

            full_path = join(path, file_name)
            test_case = full_path, encoding, language, file_name

            # print('file: ', file_name)
        
            yield test_case

# ----------------------

# the test character sets from the csv
Sample = namedtuple('Sample', 'origin,dest,name,google_code,generated,translated')
Case   = namedtuple('Case',   'origin,dest,name,google_code,generated,translated,encoded,encoding')


# helper function to load csv into List[Sample]
def _get_samples(f) -> List[Sample]:
    """Gets the data (meta..., generated, translated text) from the csv and returns it as a List[Sample]"""

    samples = []

    with open(f, 'r', encoding='utf-16') as file:

        reader = csv.reader(file)

        _ = next(reader)            # can ignore the header

        for row in reader:
            
            sample = Sample(row[0], row[1], row[2], row[3], row[4], row[5])
            samples.append(sample)

    return samples


@domain(alias='RandomEncodings')
def get_encodings():

    # loads the samples as Sample
    samples = _get_samples(f_sample)

    # from here:
    #   https://chardet.readthedocs.io/en/latest/supported-encodings.html
    #   ie, this is based on chardet's supported languages

    # this creates a dict of languages & encodings

    # I'm not sure about 'western european'       --> iso-8859-1, windows-1252, latin-1
    european = ('french', 'spanish', 'german', 'italian', 'portguese')

    languages = dict.fromkeys(european, ('iso-8859-1', 'windows-1252', 'latin-1'))
    languages.update({'chinese-traditional': ['Big5', 'GB2312'],
                 'chinese-simplified': ['GB18030', 'EUC-2312', 'ISO-2022-CN'],
                 'japanese': ['EUC-JP', 'SHIFT_JIS', 'ISO-2022-JP'],
                 'korean': ['EUC-KR', 'ISO-2022-KR'],
                 'hungarian': ['ISO-8859-2', 'windows-1250']})

    for lang in LANGUAGES.values():
        languages[lang.name.lower()] = lang.charsets

    keys = 'origin,dest,name,google_code,generated,translated,encoded,encoding'.split(',')

    # build all encodings
    for sample in samples:

        name = sample.name.lower()

        if name == 'english':
            continue
        
        for e in languages[name]:

            # iconv stuff
            try:
                s = iconv.open(e, 'utf-16')
                # result = s.iconv(bytearray(sample.translated, encoding='utf-16'))
                result = bytearray(sample.translated, encoding='utf-16')
            except ValueError as error:
                # this is iconv not recognizing the encoding (either 'in' or 'out')
                # warnings.warn(f"Encoding {e} not supported. [Language {name}]")
                continue

            # case = Case(sample.origin, sample.dest, sample.name, sample.google_code,
            #             sample.generated, sample.translated, result, e)
            case = {name: value for name, value in zip(keys, (sample.origin, sample.dest, sample.name, sample.google_code,
                                                              sample.generated, sample.translated, result, e))}
            
            yield case


# wrapper function ---------------

# TODO: chardet.detect_all

def detect_from_example(case):
    """A wrapper around chardet.detect. Returns dict of the chardet response and test-case meta data"""
    
    result = chardet.detect(case['encoded'])
    result_all = True #chardet.detect_all(case['encoded'])[0]
    return {**case, 'chardet': result, 'agrees': result == result_all}


def detect_from_filename(domain):

    file, encoding, language, filename = domain

    with open(file, 'rb') as f:

        input = f.read()
        result = chardet.detect(input)
        result_all = chardet.detect_all(input)[0]

        outcome = {**result, 'file': file, 'expected-encoding': encoding,
                  'expected-lang': language, 'filename': filename, 'agrees': result == result_all}

    return outcome

# predicates ------------------------------------

@predicate(alias=['agrees?'])
def both_detects_agree(outcome) -> bool:
    return outcome['agree']

@predicate(alias=['has-both-right?'])
def encoding_and_language(outcome) -> bool:

    if outcome['encoding'] is None: return False
    elif outcome['language'] is None: return False

    return outcome['encoding'].lower() == outcome['expected-encoding'] and \
           outcome['language'].lower() == outcome['expected-lang']


@predicate(alias='has-encoding-right?', doc_error=True)
def encoding_detection(outcome) -> bool:
    """Detected encoding does not match expected encoding"""
    if outcome['encoding'] is None: return False
    return outcome['encoding'].lower() == outcome['expected-encoding']


@predicate(alias=['has-lang-right?', 'has-language-right?'])
def detected_language(outcome) -> bool:
    if outcome['language'] is None: return False
    return outcome['language'].lower() == outcome['expected-lang']


@predicate(alias=['has-neither?'])
def both_missing(outcome) -> bool:
    return outcome['encoding'] is None and outcome['language'] is None


@predicate(alias=['expected-failure?'])
def expected_failure(outcome) -> bool:
    
    if outcome['file'] in EXPECTED_FAILURES:
        return True
    elif outcome['expected-encoding'] in MISSING_ENCODINGS:
        return True

    return False


@predicate(alias=['has-both-wrong?'])
def both_wrong(outcome): 

    if outcome['encoding'] is None: return False
    elif outcome['language'] is None: return False

    return outcome['encoding'].lower() != outcome['expected-encoding'] and \
           outcome['language'].lower() != outcome['expected-lang']


# for the random encodings ----------------------
# helper functions ---------------

def _ballpark(outcome) -> bool:
    """The actual encoding is similiar to - but not - the detected encoding"""

    close = False
    result = outcome['encoding']

    if result is None: return False

    s = outcome['chardet']['encoding'].lower()                  # source
    d = result.lower()                                          # destination

    if s == d:
        close = False                                           # it's a match, not close
    elif d in aliases[s]:
        close = True                                            # note: aliases are "mostly" compatible
    elif s.startswith('iso') and d.startswith('iso'):     
        source = s.split('-')                                   # ie  iso-1234-. == iso-1234-.
        destination = d.split('-')
        close = source[1] == destination[1]
    elif s.startswith('windows') and d.startswith('windows'):   
        close = s[:-1] == d[:-1]                                # ie they should only differ by the last digit    

    return close

def _encoding(outcome) -> bool:
    """Tests that the expected encoding matches the actual encoding."""

    if outcome['chardet']['encoding'] is None: return False
    elif outcome['encoding'] is None: return False

    return outcome['encoding'].lower() == outcome['encoding'].lower()

def _language(outcome) -> bool:
    """Tests that the expected language matches the actual language."""

    if outcome['chardet']['language'] is None: return False

    # this line is mostly for chinese-traditional ⇔ chinese
    return outcome['name'].lower() == outcome['chardet']['language'].lower() or \
           outcome['chardet']['language'].lower() in outcome['name'].lower()        

# predicates ---------------------

@predicate(alias=['neither-detected?', 'neither?'])
def is_neither(outcome) -> bool:
    return outcome['encoding'] is None and outcome['language'] is None


@predicate(alias=['encoding&language?', 'both-right?'])
def is_encoding_and_language_correct(outcome) -> bool:
    return _encoding(outcome) and _language(outcome)


@predicate(alias=['ballpark&language?', 'both-close?'])
def in_ballpark_and_language_correct(outcome) -> bool:
    return _ballpark(outcome) and _language(outcome)


@predicate(alias=['encoding?'])
def is_encoding_correct(outcome) -> bool:
    return _encoding(outcome)

@predicate(alias=['ballpark?'])
def is_ballpark(outcome) -> bool:
    return _ballpark(outcome)


@predicate(alias=['language?'])
def is_just_language(outcome) -> bool:
    return _language(outcome)


@predicate(alias=['both-wrong?'])
def is_both_wrong(outcome) -> bool:
    return not _encoding(outcome) and not _language(outcome)


@predicate(alias=['either-wrong?'])
def is_either_wrong(outcome):
    return not _encoding(outcome) or not _language(outcome)


for case in get_encodings():

    outcome = detect_from_example(case)
    
    a = is_neither(outcome)
    b = is_encoding_and_language_correct(outcome)
    c = in_ballpark_and_language_correct(outcome)
    d = is_encoding_correct(outcome)
    e = is_ballpark(outcome)
    f = is_just_language(outcome)
    g = is_both_wrong(outcome)
    h = is_either_wrong(outcome)

    print(a, b, c, d, e, f, g, h)

# for case in get_test_docs():
#     print(case)