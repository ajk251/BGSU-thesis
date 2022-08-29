
import csv
import encodings
import random
from typing import NamedTuple
import warnings

import chardet
import iconv

# import languages
from languages import LANGUAGES

from collections import defaultdict, namedtuple
from random import choice, choices, randint
from time import sleep
# from chardet.metadata.languages import LANGUAGES

from googletrans import Translator

# to get google translate to work:
#   https://stackoverflow.com/questions/70485804/google-translate-in-python


# ----------------------

Sample = namedtuple('Sample', 'origin,dest,name,google_code,generated,translated')
Case   = namedtuple('Case', 'origin,dest,name,google_code,generated,translated,encoded,encoding')

# ----------------------
# generate a list of 4k words to generate text
# from here:
#   https://raw.githubusercontent.com/pkLazer/password_rank/master/4000-most-common-english-words-csv.csv

f = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/chardet/4000-most-common-english-words.csv'
f_sample = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-chardet/lang-translation.csv'

with open(f, 'r') as file:
    corpus = tuple(map(lambda w: w.strip('\n'), file.readlines()))

# ----------------------

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

# these are extentions that I added based on:
# https://en.wikipedia.org/wiki/Windows-1252
# https://en.wikipedia.org/wiki/Windows-1255
# https://en.wikipedia.org/wiki/ISO/IEC_8859-6
# https://en.wikipedia.org/wiki/Thai_Industrial_Standard_620-2533

# -----------------------------------------------

# this downloads the text & translates

def save_to_csv(n_sentences=10):

    f = './lang-translation.csv'
    translator = Translator()

    with open(f, 'w', encoding='utf-16') as file:

        header = 'source, dest, lang-name, google-code, generated-text, translated\n'
        file.write(header)

        for i in range(n_sentences):

            sentence = generate_words()

            data = ','.join(('en', 'en', 'English', 'en', sentence, sentence)) + '\n'
            file.write(data)

            for language in languages.LANGUAGES.values():

                code = language.iso_code

                # the mappings don't agree
                if code == 'cz':
                    code = 'cs'
                elif code == 'bg':
                    code = 'be'

                translated = translator.translate(sentence, src='en', dest=code)

                data = ','.join(('en', code, language.name, language.iso_code, sentence, translated.text.strip('\n'))) + '\n'
                file.write(data)

                delay = randint(1, 10)
                sleep(delay)

                print(f"Language: {language.name} [{code}] (waiting {delay})\t\t…{i}")
            
            # and now chinese traditional & simplified
            translated = translator.translate(sentence, src='en', dest='zh-CN')
            data = ','.join(('en', 'zh-CN', 'chinese-simplified', 'zh-cn', sentence, translated.text.strip('\n'))) + '\n'
            file.write(data)

            sleep(delay)

            translated = translator.translate(sentence, src='en', dest='zh-TW')
            data = ','.join(('en', 'zh-TW', 'chinese-traditional', 'zh-tw', sentence, translated.text.strip('\n'))) + '\n'
            file.write(data)

            sleep(delay)

            # japanese
            translated = translator.translate(sentence, src='en', dest='ja')
            data = ','.join(('en', 'ja', 'japanese', 'ja', sentence, translated.text.strip('\n'))) + '\n'
            file.write(data)

            sleep(delay)

            # korean
            translated = translator.translate(sentence, src='en', dest='ko')
            data = ','.join(('en', 'ko', 'korean', 'ko', sentence, translated.text.strip('\n'))) + '\n'
            file.write(data)


# -----------------------------------------------

def generate_words(max_words=12, max_sentences=50):

    sentences = []
    punc = '.!?'

    n_sentences = randint(1, max_sentences)

    for _ in range(n_sentences):
        n_words = randint(1, max_words)
        sentence = ' '.join(choices(corpus, k=n_words)) + choice(punc)
        sentences.append(sentence)


    return ' '.join(sentences)


def get_samples(f):
    """Gets the data (meta..., generated, translated text) from the csv and returns it as a List[Sample]"""

    samples = []

    with open(f, 'r', encoding='utf-16') as file:

        reader = csv.reader(file)

        _ = next(reader)            # can ignore the header

        for row in reader:
            
            sample = Sample(row[0], row[1], row[2], row[3], row[4], row[5])
            samples.append(sample)

    return samples


def generate_encodings(samples):

    # TODO: make this an algorithm

    # from here:
    #   https://chardet.readthedocs.io/en/latest/supported-encodings.html
    #   ie, this is based on chardet's supported languages

    # I'm not sure about 'western european'       --> iso-8859-1, windows-1252, latin-1
    european = ('french', 'spanish', 'german', 'italian', 'portguese')

    languages = dict.fromkeys(european, ('iso-8859-1', 'windows-1252', 'latin-1'))
    languages.update({'chinese-traditional': ['Big5', 'GB2312'],
                 'chinese-simplified': ['GB18030', 'EUC-2312', 'ISO-2022-CN'],
                 'japanese': ['EUC-JP', 'SHIFT_JIS', 'ISO-2022-JP'],
                 'korean': ['EUC-KR', 'ISO-2022-KR'],
                 'hungarian': ['ISO-8859-2', 'windows-1250']})

    for lang in LANGUAGES.values():
        # encodings[lang.name] = lang.charsets
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
                # this is iconv not recognizing the encoding
                # warnings.warn(f"Encoding {e} not supported. [Language {name}]")
                continue

            case = Case(sample.origin, sample.dest, sample.name, sample.google_code, sample.generated,
                        sample.translated, result, e)

            # print(name, e)
            # print()
            
            yield case


# -----------------------------------------------

# def save_sentences()

# from googletrans import Translator

# translator = Translator()
# result = translator.translate('Hello world. How are you doing today?', src='en', dest='es')

# print(result.text)

# iconv stuff
# s = iconv.open('latin1', 'utf-8')
# result = s.iconv(bytearray(result.text, encoding='utf-8'))

# print(str(result, encoding='latin-1'))
# print(chardet.detect(result))

# print(generate_words())

# print(languages.LANGUAGES)

# save_to_csv()


# • encoding ↔ encodings
# • language ↔ language 
# • confidence > .70
# • detect ↔ detect-all
# • ballpark   
# • fail-all
# • no-language
# • no-encoding
# • no-confidence
# • not-supported           ['ISO8859-3', 'windows-1254', 'euc-jp] 


# use groupby:
#   'encoding & language'
#   'ballpark & language'
#   'encoding'
#   'ballpark'
#   'language'
#   'neither'


# NOTE: 
#   domain is the generated & encoded text
#   algorithm is the chardet addition
#   have to add result = chardet.detect(case)

def is_encoding(case) -> bool:
    """Actual encoding does not match detected encoding"""

    if detected['encoding'] is None: return False
    return case.encoding.lower() == detected['encoding'].lower()           

def is_language(case) -> bool:
    """Actual langauge does not match detected langauge"""

    if detected['language'] is None: return False

    return case.name.lower() == detected['language'].lower() or \
           detected['language'].lower() in case.name.lower()

def confidence_high(case) -> bool:
    """Confidence is not above 70 percent"""
    return detected['confidence'] >= 0.70

def ballpark(case) -> bool:
    """The actual encoding similiar to, but not, the detected encoding"""

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

def neither(case) -> bool:

    # finds neither the encoding or language
    return detected['encoding'] is None and detected['language'] is None


# --------------------------------

samples = get_samples(f_sample)

for case in generate_encodings(samples):

    detected = chardet.detect(case.encoded)
    # detected_all = chardet.detect_all(case.encoded)

    print(case.name, case.encoding, ' --> ', detected['encoding'], detected['language'], detected['confidence'])

    print('encoding: ', is_encoding(case))
    print('language: ', is_language(case))
    print('high confidence: ', confidence_high(case))
    print('ballpark: ', ballpark(case))
    print('neither:  ', neither(case))
    print()

print()

contains = 'iso-8850-1' in aliases['windows-1252']

print(contains, aliases['iso-8859-15'], aliases['iso-8859-1'])