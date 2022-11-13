
import pathlib
import random
from secrets import choice

from string import printable, whitespace
from typing import List

import chardet
from chardet.metadata.languages import LANGUAGES

# from falcon.predicate import predicates
# from falcon.domain import domain

# ***********************************************

# [docs]
#     https://chardet.readthedocs.io/en/latest/index.html

# Here is a link from Chardet [How it works]
#     https://www-archive.mozilla.org/projects/intl/universalcharsetdetection

# [repo]
#     https://github.com/chardet/chardet

# [chardet is bad]
#     https://medium.com/analytics-vidhya/python-character-detection-chardet-27e46218f0bb
#     https://stackoverflow.com/questions/39142778/how-to-determine-the-language-of-a-piece-of-text

# [but]
#     https://pythonawesome.com/the-universal-character-encoding-detector-for-python/

# ￫ most tools try to only detect language, chardet is focused on encodings


# [encodings]
# [windows-1255]
#     https://en.wikipedia.org/wiki/Windows-1255
#     https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit1255.txt

# ISO/IEC 8859-7
# all the greeks 
#   http://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-7.TXT

# cp1251 -> all cyrillic
#   https://www.man7.org/linux/man-pages/man7/cp1251.7.html

# ***********************************************


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

PATH = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/chardet/tests'
PY_ENCODINGS = ['utf-8', 'ascii', 'latin-1', 'ISO-8859-1', 'ISO-8859-15', 'ISO-8859-7']
BOM = chr(int('0xFEFF', base=16))       # for utf-8 & 16

# -----------------------------------------------

def generate_alphabet(start: str, end: str, encoding: str) -> str:

    start: int = int(start, base=16)
    end: int = int(end, base=16)

    current = start
    chars = []
    alphabet = ''

    while current <= end:

        try:
            char = str(chr(current))
            # chars.append(char)
            alphabet += char
        except UnicodeEncodeError:
            continue

        current += 1

    for char in chars:

        try:
            # alphabet += char
            alphabet.encode(encoding)
        except UnicodeEncodeError:
            continue

    # alphabet = ''.join(alphabet).encode(encoding)
    alphabet.encode(encoding)

    return alphabet


encodings = dict.fromkeys(["ascii", "utf-8", "utf-16", "utf-32", "iso-8859-7", "iso-8859-8", "windows-1255"], None)

encodings['ascii'] = printable + whitespace

# encodings['iso-8859-7']   = generate_alphabet('0x0020', '0x03CE', 'iso-8859-7')
# encodings['iso-8859-8']   = generate_alphabet('0x0020', '0x00FE', 'iso-8859-8')
# encodings['windows-1255'] = generate_alphabet('0x0000', '0x00FF', 'windows-1255')
# encodings['windows-1255'] = [()]
# ---------------------------------------------------------

# predicates:
#   missing?
#   fails?
#   matches? <expected> <found>
#   confidence-at-least?
#   high? low? confidence

# groups:
#   is-mix-up?                            mixed-up
#   no-lang?
#   mixed-up-lang? problematic?

# encoding BIG5

# create mapping
#  R   - russian
#  TW  - taiwan
#  JP  - japanese
#  JIS - japanese            

# this is from the chardet test code ----------------------

import textwrap
from difflib import ndiff
from os import listdir
from os.path import dirname, isdir, join, realpath, relpath, splitext
from pprint import pformat

# ---------------------------------------------------------

def build_range(start, end, encoding='windows-1255'):

    start = int(start, base=16)
    end   = int(end, base=16)+1

    return bytearray(tuple(range(start, end)))

# ---------------------------------------------------------

def gen_test_params():
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

        # Skip directories for encodings we don't handle yet.
        if encoding in MISSING_ENCODINGS:
            continue

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


# ---------------------------------------------------------


def load_examples_test():


    cases = pathlib.Path(PATH)

    for example_dir in cases.iterdir():

        encoding = example_dir.name

        if not example_dir.is_dir():
            continue

        for example in example_dir.iterdir():

            # encoding, lang = encoding.split('-')
            
            print(encoding,  ' file: ', example.stem)

            with open(example, 'rb') as file:
                print('\t', chardet.detect(file.read()))


# detect and agree
# based on this function:
#   test_detect_all_and_detect_one_should_agree

def detect_agree():

    encodings = ["ascii", "utf-8", "utf-16", "utf-32",
                 "iso-8859-7", "iso-8859-8", "windows-1255"] 
                 # greek, hebrew/hebrew 

    for encoding in encodings:

        # build a random pool of ascii characters
        pool = printable + whitespace
        n = random.randint(500, 1_000)
        text = str((random.choices(pool, k=n))) #.encode(encoding=encoding, errors='ignore')

        # t = text.encode(encoding)
        t = bytearray(text, encoding=encoding)

        result = chardet.detect(t)
        results = chardet.detect_all(t)

        print(encoding, result['encoding'])
        print(encoding, results)
        print()


def test():

    for encoding in ["ascii", "utf-8", "utf-16", "utf-32", "iso-8859-7", "iso-8859-8", "windows-1255" ]:

        # text = 'hello world how are you !@#%@#^@#%$!@^#@%^$%^&*%^(&*(%^?>":PL{"P?><?}{|}{">"><'
        text = printable

        print('encoded: ', encoding)

        try:
            data = text.encode(encoding)
            print(chardet.detect(data))
        except UnicodeEncodeError:
            continue


def load_characters(start, end):

    chars = []

    start = int(start, base=16)
    end   = int(end, base=16)

    for c in range(start, end+1):
        try:
            c = chr(c)
            chars.append(c)
        except UnicodeEncodeError as error:         # it doesn't exist
            continue

    return chars


def build_encoding(encoding='windows-1255'):

    # build a 256-value array of bytes
    bytes = bytearray(tuple(range(int('00', base=16), int('FF', base=16)+1)))

    # treat it as a string -> not all bytes are valid & they have to be ignored
    chars = str(bytes, encoding=encoding, errors='ignore')

    # chardet needs a bytearray though
    bchars = bytearray(chars, encoding=encoding)

    print(str(bchars, encoding=encoding))

    result = chardet.detect(bchars)

    print(f'encoding: {encoding} detected: {result["encoding"]}')


def detect_random_encoding(encoding='windows-1255'):

    # build pool of numbers
    # nums = tuple(range(int('00', base=16), int('FF', base=16)+1))
    nums = tuple(range(int('7e', base=16), int('FF', base=16)+1))


    n = random.randint(1, 10_000)
    char_pool = random.choices(nums, k=n)

    bytes = bytearray(char_pool)

    # treat it as a string -> not all bytes are valid -> they have to be ignored
    chars = str(bytes, encoding=encoding, errors='ignore')

    # chardet needs a bytearray though
    bchars = bytearray(chars, encoding=encoding)

    result = chardet.detect(bchars)

    print(f'n: {n}  encoding: {encoding}    detected encoding: {result["encoding"]}')
    print(result)
    print()

# ================================================

# load_examples_test()

print('detect & agree: ')
detect_agree()

print('encoding test: ')
test()

print('-' * 25)
print('detect windows-1255')
hebrew = 'abcdefgױא'.encode('windows-1255')
print(hebrew)
print(chardet.detect(hebrew))
print()

print('-' * 25)
print('detect russian:')
print(chardet.detect("Я люблю вкусные пампушки".encode('cp1251')))

print('detect hebrew:')
hebrew = ''.join(load_characters('0590', '05FF'))
print(chardet.detect(bytearray(hebrew, encoding='windows-1255', errors='ignore')))  # 'errors' is ignore characters that have no mapping


print('-' * 25)
print('\nsanity check')

# chars = str(printable).encode('utf-8')
# print('length: ', len(chars))           # length is 100
# print('encoding: ', bytes.decode(chars, encoding='utf-8'))


# alpha = bytearray(printable, encoding='utf-16')
# beta  = str(alpha.decode(encoding='utf-8', errors='ignore')).encode('utf-8')

# print(beta)
# print('length: ', len(beta))            # so the length is 200! 
# # print(beta)

text = 'Hello world'
text_1255 = text.encode('windows-1255')
print(len(text), text_1255)
original_text = text_1255.decode("windows-1255")
print(len(original_text), original_text)

# original encoding￫decoding
# https://www.adamsmith.haus/python/answers/how-to-encode-and-decode-a-string-in-python
text =  'String to encode'
text_utf = text.encode("utf_16")
print(len(text), text_utf)
original_text = text_utf.decode("utf_16")
print(len(original_text), original_text)

print('*' * 25)

# windows1255 = bytearray(tuple(range(int('00', base=16), int('FF', base=16)+1)))
# windows1255 = windows1255.decode('windows-1255', errors='ignore')

# print(chardet.detect(windows1255))
# print(windows1255.decode('utf-8', errors='ignore'))

print('*' * 10)

# latin1 = bytearray(tuple(range(int('00', base=16), int('FF', base=16)+1)))
# print(chardet.detect(latin1))
# print(latin1.decode('utf-8', errors='ignore'))


build_encoding('windows-1250')              # hungarian
build_encoding('windows-1251')              # russian
build_encoding('windows-1252')              # western european
build_encoding('windows-1253')              # greek
build_encoding('windows-1255')              # hebrew

print('*' * 10)

detect_random_encoding(encoding='windows-1250')
detect_random_encoding(encoding='windows-1251')
detect_random_encoding(encoding='windows-1252')
detect_random_encoding(encoding='windows-1253')
detect_random_encoding(encoding='windows-1255')
detect_random_encoding(encoding='maccyrillic')
detect_random_encoding(encoding='utf-8')
detect_random_encoding(encoding='utf-16')           # only 8 are encodeded
detect_random_encoding(encoding='utf-32')
detect_random_encoding(encoding='ascii')
detect_random_encoding(encoding='iso-8859-7')       # greek
detect_random_encoding(encoding='iso-8859-8')       # hebrew

# this technique works, it just doesn't detect it accurately

e = 'MacCyrillic'

ns = build_range('00', 'FF', e)
text = str(ns, encoding=e, errors='ignore')
print(text)

txt = bytearray(text, encoding=e)
print(chardet.detect(txt))
print(chardet.detect_all(txt))


# spanish = '¿Hola cómo estás hoy?'
spanish = bytearray('¿Hola cómo estás hoy?'.encode('latin-1')) #.encoding='latin-1')
print('\nSpanish: ', spanish)
print(str(spanish, encoding='latin-1', errors='ignore'))


russian = bytearray('Здравствуйте! Как вы сегодня?'.encode('windows-1251'))
print(russian)
print(chardet.detect(russian))
print(str(russian, encoding='windows-1251', errors='ignore'))


# import urllib.request

# translate = urllib.request.urlopen('https://translate.google.com/?sl=en&tl=ru&text=hello%2C%20how%20are%20you%20doing%20today%3F&op=translate')

# print(translate.read())