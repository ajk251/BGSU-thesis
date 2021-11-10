
from datetime import datetime, date
import re
from time import strftime

import predicates.predicates #as predicates
import predicates.numerical

# TODO:
#   add overwrite directive
#   add imports
#   warning for unrecognized directives
#   add falcon notes?

#   a new file for every unit test...? or directive for it?

tabsize = 4
TAB = ' ' * tabsize
nl = '\n'


# writes the file -----------------------------------------

def write_basic_unittest(intermediate, source=None):

    # print('Predicates avaliable: ', len(p.PREDICATES))

    indent = 0
    nl = '\n'

    file = intermediate['global']['directives'].setdefault('file', './test.py')

    with open(file, 'w', encoding='utf-8') as falcon:

        # write the boilerplate stuff, that applies globally
        lines = make_initial(intermediate['initial'], source)
        falcon.write(lines)

        lines = make_global(intermediate['global'])
        falcon.write(lines)

        for block in intermediate['ordering']:

            kind, value = block

            if kind == 'code':
                line = write_code(value)
                falcon.write(line)
            elif kind == 'namespace':
                lines = make_namespace(intermediate[value], value)
                falcon.write(lines)

            falcon.write(nl)

        # finally!
        falcon.write('')


# utils ---------------------------------------------------


def clean(name):
    # from here: https://stackoverflow.com/questions/3303312/how-do-i-convert-a-string-to-a-valid-variable-name-in-python
    text = re.sub('\W|^(?=\d)','_', name)
    return text.title()


# component writers ---------------------------------------
#   ie build the strings to be written

# note → these should only write exactly what they are supposed to, no more no less

def make_initial(entry, source=None) -> str:

    lines = []

    lines.append(add_imports(entry['imports']))              # always 1+
    lines.append('')                                        # blank
    lines.append(falcon_intro(source))         # hello!

    return '\n'.join(lines)


# make chunks ----------
def make_namespace(entry, name, indent=0) -> str:

    # if no tests, just 'pass'

    indent = indent if indent else 0

    # -----------------------
    # directive - language safe name
    clean_name = entry['directives'][':name'] if entry['directives'].get(':name', None) else clean(name)
    desc = entry['directives'].get(':desc', None)

    # -----------------------
    # set directives
    lines = ['\n\nclass {}(unittest.TestCase):\n'.format(clean_name)]           # add unittest class

    # limit length & wrap?
    if desc:
        indent += 1
        lines.append(indent * TAB + '# ' + desc)

    class_vars = []                                                           # holds any class-level variables

    # -----------------------
    # then all the other stuff
    for entry in entry['ordering']:

        kind, value = entry if len(entry) == 2 else (entry[0], entry[1:])

        # if kind == 'code': continue
        print(kind, value)

        # print(entry)

    print('-' * 20)

    return '\n'.join(lines)


def make_global(entry, indent=0) -> str:

    lines = []

    # directives -----
    desc = entry['directives'].get(':desc', None)

    if desc:
        lines.append(indent * TAB + '# ' + desc)

    # ----------------
    print('\nglobals: ')

    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])
        print(kind, value)

        if kind == 'code':
            line = code_block(value)
            lines.append(line)
        elif kind == 'assertion':
            line = basic_Assert(entry['tests'][value])
            lines.append(line)
        elif kind == 'test':
            continue


    return '\n'.join(lines)


def make_namespace(entry, name, indent=0) -> str:

    # if no tests, just 'pass'

    indent = indent if indent else 0

    # -----------------------
    # directive - language safe name
    clean_name = entry['directives'][':name'] if entry['directives'].get(':name', None) else clean(name)
    desc = entry['directives'].get(':desc', None)

    # -----------------------
    # set directives
    lines = ['\n\nclass {}(unittest.TestCase):\n'.format(clean_name)]           # add unittest class

    # limit length & wrap?
    if desc:
        indent += 1
        lines.append(indent * TAB + '# ' + desc)

    class_vars = []                                                           # holds any class-level variables

    # -----------------------
    print('\nnamespace', clean_name, ':')

    # then all the other stuff
    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        # if kind == 'code': continue
        print(kind, value)

        # print(entry)

    print('-' * 20)

    return '\n'.join(lines)


# boilerplate ----------
def add_imports(entry) -> str:

    lines = ['import unittest']

    # do other imports...

    return '\n'.join(lines)


def falcon_intro(source=None):

    intro = "# This file was generated automatically by falcon."
    intro += '' if not source else '\n# from: ' + source
    intro += '\n# on ' + datetime.now().strftime("%Y %b %d %a %H:%M:%S") + '\n\n'

    return intro


def write_code(entry) -> str:

    # writes a block of code
    entry = entry.strip('`')
    return entry


def basic_Test(entry) -> str:

    pass


def basic_Assert(entry, indent=0) -> str:

    lines = ['\n# Assertion test -------------']

    fn_name = entry['function']
    ws = ' '

    for stub in entry['stubs']:

        # if not stub['argument']['kind'] == 'assertion': raise "WTF"

        args = make_args(stub['argument'])
        line = 'assert ' + fn_name + args + ws + stub['predicate'] + ws + stub['value']
        lines.append(line)

        print('predicate', stub['predicate'], predicates.predicates.PREDICATES[stub['predicate']])

    return '\n'.join(lines)


# testers --------------
def assert_predicate_value(entry):
    line = 'assert {} {} {}'
    return line


def make_enumerates(entry) -> str:

    pass


def make_by_loop(entry) -> str:

    pass


def make_args(entry) -> str:

    line = []

    for arg in entry['args']:

        if arg[0] == 'value':
            line.append(arg[1])
        elif arg[0] == 'value-type':
            line.append(arg[1] + ': ' + arg[2])
        elif arg[0] == 'named-value':
            line.append(arg[1] + '=' + arg[2])
        elif arg[0] == 'name-type-value':
            # fn(a, b:int= 3):
            line.append(arg[1] + ':' + arg[2] + ' = ' + arg[3])

    return '(' + ', '.join(line) + ')'


# component parts -------
def code_block(entry) -> str:
    code = entry.strip('`')
    return code
