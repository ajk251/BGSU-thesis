

import json


def write_to_log(file_path, values):
    """Writes a dict to a file."""

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(json.dumps(values) + '\n')


def load_from_log(file_path):
    """Loads dicts made from 'write_to_log' (using json.dumps) into a list."""

    lines = []

    with open(file_path, 'r') as file:
        
        for line in file.readlines():
            lines.append(dict(json.loads(line)))

    return lines


# ---------------------------------------------------------

def issubset(a, b):

    a_ = set(a)
    b_ = set(b)

    return a_.issubset(b_)


def issuperset(a, b):

    a_ = set(a)
    b_ = set(b)

    return a_.issuperset(b_)


def isdisjoint(a, b):

    a_ = set(a)
    b_ = set(b)

    return a_.isdisjoint(b_)


def similarity(a, b):
    """Returns the Jaccard similarity between two dicts, sets, or sequences. |a ∪ b| / |a ∩ b|"""

    if isinstance(a, dict) and isinstance(b, dict):
        return len(a.keys() & b.keys()) / len(a.keys() | b.keys())
    elif isinstance(a, set) and isinstance(b, set):
        return len(a & b) / len(a | b)
    
    a_ = set(a)
    b_ = set(b)

    return len(a_ & b_) / len(a_ | b_)


def distance(a, b):
    """Returns the Jaccard dis-similiarity or distance between two dicts, sets, or sequences. 1.0 - |a ∪ b| / |a ∩ b|"""

    return 1.0 - similarity(a, b)


# ---------------------------------------------------------

f = './test-file.csv'

# info ￫ name, date, domains?, & meta-data
#      ￫ kind, the result kind: count or values

# show count of overlaps

from string import ascii_uppercase
from string import ascii_lowercase
from random import choice, randint

r_uc = lambda : choice(['X?', 'Y?', 'Z?', 'Π?', 'Γ?', 'Σ?'])
# r_uc = lambda : choice(ascii_uppercase)
r_lc = lambda : choice(ascii_lowercase)
runi = lambda : randint(1, 5)

d = {'info': {'name': 'some-func'}, 'oracles': {}}
d1 = {'info': {'name': 'some-func2'}, 'oracles': {}}
d2 = {'info': {'name': 'some-test-func1'}, 'oracles': {}}

# write_to_log(f, d)
# write_to_log(f, d1)
# write_to_log(f, d2)

logs = load_from_log(f)

print('distance:\t', distance(logs[0]['oracles'], logs[0]['oracles']))
print('distance:\t', distance(logs[0]['oracles'], logs[1]['oracles']))

print('similiarity:\t', similarity(logs[0]['oracles'], logs[0]['oracles']))
print('similiarity:\t', similarity(logs[0]['oracles'], logs[1]['oracles']))

print('⊆:\t\t', issubset(logs[0]['oracles'], logs[0]['oracles']))
print('⊆:\t\t', issubset(logs[0]['oracles'], logs[1]['oracles']))