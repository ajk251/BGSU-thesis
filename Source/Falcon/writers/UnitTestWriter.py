
import re
import runpy
import textwrap
import warnings

from collections import defaultdict
from datetime import datetime
from random import choices, randint
from string import ascii_letters, digits

# import predicates
from Falcon.algorithms.algorithms import ALGORITHMS
from Falcon.macros.macros import MACROS
from Falcon.predicates.predicates import PREDICATES
from Falcon.utilities.FalconError import FalconError
from Falcon.writers.tools import *

from Falcon import domains

# TODO:
#   add overwrite directive
#   add imports
#   warning for unrecognized directives
#   add falcon notes?

#   a new file for every unit test...? or directive for it?

tabsize: int = 4
TAB: str = ' ' * tabsize
nl: str = '\n'

# ⊻ ⊼ ⊽ ￫ these require special treatment…
booleans = {'∧': 'and', '&&': 'and', 'and': 'and',
            '∨': 'or', '||': 'or', 'or': 'or',
            '!': 'not', '¬': 'not', 'not': 'not'}

# writes the file -----------------------------------------

# NOTE:
#   unit tests can be by namespace {} or by command -u!


def write_basic_unittest(intermediate, source=None, destination=None,):

    # intermediate is the tree, source & destination are the names of the i/o

    # indent: int = 0
    # nl = '\n'

    # file = intermediate['global']['directives'].setdefault('file', './test.py')
    # file = 'Tests/tests.py' if 'file' not in intermediate['global']['directives'] else intermediate['global']['directives']['file']

    # the file can be a directive, in the commandline args, or a default
    if 'file' in intermediate['global']['directives']:
        file = intermediate['global']['directives']
    elif 'file' in intermediate['global']['directives']:
        file = intermediate['global']['directives']['file']
    elif destination is not None:
        file = destination
    else:
        file = 'Tests/test_falcon_unittest.py'

    with open(file, 'w', encoding='utf-8') as falcon:

        # write the boilerplate stuff, that applies globally
        lines = make_initial(intermediate['initial'], source)
        falcon.write(lines)

        lines = make_unittest(intermediate['global'], 0)
        falcon.write(lines)

        for block in intermediate['ordering']:

            kind, value = block

            if kind == 'code':
                line = code_block(value)
                falcon.write(line)
            elif kind == 'namespace':
                # lines = make_namespace(intermediate[value], value)
                lines = make_unittest(intermediate[value], 0)
                falcon.write(lines)

            falcon.write(nl)

        # finally!
        falcon.write('')


def make_global(entry) -> str:

    indent: int = 0
    lines = []

    # directives -----
    desc = entry['directives'].get(':desc', None)

    if desc:
        lines.append(indent * TAB + '# ' + desc)

    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        if kind == 'code':
            line = '\n' + code_block(value)
            lines.append(line)
        # elif kind == 'assertion':
        #     line = unit_assert2(entry['tests'][value])
        #     # line = basic_Assert(entry['tests'][value])
        #     lines.append(line)
        elif kind == 'domain':
            line = make_domain(value)
            lines.append(line)
        # elif kind == 'test':
        #     if entry['tests'][value]['kind'] == 'test-basic':
        #         line = unit_Test(entry['tests'][value])
        #         lines.append(line)
        #     # elif entry['tests'][value]['kind'] == 'winnow-test':
        #     elif entry['tests'][value]['kind'] == 'groupby-test':
        #         # line = basic_Winnow(entry['tests'][value], indent)
        #         # line = basic_Groupby(entry['tests'][value])
        #         line = unit_Groupby(entry['tests'][value])
        #         lines.append(line)
        #     # elif entry['tests'][value]['kind'] == 'winnow-test':
        #     #     line = unit_Winnow(entry['tests'][value])
        #     #     lines.append(line)
        #     elif entry['tests'][value]['kind'] == 'satisfy-test':
        #         line = unit_Satisfy(entry['tests'][value])
        #         lines.append(line)
        #     # elif entry['tests'][value]['kind'] == 'macro':
        #     #     line = basic_macros(entry['tests'][value])
        #     #     lines.append(line)

    # line = make_unittest(entry['ordering'])

    return '\n'.join(lines)


def make_unittest(entry, indent=0):

    lines = []

    # write unittest -------------
    lines.append('')

    line = 'class Test(unittest.TestCase):'
    lines.append(line)

    indent += 1

    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        if kind == 'assertion':
            line = unit_assert(entry['tests'][value])
            lines.append(line)
        elif kind == 'test':
            if entry['tests'][value]['kind'] == 'test-basic':
                line = unit_Test(entry['tests'][value], indent)
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'groupby-test':
                #line = unit_Winnow(entry['tests'][value], indent)
                line = unit_Groupby(entry['tests'][value])
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'satisfy-test':
                line = unit_Satisfy(entry['tests'][value], indent)
                lines.append(line)

    return '\n'.join(lines)


# for unit tests -------

def unit_assert(entry):

    indent = 1

    # directives -------------

    ignore_true = True          # this was an earlier attempt, eg is-int? True, TODO: refactor out

    # because assert is different, it can't use get_directives - it doesn't have the function & domain
    # message, pyfunc,

    # get the message, if any
    if entry['directives'].get(':message', None) is not None:
        message = entry['directives'][':message']['value']
    else:
        message = None

    # get the name of the function, create one, or append one
    # test-name ￫ user name, as-is. :name any name, but decorated

    fn_name = entry['function']

    if entry['directives'].get(':test-name', None):
        # TODO: raise warning if it does not start with test
        t_name = entry['directives'][':test-name']['value']
        pyfunc = indent * TAB + f'def {t_name}(self):'
    elif entry['directives'].get(':name', None):
        t_name = entry['directives'][':name']['value']
        pyfunc = f'def {t_name}' if t_name.startswith('test') else f'def test_{t_name}'
        pyfunc = indent * TAB + pyfunc + '(self):'
    else:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        pyfunc = indent * TAB + f'def test_{fn_name}_assertions_{rand_name}(self):' #.format(fn_name, rand_name)

    indent += 1

    # -----------------------
    a1 = 'assert {} {} {}'              # w/ symbol
    a2 = 'assert {}({}, {})'            # w/ function
    a3 = 'assert {}({})'                # ignoring True

    # -----------------------
    lines = ['', pyfunc, '']

    if message:
        lines.append((TAB * indent) + '# ' + message.strip('"'))

    for stub in entry['stubs']:

        if stub['kind'] == 'code':
            lines.append((TAB * indent) + stub['value'])
            continue

        # this is kind of a special case/after-thought
        if stub.get('predicate', False) and PREDICATES[stub['predicate']].is_symbolic:
            # these must raise an error, ie catches(fn, args, Exception)
            pd_name = PREDICATES[stub['predicate']].name
            args = make_args(stub['argument'])
            line = f"{indent * TAB}assert {pd_name}({fn_name}, {args}"
            line += f", {', '.join(s for s in stub['value'][1:] if s is not None)})" if len(stub['value']) > 1 else ')'
            lines.append(line)
            continue
        elif stub['kind'] == 'assert-logical':
            # logical conditions
            args = make_args(stub['argument']).strip('(').strip(')')
            line = (indent * TAB) + make_assert_stmt(stub, fn_name, args)
            lines.append(line)
            continue
        elif stub['kind'] == 'assert-error+':
            fn_sig = '{}({})'.format(fn_name, args) #if not just_result else fn_name
            e = 'Exception' if stub["error"] is None else stub['error']
            line = f'{(indent * TAB)}with pytest.raises({e}):\n' + ((indent + 1) * TAB) + 'assert {}({}, {})'.format(pd_name, fn_sig, ', '.join(stub['value'][1:]))
            lines.append(line)
            continue
        elif stub['kind'] == 'assert-error':
            fn_sig = '{}({})'.format(fn_name, args) #if not just_result else fn_name
            e = 'Exception' if stub["error"] is None else stub['error']
            line = f'{(indent * TAB)}with pytest.raises({e}):\n' + ((indent + 1) * TAB) + 'assert {}({})'.format(pd_name, fn_sig)
            lines.append(line)
            continue

        args = make_args(stub['argument'])
        fn = fn_name + args
        value = stub['value'][1:]

        if PREDICATES[stub['predicate']].is_symbolic:
            # the symbolic representation
            pd_name = PREDICATES[stub['predicate']].symbol
            line = a1.format(fn, pd_name, value)
        else:
            pd_name = PREDICATES[stub['predicate']].name

            if ignore_true and value == 'True':
                line = a3.format(pd_name, fn)
            elif stub['kind'] == 'logical':
                line = make_assert_stmt(stub, fn_name, args, just_result=False)
                # stmt = make_assert_stmt(stub, fn_name, args)
                # print(stmt)
            elif len(value) > 2:
                # more than 1 value in predicate args
                v = ', '.join(v for v in value[1:])
                line = f"assert {pd_name}({fn_name}{args}, {v})"
            else:
                line = a2.format(pd_name, fn, ', '.join(value))

        if 'error-message' in stub and stub['error-message'] is not None:
            line += f", {stub['error-message']}"

        # line = (TAB * indent) + line
        lines.append((TAB * indent) + line)

    # lines.append('')        # add a blank line

    return '\n'.join(lines)


def unit_Test(entry):

    indent: int = 1

    directives = get_directives(entry)

    message = directives['message']
    pyfunc = indent * TAB + directives['pyfunc'][:-3] + ('(self):')
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']

    # write tests ------
    # lines = ['\n# start test -----------------', pyfunc, '']
    lines = [pyfunc, '']
    indent += 1

    if message:
        line = indent * TAB + '# ' + message.strip('"')
        lines.append(line)

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(dvars) == 1:
        # note dvars is the number of domains, labels can be user-defined number to unpac
        template = indent * TAB + "for {} in {}:".format(','.join(labels), dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)

    # fn_name = entry['function']
    args = ', '.join(labels)

    indent += 1

    for stub in entry['stubs']:
        stmt = make_assert_stmt(stub, fn_name, args, indent)
        lines.append((indent * TAB) + stmt)

    lines.append('')

    indent -= 1

    return '\n'.join(lines)


def unit_Groupby(entry):

    indent = 0
    lines = ['']

    directives = get_directives(entry)

    # message = directives['message']
    # pyfunc = directives['pyfunc']
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']

    args = ', '.join(labels)
    fn_sig = '{}({})'.format(fn_name, args)

    # the def name
    lines.extend((f'def test_groupby_{fn_name}():', ''))

    # w1 has a separate bin function defined
    w1 = '''
try:
    result = {}
except Exception as e:
    result = e
                
try:
    group = {}(result)
except Exception as e:
    raise FalconError('Failed to properly partition the function')
    '''

    w2 = '''
try:
    group = {}
except Exception as e:   
    raise FalconError('Failed to properly partition the function')
'''

    indent += 1

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(labels) == 1:
        template = indent * TAB + "for {} in {}:".format(labels[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)
    indent += 1

    # build the template
    if entry['bin'] is not None:
        line = textwrap.indent(w1.format(fn_sig, entry['bin']), TAB * 2)
        lines.append(line)
        using_bin_fn = True
    else:
        line = textwrap.indent(w2.format(fn_sig), TAB * 2)
        lines.append(line)
        using_bin_fn = False

    # deal with the groups
    groups = defaultdict(list)

    # the groupby!
    for stub in entry['stubs']:

        stub['using-bin-fn'] = using_bin_fn
        stmt = make_assert_group_stmt(stub, fn_name, args, indent)
        groups[stub['group']].append(stmt)

    assert len(groups) > 1, "the number of groups must be greater than 1"

    # indent += 1

    groups, stmts = tuple(groups.keys()), tuple(groups.values())

    # first one is a special case, ie 'if'
    line = (indent * TAB) + f'if group == {groups[0]}:\n' #+ ((indent + 1) * TAB) + '\n'.join(groups[0][1])
    line += '\n'.join([((indent + 1) * TAB) + stmt for stmt in stmts[0]])
    lines.append(line)

    for group, stmts in zip(groups[1:], stmts[1:]):
        # line = (indent * TAB) + f'elif group == {group}:\n' + ((indent + 1) * TAB) + '\n'.join(stmt)
        line = (indent * TAB) + f'elif group == {group}:\n'
        line += '\n'.join([(indent + 1) * TAB + stmt for stmt in stmts])
        lines.append(line)

    # add failure case
    failure = (indent * TAB) + f'else:\n' + ((indent + 1) * TAB) + 'raise FalconError("Failed to meet at least one group") \t\t# TODO…'
    lines.append(failure)

    lines.append('')

    return '\n'.join(lines)


def unit_Satisfy(entry) -> str:

    lines = []
    indent: int = 0

    return '# Satisfy here…'

    # build the function name & vars
    fn_name = entry['function']

    # def name
    line = (indent * TAB) + f'def test_satisfy_{fn_name}(self):'
    lines.extend((line, ''))

    # if something goes wrong with the 1st…

    # w1 has a separate bin function defined
    w1 = '''
try:
    result = {}
except Exception as e:
    assert False, "Function error"
    continue
                
try:
    group = {}(result)
except Exception as e_bin:
    assert False, "Group-by error"   
    continue
    '''

    w2 = '''
try:
    result = {}
    group = result
except Exception as e:   
    assert False, "Function error"
    continue
'''

    # *** get suffix ***
    if entry['directives'].get(':suffix', None):
        suffix = entry['directives'][':suffix']['value']
    else:
        suffix = 'ᵢ'

    # get the variable names
    dvars = entry['domain']                                 # the domain names
    ivars = [d.lower() + suffix for d in dvars]                # the name of the values in the domain
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
    lines.append('')

    # reset the count in the loop
    lines.append(((indent + 1) * TAB) + 'count = 0')

    indent += 1

    # build the template
    if entry['bin'] is not None:
        line = textwrap.indent(w1.format(fn_sig, entry['bin']), TAB * indent)
        lines.append(line)
    else:
        line = textwrap.indent(w2.format(fn_sig), TAB * indent)
        lines.append(line)

    # deal with the groups
    groups = defaultdict(list)

    for stub in entry['stubs']:
        stmt = make_assert_stmt(stub, 'result', indent)
        groups[stub['group']].append(stmt)

    assert len(groups) > 1, "the number of groups must be greater than 1"

    # indent += 1

    # TODO: if there are multiple statements, this will fail.

    for group, stmt in groups.items():
        line = (indent * TAB) + f'if group == {group}:\n' + ((indent + 1) * TAB) + '\n'.join(stmt)
        line += '\n' + ((indent + 1) * TAB) + 'count += 1'
        lines.append(line)

    # add failure case
    case = '{' + ",".join(ivars) + '}'
    failure = (indent * TAB) + 'assert count >= 1, f"Case {} did not satisfy at least 1 case"'.format(case)
    lines.append(failure)

    lines.append('')

    return '\n'.join(lines)

