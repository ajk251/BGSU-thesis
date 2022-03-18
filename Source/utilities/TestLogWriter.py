

import json


def write_to_log(file_path, values, json_encoder=None):
    """Writes a dict to a file."""

    print('values: ', values)

    with open(file_path, 'a', encoding='utf-8') as file:

        if json_encoder is None:
            file.write(json.dumps(values) + '\n')
        else:
            file.write(json.dumps(values) + '\n', cls=json_encoder)

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

d  = {'name': 'some-func', 'a': 1, 'b': 2, 'c': 3}
d1 = {'name': 'some-func2', 'a': 1, 'c': 3, 'rt': 0}
d2 = {'name': 'test', 'z': [('a', 'b', 'c'), ('d', 'e', 'f')]}

write_to_log(f, d)
write_to_log(f, d1)
write_to_log(f, d2)

print(load_from_log(f))
