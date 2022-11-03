

from itertools import product
from random import choice, choices
from os import path

import codecs
import subprocess

import iconv

from Falcon.domains import domain
from Falcon.predicates import predicate


FILE = '/media/aaron/Shared2/School/BGSU-thesis/code-comparisons/example-iconv/iconv-encodings.txt'
# FOLDER = '~/Desktop/encodings/'
FOLDER = '/home/aaron/Desktop/encodings/'


def get_encodings():

    with open(FILE, 'r') as file:

        data = file.read().split(',')
        encodings = tuple(e.strip('\n').lstrip().rstrip() for e in data)

    return encodings


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

# domains -------------------------------------------------

@domain(alias=['EncodingCases'])
def generate_cases(n=10):

    encodings_ = get_encodings()

    # get n pairs of encodings/otherwise all pairs
    if n is not None:
        encodings = tuple((choice(encodings_), choice(encodings_)) for _ in range(n))
    else:
        encodings = product(encodings_, encodings_)

    # test file
    N = list(range(256))
    with open(FOLDER + 'full-bytes.bin', 'wb') as file:
        file.write(bytearray(N))

    for source, dest in encodings:
        
        if source == dest: continue

        valid_128 = []
        valid_256 = []

        case = {'source': source, 'dest': dest, 'filename':None, '128': valid_128,
                '256': valid_256, 'exception': None}

        # do the encodings even load?
        try:
            i = iconv.open(source, dest)
        except Exception as error:
            case['exception'] = error.args
            # continue                                    # NO!!!! 
            yield case

        # for what code points does it work?
        for n in range(128):
            try:
                i.iconv(bytearray([n]))
                valid_128.append(n)
            except Exception as error:
                continue

        for n in range(128, 256):
            try:
                i.iconv(bytearray([n]))
                valid_256.append(n)
            except Exception as error:
                continue

        points = valid_128 + valid_256

        # this is the source￫dest encoding
        name = f'encoding_{source}--{dest}.bin'
        name = FOLDER + name.replace(':', '~').replace('/', '-')

        with open(name, 'wb') as file:
            file.write(bytearray(points))

        case['filename'] = name
    
        yield case


@domain(alias=['PyEncodingCases'])
def generate_pycases(n=10):

    encodings_ = get_encodings()
    encodings = []

    # reject the ones python won't recognize
    for encoding in encodings_:

        try:
            codecs.lookup(encoding)               # raises a lookup error if not found
        except LookupError as _:
            continue

        encodings.append(encoding)

    # get n pairs of encodings/otherwise all pairs
    if n is not None:
        encodings = tuple((choice(encodings), choice(encodings)) for _ in range(n))
    else:
        encodings = product(encodings, encodings)

    sources = {}

    for source, dest in encodings:

        # source encoding as bytes
        if source in sources:
            points = sources[source]
        else:
            points = []
            # build all valid bytes
            for n in range(256):
                try:
                    str(bytearray([n]), encoding=source, errors='strict')   # any of these could cause an exception
                    c = codecs.lookup(source)
                    c.decode(bytearray([n]), errors='strict')
                    points.append(n)
                except Exception as error:
                    continue
            
            sources[source] = points

        if len(points) == 0:                # ie, a string cannot be made
            continue

        yield {'source': source, 'dest': dest, 'points': points}

# sut -----------------------------------------------------

def identity_iconv(case):

    # does it load
    # write all possible chars to file
    # what percentage of 128 & 256 does it load

    case['%-128'] = len(case['128']) / 128.
    case['%-256'] = len(case['256']) / 128.
    case['%-all'] = (len(case['128']) + len(case['256'])) / 256.

    return case
    

def iconv_sut_py(case): 
    yield case

# PREDICATES ----------------------------------------------

# these are for iconv only ------------
# does iconv commandline work?
#   write all chars in source, try to convert to dest --> No! in reverse!
# does it load?
# does it handle most characters?

@predicate(alias=['loads-iconv?'])
def does_load(case) -> bool:
    return case['exception'] is None


@predicate(alias=['has-valid-points?'])
def valid_points(case) -> bool:
    # are there any valid codepoints?
    return len(case['128']) > 0 or len(case['256']) > 0


@predicate(alias=['most-128?', 'has-most-128?'])
def most_128(case, threshold=0.51) -> bool:
    return case['%-128'] >= threshold


@predicate(alias=['most-256?', 'has-most-256?'])
def most_256(case, threshold=0.51) -> bool:
    return case['%-256'] >= threshold


@predicate(alias=['most-all?'])
def most(case, threshold=0.51) -> bool:
    return case['%-all'] >= threshold


@predicate(alias=['matches-iconv?'])
def like_iconv(case) -> bool:

    # test that the py-iconv ≡ reverse iconv

    # this is iconv command line command
    cmd = f"iconv -f {case['dest']} -t {case['source']} -o {FOLDER}temp.bin {case['filename']}"

    # print(' --> ', cmd)
    temp = FOLDER + 'temp.bin'

    try:
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
        out, err = proc.communicate()
    except:
        print('--> ', out, err, case['exception'])

    if err is not None: return False

    # check the files
    # print(path.samefile(case['filename'], FOLDER + 'temp.bin'))
    sizes = path.getsize(case['filename']) == path.getsize(FOLDER + 'temp.bin')

    if sizes:
        with open(case['filename'], 'rb') as a, open(temp, 'rb') as b:
           diff = a.read() != b.read()

    return sizes and diff


# these use python encodings ----------

@predicate(alias=['py-loads-iconv?'])
def loads_in_iconv(case) -> bool:
    # does it even load in iconv?

    try:
        i = iconv.open(case['source'], case['dest'])
    except Exception as error:
        return False

    return True


@predicate(alias=['valid-iconv?'])
def converts_in_iconv(case) -> bool:
    # does it produce a valid array of bytes?

    try:
        i = iconv.open(case['source'], case['dest'])
        i.iconv(bytearray(case['points']))
    except Exception as error:
        return False

    return True


@predicate(alias=['codepoints-match?'])
def matchs_python_codec(case) -> bool:
    # do the bytes match byte for byte in python-iconv

    # load iconv
    try:
        i = iconv.open(case['source'], case['dest'])
    except Exception as error:
        return False

    # test points
    for n in case['points']:

        try:
            i.iconv(bytearray([n]))
        except:
            return False

    return True


@predicate(alias=['matches-py-iconv?'])
def matches_iconv(case) -> bool:
    # does the cmdln iconv ≡ iconv

    # load the bytes in pyconv
    try:
        i = iconv.open(case['source'], case['dest'])
        i.iconv(bytearray(case['points']))
    except Exception as error:
        # print('doesnt load or cant cast')
        return False

    # write the file
    name = f"python_{case['source']}--{case['dest']}.bin"
    name = FOLDER + name.replace(':', '~').replace('/', '-')

    with open(name, 'wb') as file:
        file.write(bytearray(case['points']))

    # test with cmdln iconv
    cmd = f"iconv -f {case['source']} -t {case['dest']} -o {FOLDER}temp2.bin {name}"

    # the pyconv file
    temp = FOLDER + 'temp2.bin'

    try:
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
        out, err = proc.communicate()
    except:
        # print('--> ', out, err, case['exception'])    # iconv had an error
        return False
    
    if err is not None: return False                    # iconv had an error

    # check the files
    sizes = path.getsize(name) == path.getsize(FOLDER + 'temp2.bin')
    # print(path.getsize(name), path.getsize(FOLDER + 'temp2.bin'))

    # if the sizes are the same, check the contents
    if sizes:
        with open(name, 'rb') as a, open(temp, 'rb') as b:
            af = a.read()
            bf = b.read()
            diff = af == bf

    return sizes and diff
