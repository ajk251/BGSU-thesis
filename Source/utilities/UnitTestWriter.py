
import re
import textwrap

from collections import defaultdict
from datetime import datetime
from random import choices, randint
from string import ascii_letters, digits
# from time import strftime
from textwrap import indent

import predicates
from predicates.predicates import PREDICATES
from algorithms.algorithms import ALGORITHMS
import domains

# TODO:
#   add overwrite directive
#   add imports
#   warning for unrecognized directives
#   add falcon notes?

#   a new file for every unit test...? or directive for it?

tabsize = 4
TAB = ' ' * tabsize
nl = '\n'

# ⊻ ⊼ ⊽
booleans = {'∧': 'and', '&&': 'and', 'and': 'and',
            '∨': 'or', '||': 'or', 'or': 'or',
            '!': 'not', '¬': 'not', 'not': 'not'}

# writes the file -----------------------------------------

def write_basic_unittest(intermediate, source=None):

    # print('Predicates avaliable: ', len(p.PREDICATES))

    indent = 0
    nl = '\n'

    # file = intermediate['global']['directives'].setdefault('file', './test.py')
    file = 'Tests/tests.py' if 'file' not in intermediate['global']['directives'] else intermediate['global']['directives']['file']

    with open(file, 'w', encoding='utf-8') as falcon:

        # write the boilerplate stuff, that applies globally
        lines = make_initial(intermediate['initial'], source)
        falcon.write(lines)

        lines = make_global(intermediate['global'])
        falcon.write(lines)

        for block in intermediate['ordering']:

            kind, value = block

            if kind == 'code':
                line = code_block(value)
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

    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        if kind == 'code':
            line = code_block(value)
            lines.append(line)
        elif kind == 'assertion':
            line = basic_Assert(entry['tests'][value])
            lines.append(line)
        elif kind == 'domain':
            line = make_domain(value, indent)
            lines.append(line)
        elif kind == 'test':
            if entry['tests'][value]['kind'] == 'test-basic':
                line = basic_Test(entry['tests'][value], indent)
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'winnow-test':
                line = basic_Winnow(entry['tests'][value], indent)
                lines.append(line)

    return '\n'.join(lines)


# boilerplate ----------
def add_imports(entry) -> str:

    lines = ['from predicates import *',
             'from domains import *\n',
             'from algorithms import *',
             'import unittest\n']

    for module, args in entry:

        line = ''

        if len(args) == 0:
            line = 'import ' + module
        elif 'from' in args and 'as' in args:
            line = 'from {} import {} as {}'.format(module, args['from'], args['as'])
        elif 'from' in args:
            line = 'from {} import {}'.format(module, args['from'])
        elif 'as' in args:
            line = 'import {} as {}'.format(module, args['as'])

        lines.append(line)

    return '\n'.join(lines)


def falcon_intro(source=None):

    intro = "# This file was generated automatically by falcon."
    intro += '' if not source else '\n# from: ' + source
    intro += '\n# on ' + datetime.now().strftime("%Y %b %d %a %H:%M:%S") + nl + nl

    return intro


# testers --------------
def basic_Test(entry, indent=0) -> str:

    # print('directives: ', entry)

    #directives --------

    # *** message ***

    if entry['directives'].get(':message', None) is not None:
        message = entry['directives'][':message']['value']
    else:
        message = None

    # *** get function name ***
    # this is mostly for use with pytest
    fn_name = entry['function']

    if entry['directives'].get(':test-name', None):
        # TODO: raise warning if it does not start with test
        t_name = entry['directives'][':test-name']['value']
        pyfunc = f'def {t_name}():'
    elif entry['directives'].get(':name', None):
        t_name = entry['directives'][':name']['value']
        pyfunc = f'def {t_name}():' if t_name.startswith('test') else f'def test_{t_name}():'
    else:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        pyfunc = 'def test_{}_{}():'.format(fn_name, rand_name)

    # *** get algo ***
    params = []

    if entry['directives'].get(':method', None):

        algo = entry['directives'][':method']['value']

        if algo not in ALGORITHMS:
            raise f"Directive :method not found {algo}"

        # get the real name
        algo = ALGORITHMS[algo]

        # deal with the parameters of the test
        # params = []                                         # the parameters of the algorithm
        for name, values in entry['directives'][':method']['params']:
            params.append('{}={}'.format(name, ''.join(values)))
    else:
        algo = 'zip'
        params = []

    # write tests ------

    lines = ['\n# start test -----------------', pyfunc, '']
    indent += 1

    if message:
        line = indent * TAB + '# ' + message.strip('"') + nl
        lines.append(line)

    # get the variable names
    dvars = entry['domain']                                 # the domain names
    ivars = [d.lower() + 'ᵢ' for d in dvars]                # the name of the values in the domain

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(ivars) == 1:
        template = indent * TAB + "for {} in {}:".format(ivars[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(ivars), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(ivars), algo, ', '.join(dvars))

    lines.append(template)

    # fn_name = entry['function']
    args = ', '.join(ivars)
    fn_sig = '{}({})'.format(fn_name, args)
    indent += 1

    for stub in entry['stubs']:
        stmt = make_assert_stmt(stub, fn_sig, indent)
        lines.append( (indent * TAB) + stmt)

    lines.append('')

    indent -= 1

    return '\n'.join(lines)


def basic_Assert(entry, indent=0) -> str:

    # TODO:
    #   add directive for value = … \ assert predicate(value, args)...
    #   handle messages, ie assert …, <message>
    #   extra args!!! raise error!

    # directives -------------
    ignore_true = True if entry['directives'].get(':ignore-True', 'no').lower() in ['yes', 'true'] else False
    message = entry['directives'].get(':message', None)

    # -----------------------
    a1 = 'assert {} {} {}'              # w/ symbol
    a2 = 'assert {}({}, {})'            # w/ function
    a3 = 'assert {}({})'                # ignoring True

    # -----------------------
    lines = ['# Assertion test -------------']

    if message:
        lines.append('# ' + message.strip('"'))

    fn_name = entry['function']

    for stub in entry['stubs']:

        # if not stub['argument']['kind'] == 'assertion': raise "WTF"

        args = make_args(stub['argument'])
        fn = fn_name + args
        value = stub['value']

        if PREDICATES[stub['predicate']][1]:
            pd_name = PREDICATES[stub['predicate']][1]
            line = a1.format(fn, pd_name, value)
        else:
            pd_name = PREDICATES[stub['predicate']][0]

            if ignore_true and value == 'True':
                line = a3.format(pd_name, fn)
            else:
                line = a2.format(pd_name, fn, value)

        lines.append(line)

    return '\n'.join(lines)


def basic_Winnow(entry, indent=0) -> str:

    lines = []

    # build the function name & vars
    fn_name = entry['function']

    # def name
    lines.extend((f'def group_test_{fn_name}():', ''))

    # if something goes wrong with the 1st…

    # w1 has a separate bin function defined
    w1 = '''
try:
    result = {}
except Exception as e:
    group = 'Unspecified function error'
    result = e
                
try:
    group = {}(result)
except Exception as e_bin:
    group = 'Unspecified binning error'
    result = e_bin     
    '''

    w2 = '''
try:
    result = {}
    group = result
except Exception as e:
    group = 'Unspecified function error'
    result = e    
'''
    # get the variable names
    dvars = entry['domain']                                 # the domain names
    ivars = [d.lower() + 'ᵢ' for d in dvars]                # the name of the values in the domain
    args = ', '.join(ivars)
    fn_sig = '{}({})'.format(fn_name, args)

    # *** get algo ***
    params = []

    if entry['directives'].get(':method', None):

        algo = entry['directives'][':method']['value']

        if algo not in ALGORITHMS:
            raise f"Directive :method not found {algo}"

        # get the real name
        algo = ALGORITHMS[algo]

        # deal with the parameters of the test
        # params = []                                         # the parameters of the algorithm
        for name, values in entry['directives'][':method']['params']:
            params.append('{}={}'.format(name, ''.join(values)))
    else:
        algo = 'zip'
        params = []

    indent += 1

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(ivars) == 1:
        template = indent * TAB + "for {} in {}:".format(ivars[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(ivars), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(ivars), algo, ', '.join(dvars))

    lines.append(template)

    # build the template
    if entry['bin'] is not None:
        line = textwrap.indent(w1.format(fn_sig, entry['bin']), TAB * 2)
        lines.append(line)
    else:
        line = textwrap.indent(w2.format(fn_sig), TAB * 2)
        lines.append(line)

    # deal with the groups
    groups = defaultdict(list)

    for stub in entry['stubs']:
        stmt = make_assert_stmt(stub, 'result', indent)
        groups[stub['group']].append(stmt)

    assert len(groups) > 1, "the number of groups must be greater than 1"

    first = entry['group-predicates'][0][0]

    # TODO: if there are multiple statements, this will fail.

    indent += 1

    for group, stmts in groups.items():

        if group == first:
            line = (indent * TAB) + f'if group is {group}:\n' + ((indent + 1) * TAB) + '\n'.join(stmts)
        else:
            line = (indent * TAB) + f'elif group is {group}:\n' + ((indent + 1) * TAB) + '\n'.join(stmts)

        lines.append(line)

    # add failure case
    failure = (indent * TAB) + f'else:\n' + ((indent + 1) * TAB) + 'print("You shouldn\'t be here!") # TODO…'
    lines.append(failure)

    lines.append('')

    return '\n'.join(lines)

# component parts -------
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


def code_block(entry) -> str:
    code = entry.strip('`')
    return code


def make_domains(entry, indent=0) -> str:

    # TODO: if name fails raise error
    #       add :annotate to add/or not "# domains"

    lines = [nl, '# domains -------------------\n']

    f1 = '{} = {}()'              # x = Reals()
    f2 = '{} = {}({})'            # x = Reals(lb, ub)
    f3 = '{} = {}({}, {})'        # x = Reals(lb, ub, nrandom=10)

    print(entry)

    for name, info in entry.items():

        if info['kind'] == 'domain':
            var = info['var-name']
            name = domains.DOMAINS[info['domain']]
            line = f1.format(var, name)
        elif info['kind'] == 'domain-args':

            var = info['var-name']
            name = domains.DOMAINS[info['domain']]

            args = ', '.join(info['args']) if info['args'] else ''

            if info['kwargs']:
                for k, v in info['kwargs'].items():
                    args += ', '
                    args += k.strip('-') + '='
                    args += v

            line = f2.format(var, name, args)

        lines.append(line)
        # lines.append(nl)
        text = '\n'.join(lines) + nl + nl

    return text


def make_domain(entry, indent=0) -> str:

    # TODO: if name fails raise error
    #       add :annotate to add/or not "# domains"

    f1 = '{} = {}()'              # x = Reals()
    f2 = '{} = {}({})'            # x = Reals(lb, ub)
    f3 = '{} = {}({}, {})'        # x = Reals(lb, ub, nrandom=10)

    # print(entry)

    if entry['kind'] == 'domain':
        var = entry['var-name']
        name = domains.DOMAINS[entry['domain']]
        line = f1.format(var, name)
    elif entry['kind'] == 'domain-args':

        var = entry['var-name']
        name = domains.DOMAINS[entry['domain']]

        args = ', '.join(entry['args']) if entry['args'] else ''

        if entry['kwargs']:
            for k,v in entry['kwargs'].items():
                args += ', '
                args += k.strip('-') + '='
                args += v

        line = f2.format(var, name, args)

    return line


def make_boolean(entry, fn_sig='', indent=0) -> str:

    case = []
    line = []

    for element in entry['values']:

        if element in ('!', '¬', 'not'): case.append('not ')
        elif element in booleans: case.append(' ' + booleans[element] + ' ')
        elif element in PREDICATES: case.append(PREDICATES[element])
        elif isinstance(element, tuple): case[-1] += element                # ++ to the previous tuple
        else: case.append(element)

    f1 = '{} {} {}'            # fn < 10
    f2 = '{}({})'              # pd(fn(…))
    f3 = '{}({}, {})'          # pd(fn(…), args)

    for element in case:

        if isinstance(element, tuple):

            predicate = element[0]
            use_symbolic = element[1]
            args = element[2:] if len(element) > 2 else None

            if use_symbolic:
                line.append(f1.format(fn_sig, use_symbolic, ''.join(args)))
            elif args is None:
                line.append(f2.format(predicate, fn_sig))
            else:
                line.append(f3.format(predicate, fn_sig, ', '.join(args)))
        else:
            line.append(element)

    return ''.join(line)


def make_assert_stmt(stub, fn_sig, indent=0):

    f1 = 'assert {} {} {}'              # w/ symbol
    f2 = 'assert {}({}, {})'            # pd( fn(arg), value)
    f3 = 'assert {}({}, {})'            # w/ function
    f4 = 'assert {}({})'                # ignoring True

    # fn_name = entry['function']
    # args = ', '.join(ivars)
    # fn_sig = '{}({})'.format(fn_name, args)
    indent += 1
    line = ''

    # get the name of the predicate if it knows it's a predicate (or should be, ie OOPS)
    if stub['kind'].startswith('predicate') and stub['predicate'] in PREDICATES:
        # get the symbolic name if there is one, otherwise the function name

        if PREDICATES[stub['predicate']][1]:
            pd_name = PREDICATES[stub['predicate']][1]
            use_symbolic = True
        else:
            pd_name = PREDICATES[stub['predicate']][0]
            use_symbolic = False
    elif stub['kind'].startswith('predicate'):
        pd_name = stub['predicate']
        use_symbolic = False
    else:
        # raise error
        pd_name = "OOPS!"
    #
    # # write the predicate
    # if stub['kind'] == 'predicate-value':
    #     # raises is a special case
    #     if pd_name == 'raises':
    #         line = TAB * indent + f'assert {pd_name}({fn_name}, {args}, {stub["value"]})'
    #     elif use_symbolic and stub['value'] == 'True':
    #         line = TAB * indent + f4.format(pd_name, fn_sig)
    #     elif use_symbolic:
    #         line = TAB * indent + f1.format(fn_sig, pd_name, stub['value'])
    #     else:
    #         line = TAB * indent + f2.format(pd_name, fn_sig, stub['value'])
    # elif stub['kind'] == 'predicate':
    #     line = indent * TAB + f4.format(pd_name, fn_sig)
    # elif stub['kind'] == 'predicate-value+':
    #     line = TAB * indent + f2.format(pd_name, fn_sig, ', '.join(stub['value']))
    # elif stub['kind'] == 'predicate-values':
    #     # this is redundant and should be predicate-value+, it is for the groupby
    #     line = TAB * indent + f2.format(pd_name, fn_sig, ', '.join(stub['values']))
    # elif stub['kind'] == 'logical':
    #     line = TAB * indent + 'assert ' + make_boolean(stub['values'], fn_sig, indent)
    # elif stub['kind'] == 'code':
    #     line = (TAB * indent) + stub['value']
    # elif stub['kind'] == 'predicate-side-effect':
    #     line = TAB * indent + f4.format(pd_name, stub['name'])
    # elif stub['kind'] == 'predicate-side-effect+':
    #     args = ', '.join(stub['values'])
    #     line = TAB * indent + f3.format(pd_name, stub['name'], args)
    # else:
    #     print('Test writer -- forgot about --> ', stub)

    if stub['kind'] == 'predicate-value':
        # raises is a special case
        if pd_name == 'raises':
            line = f'assert {pd_name}({fn_name}, {args}, {stub["value"]})'
        elif use_symbolic and stub['value'] == 'True':
            line = f4.format(pd_name, fn_sig)
        elif use_symbolic:
            line = f1.format(fn_sig, pd_name, stub['value'])
        else:
            line = f2.format(pd_name, fn_sig, stub['value'])
    elif stub['kind'] == 'predicate':
        line = f4.format(pd_name, fn_sig)
    elif stub['kind'] == 'predicate-value+':
        line = f2.format(pd_name, fn_sig, ', '.join(stub['value']))
    elif stub['kind'] == 'predicate-values':
        # this is redundant and should be predicate-value+, it is for the groupby
        line = f2.format(pd_name, fn_sig, ', '.join(stub['values']))
    elif stub['kind'] == 'logical':
        line = 'assert ' + make_boolean(stub['values'], fn_sig, indent)
    elif stub['kind'] == 'code':
        line = stub['value']
    elif stub['kind'] == 'predicate-side-effect':
        line = f4.format(pd_name, stub['name'])
    elif stub['kind'] == 'predicate-side-effect+':
        args = ', '.join(stub['values'])
        line = f3.format(pd_name, stub['name'], args)
    else:
        print('Test writer -- forgot about --> ', stub)

    return line
