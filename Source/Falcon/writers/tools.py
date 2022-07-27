
import re
import runpy
import pathlib
import textwrap
import os
import sys
import warnings

from collections import defaultdict
from datetime import datetime
from random import choices, randint
from string import ascii_letters, digits
from sys import stderr, path
from typing import Union

from Falcon.algorithms.algorithms import ALGORITHMS
from Falcon.macros.macros import MACROS
from Falcon.predicates.predicates import PREDICATES, Predicate
from Falcon.utilities.FalconError import FalconError
from Falcon.domains import DOMAINS

"""
Functions/utility methods that are common to all writers
"""


tabsize: int = 4
TAB: str = ' ' * tabsize
nl: str = '\n'

# ⊻ ⊼ ⊽ ￫ these require special treatment…
booleans = {'∧': 'and', '&&': 'and', 'and': 'and',
            '∨': 'or', '||': 'or', 'or': 'or',
            '!': 'not', '¬': 'not', 'not': 'not'}


def add_pytest_config_file(path: str):

    # as it turns out, this may not be needed

    # a solution based on this
    #   https://stackoverflow.com/questions/49028611/pytest-cannot-find-module

    contents = '[tool.pytest.ini_options]\npythonpath = ["."]\n'

    with open(path, 'w') as file:
        file.write(contents)

# helper funcs ----------------------------------

def clean(name: str) -> str:
    # from here: https://stackoverflow.com/questions/3303312/how-do-i-convert-a-string-to-a-valid-variable-name-in-python
    text = re.sub('\W|^(?=\d)','_', name)
    return text.title()


def to_list(text):

    # because I screwed up

    txt = text.split(',')
    txt[0] = txt[0].strip('[')
    txt[-1] = txt[-1].strip(']')

    values = []

    for value in txt:

        value = value.strip().rstrip('\'').lstrip('\'')
        values.append(value)

    return values


# structure -------------------------------------

def make_initial(entry, source=None) -> str:

    lines = []

    lines.append(add_imports(entry['imports']))             # always 1+
    lines.append('')                                        # blank
    lines.append(falcon_intro(source))                      # hello!

    return '\n'.join(lines)


# boilerplate -----------------------------------

def add_imports(entry) -> str:
    """Add the imports to the generated file"""

    # TODO: Make these prettier

    sys.path.append('.')                # have to add the current directory

    lines = ['from Falcon.algorithms import *',
             'from Falcon.domains import *',
             'from Falcon.macros import *',
             'from Falcon.predicates import *',
             'from Falcon.utilities.utls import call',
             'from Falcon.utilities.TestLogWriter import write_to_log',
             'from Falcon.utilities import FalconError\n',
             'from collections import defaultdict\n',
             'import pytest']

    for module, args in entry:

        line = ''

        # # this is to help with naming issues, like Tests.Module
        # if 'dot' in args or '.' in args:
        #     name = '.' + module
        # elif 'dotdot' in args or '..' in args:
        #     name = '..' + module
        # else:
        #     name = module

        name = module           # TODO: refactor

        # path = pathlib.PurePath(os.getcwd() + f'./{module}.py')
        # print(path.parts, path.parts[-2])

        if len(args) == 0:
            line = 'import ' + name
        elif 'from' in args and 'as' in args:
            line = 'from {} import {} as {}'.format(name, args['from'], args['as'])
        elif 'from' in args and '[' in args['from']:
            s = args['from'].strip('[]').split(',')         # for some reason, this is just a string
            line = 'from {} import {}'.format(name, ','.join(fn for fn in s))
        elif 'all' in args:
            line = 'from {} import *'.format(name)
        elif 'from' in args:
            line = 'from {} import {}'.format(name, args['from'])
        elif 'as' in args:
            line = 'import {} as {}'.format(name, args['as'])

        # has to load the module to get the predicates from predicates.PREDICATES
        try:
            runpy.run_path(f'{name}.py')
        except ImportError as e:
            stderr.write('Could not import module. Check module for exceptions.')
            raise e
        except ModuleNotFoundError as e:
            stderr.write('Could not find module')
            raise e

        lines.append(line)

    return '\n'.join(lines)


def falcon_intro(source=None) -> str:
    """Add a message to the generated file"""

    intro = "# This file was generated automatically by Falcon."
    intro += '' if not source else '\n# from: ' + source
    intro += '\n# on ' + datetime.now().strftime("%Y %b %d %a %H:%M:%S") + nl + nl

    return intro

# component parts -------------------------------


def make_args(entry) -> str:
    """Makes the arguments for a function, <fn>(x,y,z)"""

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
    """Makes a code statement"""
    code = entry.strip('`')
    return code


def make_domain(entry) -> str:
    """Makes the domain in the generated code, ie x = integers(0, 100, 5)"""

    indent: int = 0

    # TODO: if name fails raise error
    #       add :annotate to add/or not "# domains"

    # format templates
    f1 = (indent * TAB) + '{} = {}()'              # x = Reals()
    f2 = (indent * TAB) + '{} = {}({})'            # x = Reals(lb, ub)
    f3 = (indent * TAB) + '{} = {}({}, {})'        # x = Reals(lb, ub, nrandom=10)
                                                   # x = Reals(nrandom=10) ???

    # get the name of the Domain
    if DOMAINS.get(entry['domain'], False):
        name = DOMAINS[entry['domain']]
    else:
        raise FalconError(f"Domain name '{entry['domain']}' not found")

    if entry['kind'] == 'domain':
        var = entry['var-name']
        # name = DOMAINS[entry['domain']]
        line = f1.format(var, name)
    elif entry['kind'] == 'domain-args':
        var = entry['var-name']

        if entry['args']:
            args = ', '.join(entry['args']) if entry['args'] else ''
        else:
            args: str = ''

        if entry['kwargs']:
            for k, v in entry['kwargs'].items():
                args += ', ' if args else ''
                args += k.strip('-') + '='
                args += v

        line = f2.format(var, name, args)

    return line


def get_directives(entry, test_name=None) -> dict[str, Union[None, str, list, bool]]:
    """Extract the directives and put them into a dictionary"""

    # supported:
    #   message, pyfunc, suffix, method (of enumeration),
    #   labels, only (groupby/winnow), algorithm, & algo-params

    # these are implemented
    recognized = frozenset((':follow-up', ':message', ':only', ':test-name', ':name',
                            ':no-suffix', ':suffix', ':labels', ':method', ':log', ':log-name',
                            ':iter-object', ':object-update', ':min', ':max', ':save-results',
                            ':save-cases', ':no-error-message', ':min-cases', ':no-minimum',
                            ':either'))

    # see if any are not recognized
    if not frozenset(entry['directives'].keys()).issubset(recognized):
        warnings.warn(f"Unrecognized directives: {frozenset(entry['directives'].keys()) - recognized}")

    # directives --------
    directives = {}

    # *** follow-up function ***
    if entry['directives'].get(':follow-up', False):
        directives['follow-up'] = entry['directives'][':follow-up']['value']
    else:
        directives['follow-up'] = None

    # *** message ***

    if entry['directives'].get(':message', None) is not None:
        directives['message'] = entry['directives'][':message']['value']
    else:
        directives['message'] = None

    # *** get the only args ***
    if entry['directives'].get(':only', None) is not None:
        directives['only'] = entry['directives'][':only']['value']
    else:
        directives['only'] = None

    # *** get function name ***
    # this is mostly for use with pytest
    fn_name = entry['function']
    directives['fn_name'] = entry['function']

    if entry['directives'].get(':test-name', False):
        # TODO: raise warning if it does not start with test
        t_name = entry['directives'][':test-name']['value'].strip('\'').strip('\"')
        directives['pyfunc'] = f'def {t_name}():'
    elif entry['directives'].get(':name', False):
        t_name = entry['directives'][':name']['value'].strip('\'').strip('\"')
        directives['pyfunc'] = f'def {t_name}():' if t_name.startswith('test') else f'def test_{t_name}():'
    elif test_name:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        fname = 'object' if fn_name == '_' else fn_name
        directives['pyfunc'] = f"def test_{test_name}_{fname}_{rand_name}():"
    else:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        fname = 'object' if fn_name == '_' else fn_name
        directives['pyfunc'] = f"def test_{fname}_{rand_name}():"

    # *** get suffix ***
    # looks for :no-suffix or :suffix <blank> or :suffix '' or :suffix '_i'
    if entry['directives'].get(':no-suffix', False):
        suffix = ''
    elif entry['directives'].get(':suffix', False):
        value = entry['directives'][':suffix']['value']
        suffix = value if (value is not None) else ''
    elif entry['directives'].get(':labels', False):                 # if there are labels, don't bother
        suffix = ''
    else:
        suffix = 'ᵢ'

    # *** get labels, ie, for <labels> in …: ***
    # that is, the labels of the domains used inside the loop

    # get the variable names
    dvars = entry['domain']                                             # the domain names

    if entry['directives'].get(':labels', False):
        # TODO: input must be a list - how to catch bad input?
        lbs = to_list(entry['directives'][':labels']['value'])
        directives['labels'] = [d.lower() + suffix for d in lbs]
    else:
        directives['labels'] = [d.lower() + suffix for d in dvars]      # the name of the values in the domain                                   # the domain names

    # make the labels here
    assert len(directives['labels']) >= 1, 'Must have 1 or more Domains defined'

    if len(directives['labels']) == 1:
        directives['args'] = directives['labels'][0]
    else:
        directives['args'] = ', '.join(directives['labels'])

    # *** get algo ***
    params = []

    if entry['directives'].get(':method', None):

        algo = entry['directives'][':method']['value']

        if algo not in ALGORITHMS:
            raise FalconError(f"Directive :method not found {algo}")

        # get the real name
        algo = ALGORITHMS[algo]

        # deal with the parameters of the test
        # params = []                                         # the parameters of the algorithm
        for name, values in entry['directives'][':method']['params']:
            params.append('{}={}'.format(name, ''.join(values)))

        directives['params'] = params
    else:
        algo = 'zip'
        directives['params'] = []

    directives['algo'] = algo

    # *** logging ***

    if entry['directives'].get(':log', False):
        directives['use-log'] = True
    else:
        directives['use-log'] = False

    if entry['directives'].get(':log-name', False):
        directives['log-name'] = entry['directives'][':log-name']['value']
    else:
        directives['log-name'] = None

    # *** iterable object ***
    if entry['directives'].get(':iter-object', False):
        directives['iter-object'] = entry['directives'][':iter-object']['value']
    else:
        directives['iter-object'] = None

    if entry['directives'].get(':update', False):
        directives['update'] = True
    else:
        directives['update'] = False

    # *** save results & save cases ***

    if entry['directives'].get(':save-results', False):
        directives['save-results'] = True
    else:
        directives['save-results'] = False

    if entry['directives'].get(':save-cases', False):
        directives['save-cases'] = True
    else:
        directives['save-cases'] = False

    # *** leave the error message if available ***

    if entry['directives'].get(':no-error-message', False):
        directives['no-error-message'] = False
    else:
        directives['no-error-message'] = True

    # *** Groupby - min cases ***

    if entry['directives'].get(':min-cases', False):
        directives['min-cases'] =  int(entry['directives'][':min-cases']['value'])
    elif entry['directives'].get(':no-minimum', False):
        directives['min-cases'] = 0
    else:
        directives['min-cases'] = 1

    # *** either ***

    if entry['directives'].get(':either', False):
        directives['either'] = to_list(entry['directives'][':either']['value'])
    elif entry['directives'].get(':either', False):
        directives['either'] = None

    return directives


def get_predicate(stub, by_group=False): # -> Tuple[Predicate, List]:
    """Find & build the predicates"""

    predicate, values = None, None

    # is the predicate defined?
    if not by_group and PREDICATES.get(stub['predicate'], False): #stub.get('predicate', False):
        predicate = PREDICATES[stub['predicate']]
    elif by_group and PREDICATES.get(stub['group-predicate'], False):
        predicate = PREDICATES[stub['group-predicate']]
    elif by_group:
        predicate = Predicate(stub['group-predicate'], None, False, False, False, False)
        warnings.warn(f"Predicate '{predicate.name}' was not defined.")
    elif not by_group:
        predicate = Predicate(stub['predicate'], None, False, False, False, False)
        warnings.warn(f"Predicate '{predicate.name}' was not defined.")

    # get the values associated with it
    if stub.get('group-values', False):
        values = stub['group-values']
    elif stub.get('groupby-many-with-group', False):
        values = stub['groupby-many-with-group']
    elif stub.get('value', False):
        values = stub['value']
    elif stub.get('values', False):
        values = stub['values']

    # values
    # if not by_group:
    #     if stub.get('value', False):
    #         values = stub['value']
    #     elif stub.get('values', False):
    #         values = stub['values']
    # elif by_group:
    #     if stub.get('group-values', False):
    #         values = stub['group-values']
    #     elif stub.get('groupby-many-with-group', False):
    #         values = stub['groupby-many-with-group']

    return predicate, values


# assertion/group-tests builders ----------------

def make_boolean(entry, fn_sig='') -> str:

    indent: int = 0
    case = []
    line = []

    for element in entry['values']:

        if element == '(':
            case.append('(')
            continue
        elif element == ')':
            case.append(')')
            continue

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

            name = element[0]

            # get the predicate
            if name in PREDICATES:
                predicate = PREDICATES[name]
            else:
                predicate = Predicate(name, None, False, False, False, False, False, None)
                warnings.warn(f'Predicate "{name}" was not found')

            # predicate = element[0]
            # use_symbolic = element[1]

            # args = element[2:] if len(element) > 2 else None
            args = element[3:] if element[2] is False else None

            # if use_symbolic is not None:
            if predicate.symbol:
                # line.append(f1.format(fn_sig, use_symbolic, ''.join(args[1:])))
                line.append(f1.format(fn_sig, predicate.symbol, args[0]))
            # elif not args:
            else:
                line.append(f2.format(predicate.name, fn_sig))
            # else:
                # line.append(f3.format(predicate.name, fn_sig, ', '.join([str(a) for a in args])))
                # line.append(f3.format(predicate, fn_sig, ', '.join(args)))
        else:
            line.append(element)

    return ''.join(line)


def make_assert_stmt(stub, fn_name, args=None, just_result: bool = False, use_error_msg: bool = False):

    # just_result --> it is using 'result' instead of fn(args)

    indent: int = 0

    f1 = 'assert {} {} {}'              # w/ symbol             result < 4
    f2 = 'assert {}({}, {})'            # pd( fn(arg), value)
    f3 = 'assert {}({})'                # pd(result|args)

    # deal with no function, just acting on the predicates -> fn_sig ==> function-signature
    if fn_name == '_':
        fn_sig = args
    elif just_result:
        fn_sig = 'result'
    else:
        fn_sig = f'{fn_name}({args})'

    indent += 1
    line: str = ''

    # Predicate -> name, symbol, is_symbolic, is_error, is_group, doc_error

    # these are code / logical (and they have no 'predicate' argument)
    if stub['kind'] == 'logical' or stub['kind'] == 'assert-logical':
        return 'assert ' + make_boolean(stub['values'], fn_sig)
    elif stub['kind'] == 'code':
        return stub['value']
    elif stub['kind'] == 'codeline':
        return stub['value']

    # get the predicate or make one up & the values for the predicate
    if stub['predicate'] in PREDICATES:
        predicate, values = get_predicate(stub, False)
    else:
        predicate = Predicate(stub["predicate"], None, False, False, False, False, False, None)
        values = stub['value'] if stub.get('value', False) else stub['values']      # it will return True, not a (…)\
        warnings.warn(f'Predicate "{stub["predicate"]}" not found. Treating as a "raw" predicate.')

    # somewhere in the tree is says True (eg, is-none?), needs refactored out
    if isinstance(values, bool):
        values = None
    elif values == 'True':
        values = None

    # just have to know has-values, symbolic, is-error
    # or logical
    if stub['kind'] == 'predicate-fail-side-effect+':                           # special cases
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f2.format(predicate.name, fn_sig, ', '.join(stub['value']))
    elif stub['kind'] == 'predicate-fail-side-effect':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f3.format(predicate.name, fn_sig)
    elif stub['kind'] == 'assert-error+':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f2.format(predicate.name, fn_sig, ', '.join(stub['value'][1:]))
    elif stub['kind'] == 'assert-error':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f3.format(predicate.name, fn_sig)
    elif predicate.is_error and values is None:
        line = f'assert {predicate.name}({fn_name}, ({args}))'                            # calls it as fn, args
    elif predicate.is_error and values:
        line = f'assert {predicate.name}({fn_name}, ({args}), {", ".join(values)})'     # calls it as fn, args, values
    elif predicate.is_symbolic:
        line = f3.format(predicate.name, fn_sig)                                         # uses symbol
    elif values and isinstance(values, tuple):
        line = f2.format(predicate.name, fn_sig, ', '.join(values))
    elif values:
        line = f2.format(predicate.name, fn_sig, values)
    elif values is None:
        line = f3.format(predicate.name, fn_sig)

    # TODO: 'message' should be in all the stubs, eventually
    if 'error-message' in stub and stub['error-message'] is not None:
        line += f", {stub['error-message']}"
    elif use_error_msg and predicate.doc_error and predicate.error_message is not None:
        line += f", '{predicate.error_message}'"

    return line

# def make_assert_stmt(stub, fn_name, args=None, just_result: bool = False, use_error_msg: bool = False):
#
#     # TODO: REFACTOR to use Predicate
#     # just_result --> it is using 'result' instead of fn(args)
#
#     indent: int = 0
#
#     # TODO: 2 & 3 are the same!
#     f1 = 'assert {} {} {}'              # w/ symbol             result < 4
#     f2 = 'assert {}({}, {})'            # pd( fn(arg), value)
#     f3 = 'assert {}({}, {})'            # w/ function
#     f4 = 'assert {}({})'                # ignoring True
#
#     # deal with no function, just acting on the predicates
#     if fn_name == '_':
#         fn_sig = args
#     elif just_result:
#         fn_sig = 'result'
#     else:
#         # fn_sig = '{}({})'.format(fn_name, args) if not just_result else fn_name
#         fn_sig = f'{fn_name}({args})'
#
#     indent += 1
#     line = ''
#
#     # TODO get or create a Predicate type
#
#     # find
#     if (stub['kind'].startswith('predicate')) and (stub.get('predicate', '') not in PREDICATES):
#         warnings.warn(f'Predicate "{stub["predicate"]}" not found. Treating a "raw" predicate.')
#         predicate = Predicate(stub["predicate"], None, False, False, False, False, False, None)
#     elif stub['kind'] == 'assert-logical':
#         print('FIX!  make_assert_stmt')
#     elif stub['kind'] == 'logical':
#         print('FIX!  make_assert_stmt')
#     else:
#         predicate = PREDICATES[stub['predicate']]
#
#     use_symbolic = False
#     error_type = False
#
#     # TODO: refactor to this. Returns a namedtuple -> name, symbol, is_symbolic, is_error, is_group, doc_error
#     # predicate = PREDICATES[stub['predicate']]
#     # has_values = ...
#
#     if stub['kind'].startswith('predicate') and stub['predicate'] in PREDICATES:
#         # get the symbolic name if there is one, otherwise the function name
#
#         if PREDICATES[stub['predicate']][1]:
#             pd_name = PREDICATES[stub['predicate']][1]
#             use_symbolic = True
#         else:
#             pd_name = PREDICATES[stub['predicate']][0]
#             use_symbolic = False
#     elif stub['kind'].startswith('predicate'):
#         pd_name = PREDICATES[stub['predicate']][0]
#     elif stub.get('predicate', False):
#         # TODO: Does not handle symbolic tests!!!
#         pd_name = PREDICATES[stub['predicate']][0]
#     else:
#         # raise FalconError(f"Predicate {stub['predicate']} not found")
#         warnings.warn(f"Predicate {stub['predicate']} not found.")
#         pd_name = stub['predicate']
#
#     if stub['kind'] == 'predicate-value':
#         if PREDICATES[stub['predicate']].is_error and not just_result:
#             # it's an error
#             line = f'assert {pd_name}({fn_name}, {args}, {stub["value"]})'
#         elif PREDICATES[stub['predicate']].is_error and isinstance(stub["value"], tuple):
#             line = f2.format(pd_name, 'result', ','.join(stub["value"]))
#         elif PREDICATES[stub['predicate']].is_error:
#             line = f4.format(pd_name, 'result')
#         elif use_symbolic and stub['value'] == 'True':
#             line = f4.format(pd_name, fn_sig)
#         elif use_symbolic:
#             line = f1.format(fn_sig, pd_name, stub['value'])
#         else:
#             line = f2.format(pd_name, fn_sig, stub['value'])
#     elif stub['kind'] == 'predicate':
#         line = f4.format(pd_name, fn_sig)
#     elif stub['kind'] == 'predicate-value+':
#         line = f2.format(pd_name, fn_sig, ', '.join(stub['value']))
#     elif stub['kind'] == 'logical' or stub['kind'] == 'assert-logical':
#         line = 'assert ' + make_boolean(stub['values'], fn_sig)
#     elif stub['kind'] == 'code':
#         line = stub['value']
#     elif stub['kind'] == 'predicate-side-effect':
#         line = f4.format(pd_name, stub['name'])
#     elif stub['kind'] == 'predicate-side-effect+':
#         args = ', '.join(stub['values'])
#         line = f3.format(pd_name, stub['name'], args)
#     elif stub['kind'] == 'predicate-fail-side-effect+':
#         e = 'Exception' if stub["error"] is None else stub['error']
#         line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f2.format(pd_name, fn_sig, ', '.join(stub['value']))
#     elif stub['kind'] == 'predicate-fail-side-effect':
#         e = 'Exception' if stub["error"] is None else stub['error']
#         line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f4.format(pd_name, fn_sig)
#     elif stub['kind'] == 'assert-error+':
#         e = 'Exception' if stub["error"] is None else stub['error']
#         line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f2.format(pd_name, fn_sig, ', '.join(stub['value'][1:]))
#     elif stub['kind'] == 'assert-error':
#         e = 'Exception' if stub["error"] is None else stub['error']
#         line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f4.format(pd_name, fn_sig)
#
#     # this is how it should be done / need to accommodate no defined predicates
#     if pd_name in PREDICATES:
#         predicate = PREDICATES[pd_name]
#     else:
#         predicate = Predicate(pd_name, None, False, False, False, False, False, None)
#
#     # TODO: 'message' should be in all the stubs, eventually
#     if 'error-message' in stub and stub['error-message'] is not None:
#         line += f", {stub['error-message']}"
#     elif use_error_msg and predicate.doc_error and predicate.error_message is not None:
#         line += f", '{predicate.error_message}'"
#
#     return line


def make_assert_group_stmt(stub, fn_name, args):

    indent = 0
    fn_sig = '{}({})'.format(fn_name, args)
    indent += 1
    line = ''

    if stub['predicate'] not in PREDICATES:
        raise FalconError(f'Predicate "{stub["predicate"]}" not found')

    # get the name of the predicate if it knows it's a predicate (or should be, ie OOPS)
    if stub['predicate'] in PREDICATES:
        # get the symbolic name if there is one, otherwise the function name

        if PREDICATES[stub['predicate']][1]:
            pd_name = PREDICATES[stub['predicate']][1]
            use_symbolic = True
        else:
            pd_name = PREDICATES[stub['predicate']][0]
            use_symbolic = False
    else:
        pd_name = stub['predicate']
        use_symbolic = False
    # else:
    #     # TODO: raise error
    #     print('Predicate Not Found!', fn_sig, stub)
    #     pd_name = "OOPS!"

    f1 = 'assert {} {} {}'              # w/ symbol
    f2 = 'assert {}({}, {})'            # pd( fn(arg), value)
    f3 = 'assert {}({})'                # ignoring True

    if stub['using-bin-fn'] and stub['kind'] != 'winnow-many':
        if stub['kind'] == 'group-predicate':
            line = f3.format(pd_name, 'result')
        elif stub['kind'] == 'group-predicate-values' and use_symbolic:
            line = f1.format('result', pd_name, ''.join(stub['values']))
        elif stub['kind'] == 'group-predicate-values':
            line = f2.format(pd_name, 'result', ', '.join(stub['values']))
    elif stub['kind'] == 'winnow-many':
        if use_symbolic:
            line = f1.format('result', pd_name, ''.join(stub['values']))
        elif len(stub['values']) > 1:
            line = f2.format(pd_name, 'result', ', '.join(stub['values']))
        else:
            line = f3.format(pd_name, 'result') #'''.join(stub['values']))
    else:
        if stub['kind'] == 'group-predicate':
            line = f3.format(pd_name, args)
        elif stub['kind'] == 'group-predicate-values' and use_symbolic:           # this can't really happen
            line = f1.format(''.join(args), pd_name, ''.join(stub['values']))
        elif stub['kind'] == 'group-predicate-values' and use_symbolic:
            line = f3.format(pd_name, args)
        elif stub['kind'] == 'group-predicate-values':
            line = f2.format(pd_name, 'result', args)

    return line


def make_if_group_stmt(stub, fn_name, args):

    indent = 0
    fn_sig = '{}({})'.format(fn_name, args)
    indent += 1
    line = ''

    if stub['predicate'] not in PREDICATES:
        raise FalconError(f'Predicate "{stub["predicate"]}" not found')

    # get the name of the predicate if it knows it's a predicate (or should be, ie OOPS)
    if stub['predicate'] in PREDICATES:
        # get the symbolic name if there is one, otherwise the function name

        if PREDICATES[stub['predicate']][1]:
            pd_name = PREDICATES[stub['predicate']][1]
            use_symbolic = True
        else:
            pd_name = PREDICATES[stub['predicate']][0]
            use_symbolic = False
    else:
        pd_name = stub['predicate']
        use_symbolic = False

    # cond = 'if' if first else 'elif'

    f1 = '{} {} {}'              # w/ symbol
    f2 = '{}({}, {})'            # pd( fn(arg), value)
    f3 = '{}({})'                # ignoring True

    # TODO: groupby-many-with-group messes things up - does it work for all conditions?

    if stub['using-bin-fn'] and stub['kind'] != 'winnow-many':
        if stub['kind'] == 'group-predicate':
            line = f3.format(pd_name, 'result')
        elif stub['kind'] == 'group-predicate-values' and use_symbolic:
            line = f1.format('result', pd_name, ''.join(stub['values']))
        elif stub['kind'] == 'group-predicate-values':
            line = f2.format(pd_name, 'result', ', '.join(stub['values']))
    elif stub['kind'] == 'winnow-many':
        if use_symbolic:
            line = f1.format('result', pd_name, ''.join(stub['values']))
        elif len(stub['values']) > 1:
            line = f2.format(pd_name, 'result', ', '.join(stub['values']))
        else:
            line = f3.format(pd_name, 'result') #'''.join(stub['values']))
    else:
        if stub['kind'] == 'group-predicate':
            line = f3.format(pd_name, args)
        elif stub['kind'] == 'group-predicate-values' and use_symbolic:           # this can't really happen
            line = f1.format(''.join(args), pd_name, ''.join(stub['values']))
        elif stub['kind'] == 'group-predicate-values':
            # line = f3.format(pd_name, args)
            line = f2.format(pd_name, 'result', ', '.join(stub['values']))
        elif stub['kind'] == 'group-predicate-values':
            line = f2.format(pd_name, 'result', args)
        elif stub['kind'] == 'groupby-many-with-group':
            line = f3.format(pd_name, args)

    return line


def make_group_predicate_error(group: str, error_message: str, predicate_name: str, add_predicate: bool = True) -> str:

    # msg = ''

    if add_predicate is False:
        return ''

    if error_message is not None and error_message != '':
        return f", \"{error_message}\""

    return f', "Group {group} predicate \'{predicate_name}\' has failed"'

