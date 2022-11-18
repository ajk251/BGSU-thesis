
from distutils.log import error
from itertools import product
from random import choices
from re import sub

import iconv


FILE = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-iconv/iconv-encodings.txt'

def get_encodings():

    with open(FILE, 'r') as file:

        data = file.read().split(',')
        
        encodings = tuple(e.strip('\n').lstrip().rstrip() for e in data)

    return encodings

# -----------------------------------------------

def sample_file_encodings(n=15):

    encodings = get_encodings()

    subset = choices(encodings, k=n)

    for i, j in product(subset, repeat=2):
        
        if i != j:
            yield i, j


def file_encodings():

    encodings = get_encodings()

    for i,j in product(encodings, repeat=2):

        if i != j: 
            yield i,j


def iconv_wrapper(source, dest):

    try: 
        result = iconv.open(source, dest)
    except Exception as error:
        result = error

    return result, source, dest #, bytes_object

# -----------------------------------------------

def converts(encoding) -> bool:

    try: 
        outcome = encoding.iconv()
    except Exception as error:
        result = error
        return False

    return True


# source & destination

def is_lookup_error(encoding) -> bool:
    # did not recognize the encoding
    return isinstance(encoding, LookupError)


def is_iconv_error(encoding) -> bool:
    return isinstance(encoding, iconv.error)


def matches(iconv_text, text_bytes) -> bool:
    return iconv_text == text_bytes


def length(iconv_text, text_bytes) -> bool:
    return len(iconv_text) == len(text_bytes)


# iconv errors *******************

# 'encoding without a string argument'
# 'Argument list too long'
# 'Invalid or incomplete multibyte or wide character'

# -----------------------------------------------

utfs = ('utf-8', 'utf-16', 'utf-32', 'utf-32be', 'utf-32le')
us_text = 'the quick brown fox jumps over the lazy dog'

for i,j in sample_file_encodings():

    continue

print(' - ' * 25)

for i,j in sample_file_encodings():

    # ftext = tuple(str(int(str(n), base=16)) for n in range(0, 256))
    # ftext = ''.join(ftext).encode(i, errors='ignore')

    # if converts(i, j):
    #     print(i, j)
    # else: 
    #     print('no ', i, j)

    try:
        s = iconv.open(i, j)
    except Exception as error:
        # print('conversion exception')
        continue
    
    try:
        # r = s.iconv(b'Hello world')
        text = bytearray(us_text, encoding=i, errors='ignore')
        r = s.iconv(text)
    except LookupError as error:
        print('lookup failed', i, j)
        continue
    except Exception as error:
        print('conversion failed ', i, j, error.args)
        continue

    print('matches: ', r == text, '  length:  ', len(r) == len(text))
    print('worked… ', i, j, r)


# arabic = 'iso-8859-6'
# turkish = 'iso-8859-9'

# numbers = bytearray(range(32, 126), encoding='ISO-8859-6')

# i = iconv.open('ISO-8859-6', 'utf-8')

# text = bytearray(numbers, encoding='ISO-8859-6', errors='ignore')
# result = i.iconv(numbers)
# print(text)
# result = i.iconv(text)
# print(result)


# import re
# import codecs
# import unicodedata

# i = iconv.open('ISO-8859-6', 'utf-8')
# numbers = bytearray(range(32, 127))                             #printable range
# text = str(numbers, encoding='iso-8859-6', errors='ignore')

# bytes(numbers)

# print(i.iconv(bytes(numbers)))

# print(text)

# print('-' * 25)

# rehex = r'\\x[0-9abcdef][0-9abcdef]'

# i = iconv.open('ISO-8859-6', 'utf-8')

# numbers = bytearray(range(0, 256))
# text = str(numbers, encoding='iso-8859-6', errors='ignore')
# btext = text.encode('utf-8')
# btext = btext.decode('iso-8859-6', errors='ignore')
# btext = bytes(btext, encoding='iso-8859-6')

# btext = bytearray(text, encoding='iso-8859-6', errors='ignore')
# print(len(text), text)

# c = codecs.encode(text, encoding='iso-8859-6', errors='ignore')

# print(bytes(numbers))
# t = str(bytes(numbers))

# print(i.iconv(btext))



# print(t)
# text_ = bytes(re.sub(rehex, '', t), encoding='iso-8859-6')

# print(text_)

# print(i.iconv(text))

# import codecs

# print(codecs.encode(text, encoding='iso-8859-6'))

# a = bytearray([int('e1', base=16), int('e2', base=16), int('e3', base=16)])
# print('--> ', str(a, encoding='iso-8859-6', errors='strict'))


# arabic  = 'iso-8859-6'
# turkish = 'iso-8859-9'

# numbers = bytearray(range(0, 256))
# valid_points = []

# for n in range(256):

#     try:
#         str(bytearray([n]), encoding=arabic, errors='strict')
#         valid_points.append(n)
#     except:
#         continue

# text = str(bytearray(valid_points), encoding=arabic, errors='strict')

# print('text: ', text)

# i.iconv(bytearray(bytearray(valid_points)))