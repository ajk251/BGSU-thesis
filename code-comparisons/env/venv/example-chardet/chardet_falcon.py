
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

EXPECTED_FAILURES = {"tests/iso-8859-7-greek/disabled.gr.xml",
                     "tests/iso-8859-9-turkish/_ude_1.txt",
                     "tests/iso-8859-9-turkish/_ude_2.txt",
                     "tests/iso-8859-9-turkish/divxplanet.com.xml",
                     "tests/iso-8859-9-turkish/subtitle.srt",
                     "tests/iso-8859-9-turkish/wikitop_tr_ISO-8859-9.txt"}

f_sample = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-chardet/lang-translation.csv'

# Aliases ---------------------------------------
# these are aliases for the language encodings, like windows-1255 ≡ cp1255      (that is no difference)
#   this also includes aliases for encodings that are practically similiar, but not equal, like iso-8859-1 ⇔ iso-8859-15
#   these have several small difference ￫ chardet detecting one and not the other is not a (major) problem, but inevitable

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

@domain(alias='Files')
def get_test_docs():
    """Yields tuples of paths and encodings to use for test_encoding_detection"""
    
    base_path = PATH #relpath(join(dirname(realpath(__file__)), "tests"))

    for encoding in listdir(base_path):
        
        path = join(base_path, encoding)
        # Skip files in tests directory
        if not isdir(path):
            continue
        
        # Remove language suffixes from encoding if present
        encoding = encoding.lower()

        for language in sorted(LANGUAGES.keys()):
            postfix = "-" + language.lower()
            if encoding.endswith(postfix):
                encoding = encoding.rpartition(postfix)[0]
                break

        # # Skip directories for encodings we don't handle yet.
        # if encoding in MISSING_ENCODINGS:
        #     continue

        # Test encoding detection for each file we have of encoding for
        for file_name in listdir(path):
        
            ext = splitext(file_name)[1].lower()
        
            if ext not in [".html", ".txt", ".xml", ".srt"]:
                continue

            full_path = join(path, file_name)
            test_case = full_path, encoding

            # if full_path in EXPECTED_FAILURES:
            #     test_case = pytest.param(*test_case, marks=pytest.mark.xfail)
        
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

    # build all encodings
    for sample in samples:

        name = sample.name.lower()

        if name == 'english':
            continue
        
        for e in languages[name]:

            # iconv stuff
            try:
                s = iconv.open(e, 'utf-16')
                result = s.iconv(bytearray(sample.translated, encoding='utf-16'))
            except ValueError as error:
                # this is iconv not recognizing the encoding (either 'in' or 'out')
                # warnings.warn(f"Encoding {e} not supported. [Language {name}]")
                continue

            case = Case(sample.origin, sample.dest, sample.name, sample.google_code,
                        sample.generated, sample.translated, result, e)
            
            yield case

# ----------------------

# a translated text domain?
# …

# predicates ------------------------------------
# test that the encoded matches expected

@predicate(alias='matches?', doc_error=True)
def encoding_detection(encoding) -> bool:
    """Detected encoding does not match expected encoding"""
    return encoding == detected['encoding']


def expected_failure(encoding) -> bool:
    pass




# for the random encodings -------
# predicates ---------------------

detected = {'encoding': None}

# helper functions ---------------
def _ballpark(case) -> bool:
    """The actual encoding is similiar to - but not - the detected encoding"""

    close = False
    result = detected['encoding']

    if result is None: return False

    s = case.encoding.lower()                   # source
    d = result.lower()                          # destination

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

def _encoding(case) -> bool:

    if detected['encoding'] is None: return False

    return case.encoding.lower() == detected['encoding'].lower()

def _language(case) -> bool:

    if detected['language'] is None: return False

    # this line is mostly for chinese-traditional ⇔ chinese

    return case.name.lower() == detected['language'].lower() or \
           detected['language'].lower() in case.name.lower()        

# --------------------------------

@predicate(alias=['neither-detected?', 'neither?'])
def is_neither(case) -> bool:
    return detected['encoding'] is None and detected['language'] is None


@predicate(alias=['encoding&language?', 'both-right?'])
def is_encoding_and_language_correct(case) -> bool:
    return _encoding(case) and _language(case)


@predicate(alias=['ballpark&language?', 'both-close?'])
def in_ballpark_and_language_correct(case) -> bool:
    return _ballpark(case) and _language(case)


@predicate(alias=['encoding?'])
def is_encoding_correct(case) -> bool:
    return _encoding(case)

@predicate(alias=['ballpark?'])
def is_ballpark(case) -> bool:
    return _ballpark(case)


@predicate(alias=['language?'])
def is_just_language(case) -> bool:
    return _language(case)


@predicate(alias=['both-wrong?'])
def is_both_wrong(case) -> bool:
    return not _encoding(case) and not _language(case)


@predicate(alias=['either-wrong?'])
def is_either_wrong(case):
    return not _encoding(case) or not _language(case)



# temp tests ====================================

# for file in get_test_docs():
#     print(file)

# for case in get_encodings():
    # print(case.translated)

# for case in get_encodings():

#     detected = chardet.detect(case.encoded)
    
#     if is_encoding_and_language_correct(case): 
#         print('e & l: ' )
#     elif in_ballpark_and_language_correct(case):
#         print('b & l: ' )
#     elif is_encoding_correct(case):
#         print('e:  ', )
#     elif is_ballpark(case):
#         print('b: ', )
#     elif is_just_language(case):
#         print('just lang')
#     elif is_both_wrong(case):
#         print('both wrong!')
#     elif is_either_wrong(case):
#         # print('either')
#         print('EITHER ', case.name, case.encoding, detected['encoding'], detected['language'])
#     elif is_neither(case):
#         print('n: ', )
#     else:
#         raise ZeroDivisionError('You cant do that!')
#         print('whoops! ', case.name, case.encoding, detected['encoding'], detected['language'])
    