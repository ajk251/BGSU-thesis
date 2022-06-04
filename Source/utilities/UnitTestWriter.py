
import re
import runpy
import textwrap
import sys
import warnings

from collections import defaultdict
from datetime import datetime
from random import choices, randint
from string import ascii_letters, digits
from typing import Any, Tuple, List, Optional, Union

# import predicates
from algorithms.algorithms import ALGORITHMS
from macros.macros import MACROS
from predicates.predicates import PREDICATES
from utilities.FalconError import FalconError

import domains
import macros

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


def write_basic_unittest(intermediate, source=None):

    # print('Predicates avaliable: ', len(p.PREDICATES))

    # indent: int = 0
    # nl = '\n'

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
                # lines = make_namespace(intermediate[value], value)
                lines = make_unittest(intermediate[value], 0)
                falcon.write(lines)

            falcon.write(nl)

        # finally!
        falcon.write('')


# utils ---------------------------------------------------


def clean(name):
    # from here: https://stackoverflow.com/questions/3303312/how-do-i-convert-a-string-to-a-valid-variable-name-in-python
    text = re.sub('\W|^(?=\d)','_', name)
    return text.title()


def to_list(text):
    # because I screwed up. I should have made this a json first, so I don't have to read it by characters...

    txt = text.split(',')
    txt[0] = txt[0].strip('[')
    txt[-1] = txt[-1].strip(']')

    values = []

    for value in txt:

        value = value.strip().rstrip('\'').lstrip('\'')
        values.append(value)

    return values


# component writers ---------------------------------------
#   ie build the strings to be written

# note → these should only write exactly what they are supposed to, no more no less

def make_initial(entry, source=None) -> str:

    lines = []

    lines.append(add_imports(entry['imports']))              # always 1+
    lines.append('')                                        # blank
    lines.append(falcon_intro(source))         # hello!

    return '\n'.join(lines)


def make_unittest(entry, indent=0):

    lines = []

    # directives -----------------

    # write other stuff ----------
    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        if kind == 'code':
            line = code_block(value)
            lines.append(line)
        elif kind == 'domain':
            line = make_domain(value, indent)
            lines.append(line)

    # write unittest -------------
    lines.append('')

    line = 'class Test(unittest.TestCase):\n'
    lines.append(line)

    indent += 1

    for block in entry['ordering']:

        kind, value = block if len(block) == 2 else (block[0], block[1:])

        if kind == 'assertion':
            line = unit_Assert(entry['tests'][value])
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

            # TODO Add winnow!

    return '\n'.join(lines)


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
        elif kind == 'assertion':
            line = basic_Assert(entry['tests'][value])
            lines.append(line)
        elif kind == 'domain':
            line = make_domain(value)
            lines.append(line)
        elif kind == 'test':
            if entry['tests'][value]['kind'] == 'test-basic':
                line = basic_Test(entry['tests'][value])
                lines.append(line)
            # elif entry['tests'][value]['kind'] == 'winnow-test':
            elif entry['tests'][value]['kind'] == 'groupby-test':
                # line = basic_Winnow(entry['tests'][value], indent)
                # line = basic_Groupby(entry['tests'][value])
                line = basic_Groupby2(entry['tests'][value])
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'winnow-test':
                line = basic_Winnow2(entry['tests'][value])
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'satisfy-test':
                line = basic_Satisfy2(entry['tests'][value])
                lines.append(line)
            elif entry['tests'][value]['kind'] == 'macro':
                line = basic_macros(entry['tests'][value])
                lines.append(line)

    return '\n'.join(lines)


# boilerplate ----------
def add_imports(entry) -> str:

    # TODO: Make these prettier

    lines = ['from algorithms.algorithms import *',
             'from domains import *',
             'from macros import *',
             'from predicates import *',
             'from utilities.utls import call',
             'from utilities.TestLogWriter import write_to_log',
             'from utilities import FalconError\n',
             'from collections import defaultdict',
             'import unittest\n',
             'import pytest']

    for module, args in entry:

        line = ''

        if len(args) == 0:
            line = 'import ' + module
        elif 'from' in args and 'as' in args:
            line = 'from {} import {} as {}'.format(module, args['from'], args['as'])
        elif 'from' in args and '[' in args['from']:
            s = args['from'].strip('[]').split(',')         # for some reason, this is just a string
            line = 'from {} import {}'.format(module, ','.join(fn for fn in s))
        elif 'all' in args:
            line = 'from {} import *'.format(module)
        elif 'from' in args:
            line = 'from {} import {}'.format(module, args['from'])
        elif 'as' in args:
            line = 'import {} as {}'.format(module, args['as'])

        # has to load the module to get the predicates from predicates.PREDICATES
        # TODO: maybe force every test module to have …_predicates, to avoid imports‽
        runpy.run_module(module)

        lines.append(line)

    return '\n'.join(lines)


def falcon_intro(source=None):

    intro = "# This file was generated automatically by falcon."
    intro += '' if not source else '\n# from: ' + source
    intro += '\n# on ' + datetime.now().strftime("%Y %b %d %a %H:%M:%S") + nl + nl

    return intro


# testers --------------
def basic_macros(entry) -> str:

    name = entry['name']

    if MACROS.get(name, False):
        lines = MACROS[name][0](entry)
    else:
        raise FalconError(f'{name} is not a Falcon function or macro')

    return '\n'.join(lines)


def basic_Test(entry) -> str:

    # Test - a for-loop over some domain with n predicates

    indent: int = 0

    directives = get_directives(entry)

    message = directives['message']
    pyfunc = directives['pyfunc']
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']
    obj_update = directives['object-update']

    # write tests ------
    lines = ['\n# start test -----------------', pyfunc, '']
    indent += 1

    if message:
        line = indent * TAB + '# ' + message.strip('"') + nl
        lines.append(line)

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(dvars) == 1:
        # note dvars is the number of domains, labels can be user-defined number to unpack
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
        stmt = make_assert_stmt(stub, fn_name, args)
        lines.append((indent * TAB) + stmt)

    lines.append('')

    if obj_update:
        # test_case = ', '.join(str(arg) for arg in args)
        for domain in entry['domain']:
            line = indent * TAB + domain + "()"
            lines.append(line)

    # indent -= 1

    return '\n'.join(lines)


def basic_Assert(entry) -> str:

    # n predicates

    # TODO:
    #   add directive for value = … \ assert predicate(value, args)...
    #   handle messages, ie assert …, <message>
    #   extra args!!! raise error!
    #   add explanations

    # directives -------------

    indent: int = 0
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
        pyfunc = f'def {t_name}():'
    elif entry['directives'].get(':name', None):
        t_name = entry['directives'][':name']['value']
        pyfunc = f'def {t_name}():' if t_name.startswith('test') else f'def test_{t_name}():'

    else:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        pyfunc = f'def test_{fn_name}_assertions_{rand_name}():' #.format(fn_name, rand_name)

    indent += 1

    # -----------------------
    a1 = 'assert {} {} {}'              # w/ symbol
    a2 = 'assert {}({}, {})'            # w/ function
    a3 = 'assert {}({})'                # ignoring True

    # -----------------------
    lines = ['', pyfunc + '\n']

    if message:
        lines.append((TAB * indent) + '# ' + message.strip('"'))

    # fn_name = entry['function']

    for stub in entry['stubs']:

        if stub['kind'] == 'code':
            lines.append((TAB * indent) + stub['value'])
            continue

        # this is kind of a special case/after-thought
        if stub.get('predicate', False) and PREDICATES[stub['predicate']][2]:
            # these must raise an error, ie catches(fn, args, Exception)
            pd_name = PREDICATES[stub['predicate']][0]
            args = make_args(stub['argument'])
            line = f"{indent * TAB}assert {pd_name}({fn_name}, {args}"
            line += f", {', '.join(stub['value'][1:])})" if len(stub['value']) > 1 else ')'
            lines.append(line)
            continue
        elif stub['kind'] == 'assert-logical':
            # logical conditions
            args = make_args(stub['argument']).strip('(').strip(')')
            line = (indent * TAB) + make_assert_stmt(stub, fn_name, args)
            lines.append(line)
            continue
        elif stub['kind'] == 'assert-error':
            # error stubs
            if len(stub['value']) > 2:
                stub['kind'] = 'assert-error+'
            args = make_args(stub['argument']).strip('(').strip(')')
            line = (indent * TAB) + make_assert_stmt(stub, fn_name, args)
            lines.append(line)
            continue

        args = make_args(stub['argument'])
        fn = fn_name + args
        value = stub['value']

        if PREDICATES[stub['predicate']][1]:
            # the symbolic representation
            pd_name = PREDICATES[stub['predicate']][1]
            line = a1.format(fn, pd_name, value)
        else:
            pd_name = PREDICATES[stub['predicate']][0]

            if ignore_true and value == 'True':
                line = a3.format(pd_name, fn)
            elif stub['kind'] == 'logical':
                make_assert_stmt(stub, fn_name, args, just_result=False)
                # stmt = make_assert_stmt(stub, fn_name, args)
                # print(stmt)
            elif len(value) > 2:
                # more than 1 value in predicate args
                v = ', '.join(v for v in value[1:])
                line = f"assert {pd_name}({fn_name}{args}, {v})"
                # line = a2.format(pd_name, fn_name, ', '.join((v for v in value[1:])))
            else:
                line = a2.format(pd_name, fn, value)

        # TODO: 'message' should be in all the stubs, eventually
        if 'error-message' in stub and stub['error-message'] is not None:
            line += f", {stub['error-message']}"

        # line = (TAB * indent) + line
        lines.append((TAB * indent) + line)

    return '\n'.join(lines)


def basic_Groupby2(entry) -> str:

    # groupby - predicates must hold for every group member, n groups, m predicates

    indent: int = 0
    lines = ['']

    directives = get_directives(entry)

    # message = directives['message']
    pyfunc = directives['pyfunc']
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']
    followup = directives['follow-up']

    save_results = True if entry.get(':no-results', True) else False
    save_groups = True if entry.get(':no-cases', True) else False

    args = ', '.join(labels)
    fn_sig = '{}({})'.format(fn_name, args)

    # the def name
    lines.extend((f'{pyfunc}', ''))

#     # w1 has a separate bin function defined
#     w1 = '''
# try:
#     result = {}
# except Exception as e:
#     result = e
#
# try:
#     group = {}(result)
# except Exception as e:
#     raise FalconError('Failed to properly partition the function')
#     '''

    w2 = '''
try:
    result = {}
except Exception as e:
    result = e
'''

    indent += 1

    if save_groups:
        line = (indent * TAB) + 'groups = defaultdict(list)'
        lines.append(line)
    if save_results:
        line = (indent * TAB) + 'results = defaultdict(list)\n'
        lines.append(line)

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(labels) == 1:
        template = indent * TAB + "for {} in {}:".format(labels[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)

    # build the template
    line = textwrap.indent(w2.format(fn_sig, entry['bin'], ', '.join(labels)), TAB * 2)
    lines.append(line)
    using_bin_fn = False

    # =========================================

    # collected all the groups {name: stub...}
    groups = defaultdict(list)

    for stub in entry['stubs']:
        groups[stub['group']].append(stub)

    groups = tuple(groups.items())      # flatten
    agg_groups = []                     # the groups that have aggregated ops on them
    labels = ', '.join(labels)

    cond = 'if'         # rather than have if if, if elif, ...

    for group, stub in groups:

        # the if statement
        if len(stub) > 1:
            names = []
            for s in stub:
                # just the predicates, no values
                predicate, _ = get_predicate(s, by_group=False)
                text = f"{predicate.name}({labels})"
                names.append(text)
            line = f"{indent * TAB}{cond} {' or '.join(names)}:\n"
        else:
            predicate, values = get_predicate(stub[0], by_group=False)
            line = f"{indent * TAB}{cond} {predicate.name}({labels}):\n"

        cond = 'elif'

        # the sub-parts is there a group-predicate test & by-value/by-all
        gpredicate, gvalues = get_predicate(stub[0], by_group=True)
        indent += 1

        # the first two go at the end
        if gpredicate.is_group and gvalues is not None:
            gline = f"{indent * TAB}assert {gpredicate.name}(results[{group}], {', '.join(gvalues)})"
            agg_groups.append(gline)
        elif gpredicate.is_group:
            gline = f"{indent * TAB}assert {gpredicate.name}(results[{group}])"
            agg_groups.append(gline)
        if gpredicate.is_group or gpredicate is None:
            line += ''
        elif gvalues is not None:
            line += f"{indent * TAB}assert {gpredicate.name}(result, {', '.join(gvalues)})"
        else:
            line += f"{indent * TAB}assert {gpredicate.name}(result)"

        #

        # save if necessary
        if save_groups:
            line +=  f'\n{indent * TAB}groups[{groups[0][0]}].append({labels})'
        if save_results:
            line += f'\n{indent * TAB}results[{groups[0][0]}].append(result)'

        lines.append(line)
        indent -= 1

    # add the last group
    line = f"{indent * TAB}else:\n{(indent + 1) * TAB}raise FalconError('Failed to meet at least one group')"
    lines.append(line)
    lines.append('')

    # add the aggregate group operations
    lines.extend(agg_groups)

    # ==========================================

    # # deal with the groups
    # groups = defaultdict(list)
    # gb_groups = {}
    # group_predictes = {}
    #
    # # TODO: This needs work... need a separate function for all the cases & error handling...
    # # TODO: - The commented out code is for the group assert? Is it necessary?
    # #       -> fix it with a directive
    #
    # for stub in entry['stubs']:
    #
    #     stub['using-bin-fn'] = using_bin_fn
    #     stmt = make_if_group_stmt(stub, fn_name, args)
    #     groups[stub['group']].append(stmt)
    #
    #     if stub['kind'] == 'groupby-many-with-group':
    #         gb_groups[stub['group']] = (stub['group-predicate'], stub['group-values'])
    #
    #     if stub.get('group-predicate', False):
    #         group_predictes[stub['group']] = (stub['group-predicate'], stub['group-values'])
    #     else:
    #         group_predictes[stub['group']] = (None, None)
    #
    # # assert len(groups) > 1, "the number of groups must be greater than 1"
    #
    # indent += 1
    # groups = tuple(groups.items())
    #
    # # the first statement is an 'if'
    # cond = ' or '.join((predicate for predicate in groups[0][1])) if len(groups[0][1]) > 1 else groups[0][1][0]
    # case = '(' + ', '.join((lbl for lbl in labels)) + ')' if len(labels) > 1 else f'({labels[0]},)'
    # line = f'{indent * TAB}if {cond}:'
    #
    # # TODO: check that the first one is not a group predicate!!!
    #
    # if stub['kind'] == 'groupby-many-with-group':
    #     group = groups[0][0]
    #     pd = PREDICATES.get(gb_groups[group][0], (None, None, None, None))
    #     line += f'\n{(indent + 1) * TAB}assert {pd[0]}(result)'
    #
    # # line += f'\n{(indent + 1) * TAB}groups[{groups[0][0]}].append((result, {case}))'
    # line +=  f'\n{(indent + 1) * TAB}groups[{groups[0][0]}].append({case})'
    # line += f'\n{(indent + 1) * TAB}results[{groups[0][0]}].append(result)'
    #
    # lines.append(line)
    #
    # for group, stmts in groups[1:]:
    #
    #     # note: group is (name, args ∨ [])
    #
    #     cond = ' or '.join((predicate for predicate in stmts)) if len(stmts) > 1 else stmts[0]
    #     line = f'{indent * TAB}elif {cond}:'
    #
    #     # check what kind of predicate should be applied & valid & stuff
    #     if stub['kind'] == 'groupby-many-with-group':
    #
    #         pd = PREDICATES.get(gb_groups[group][0], (None, None, None, None))
    #
    #         if len(stub['group-values']) > 0:
    #             # print(stub['group-values'], len(stub['group-values']))
    #             args = ', '.join(stub['group-values'])
    #         else:
    #             args = None
    #
    #         # print('args ', args, group, group_predictes[group])
    #
    #         # if it is a group predicate or has no name, skip it
    #         if pd.is_group or pd[0] is None:
    #             line += ''                      # do nothing...
    #         elif args is not None:
    #             # print('has args ', args, type(args))
    #             line += f'\n{(indent + 1) * TAB}assert {pd.name}(result, {args})'
    #         else: # elif PREDICATES.get(pd.name, False):
    #             line += f'\n{(indent + 1) * TAB}assert {pd.name}(result)'
    #
    #     line += f'\n{(indent + 1) * TAB}groups[{group}].append({case})'
    #     line += f'\n{(indent + 1) * TAB}results[{group}].append(result)'
    #     lines.append(line)

    # line = f"{indent * TAB}else:\n{(indent + 1) * TAB}FalconError('Failed to meet at least one group')"
    # lines.append(line)
    #
    # # this might need to be optional
    # lines.append('')
    #
    # # # add group assert statements
    # for group, pd in group_predictes.items():
    #
    #     if pd[0] is None: continue
    #
    #     if grp_pd := PREDICATES.get(pd[0], False):
    #         pd_name = grp_pd[0]
    #     else:
    #         # raise FalconError(f"Predicate {pd[0]} not found"
    #         warnings.warn(f"Predicate {pd[0]} not found")
    #
    #     # write the group assert statement, if it is a group-predicate
    #     if not grp_pd[3]:
    #         continue
    #     if pd[1] == []:
    #         line = f'{indent * TAB}assert {pd_name}(results[{group}])'
    #     else:
    #         line = f"{indent * TAB}assert {pd_name}(results[{group}], {', '.join(pd[1])})"
    #
    #     lines.append(line)

    indent -= 1

    if followup:
        line = f'\n{indent * TAB}{followup}(groups, results)'
        lines.append(line)

    lines.append('')

    return '\n'.join(lines)


def basic_Winnow(entry) -> str:

    # winnow - predicates must hold for every group member, n groups, m predicates
    #        - predicates must hold for each group

    indent: int = 0
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

    for stub in entry['stubs']:

        stub['using-bin-fn'] = using_bin_fn

        # if using_bin_fn:
        stmt = make_assert_group_stmt(stub, fn_name, args)
        # else:
        #     stmt = make_assert_stmt(stub, fn_name, args, indent)

        groups[stub['group']].append(stmt)

    # assert len(groups) > 1, "the number of groups must be greater than 1"

    indent += 1

    groups = tuple(groups.items())

    # first one is a special case, ie 'if'
    line = (indent * TAB) + f'if group == {groups[0][0]}:\n' + ((indent + 1) * TAB) + '\n'.join(groups[0][1])
    lines.append(line)

    # TODO: if there are multiple statements, this will fail.

    for group, stmt in groups[1:]:
        line = (indent * TAB) + f'elif group == {group}:\n' + ((indent + 1) * TAB) + '\n'.join(stmt)
        lines.append(line)

    # add failure case
    failure = (indent * TAB) + f'else:\n' + ((indent + 1) * TAB) + 'raise FalconError("Failed to meet at least one group") \t\t# TODO…'
    lines.append(failure)

    lines.append('')

    return '\n'.join(lines)


def basic_Winnow2(entry) -> str:

    # winnow - predicates must hold for every group member, n groups, m predicates

    indent: int = 0
    lines = ['']

    directives = get_directives(entry)

    # message = directives['message']
    # pyfunc = directives['pyfunc']
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']
    followup = directives['follow-up']

    # these are for the log
    use_log = directives['use-log']
    log_name = directives['log-name']

    # these are the minimum and maximum number of predicates that should be meet.
    if entry['directives'].get(':min', False):
        minimum = entry['directives'][':min']['value']
    else:
        minimum = 1

    if entry['directives'].get(':max', False):
        maximum = entry['directives'][':max']['value']
    else:
        maximum = None

    args = ', '.join(labels)
    fn_sig = '{}({})'.format(fn_name, args)

    # the def name
    lines.extend((f'def test_winnow_{fn_name}():', ''))

#     # w1 has a separate bin function defined
#     w1 = '''
# try:
#     result = {}
# except Exception as e:
#     result = e
#
# try:
#     group = {}(result)
# except Exception as e:
#     raise FalconError('Failed to properly partition the function')
#     '''

    w2 = '''
try:
    result = {}
except Exception as e:
    result = e
'''

    indent += 1

    line = (indent * TAB) + 'groups = defaultdict(list)\n'
    lines.append(line)

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(labels) == 1:
        template = indent * TAB + "for {} in {}:".format(labels[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)

    # build the template
    line = textwrap.indent(w2.format(fn_sig, entry['bin'], ', '.join(labels)), TAB * 2)
    lines.append(line)
    using_bin_fn = False

    # deal with the groups
    groups = defaultdict(list)

    for stub in entry['stubs']:

        stub['using-bin-fn'] = using_bin_fn
        stmt = make_if_group_stmt(stub, fn_name, args)
        groups[stub['group']].append(stmt)

    # assert len(groups) > 1, "the number of groups must be greater than 1"

    indent += 1
    groups = tuple(groups.items())

    # the first statement is an 'if'
    # cond = ' or '.join((predicate for predicate in groups[0][1])) if len(groups[0][1]) > 1 else groups[0][1][0]
    # case = '(' + ', '.join((lbl for lbl in labels)) + ')' if len(labels) > 1 else f'({labels[0]},)'
    # line = f'{indent * TAB}if {cond}:\n{(indent + 1) * TAB}groups[{groups[0][0]}].append((result, {case}))'
    # lines.append(line)

    case = '(' + ', '.join((lbl for lbl in labels)) + ')' if len(labels) > 1 else f'({labels[0]},)'

    for group, stmts in groups:
        cond = ' or '.join((predicate for predicate in stmts)) if len(stmts) > 1 else stmts[0]
        line = f'{indent * TAB}if {cond}:\n{(indent + 1) * TAB}groups[{group}].append((result, {case}))'
        lines.append(line)

    lines.append('')

    # deal with the group predicates
    for stub in entry['stubs']:

        if (stub['kind'].startswith('predicate')) and (stub.get('predicate', '') not in PREDICATES):
            raise FalconError(f'Predicate "{stub["predicate"]}" not found')

        pd = PREDICATES[stub['group-predicate']][0]
        stmt = f"{indent * TAB}assert {pd}(groups[{stub['group']}], {', '.join(stub['group-values'])})"

        lines.append(stmt)

    # add an 'if not captured…'
    if use_log:
        line = '\n' + (indent * TAB) + 'if count == 0:\n' + ((indent+1) * TAB) + 'oracles["random-test"].append((({}), repr(result)))'.format(', '.join(labels))
        lines.append(line)

    lines.append('')

    line = f'{(indent * TAB)}assert count <= {minimum}, f"The minimum number of predicates has not been met - met: {{count}}, min: {minimum}"'
    lines.append(line)

    if maximum is not None:
        line = (indent * TAB) + f'assert count > {maximum}, f"Exceed number of predicates met - met: {{count}}, max: {maximum}"'
        lines.append(line)

    if followup:
        line = f'\n{indent * TAB}{followup}(groups)'
        lines.append(line)

    indent -= 1

    lines.append('')

    return '\n'.join(lines)


def basic_Satisfy2(entry):

    # at least 1 or more predicates must be true
    indent: int = 0
    directives = get_directives(entry)

    message = directives['message']
    pyfunc = directives['pyfunc']
    dvars = entry['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']

    # these are for the log
    use_log = directives['use-log']
    log_name = directives['log-name']

    # these are the minimum and maximum number of predicates that should be meet.
    if entry['directives'].get(':min', False):
        minimum = entry['directives'][':min']['value']
    else:
        minimum = 1

    if entry['directives'].get(':max', False):
        maximum = entry['directives'][':max']['value']
    else:
        maximum = None

    # write tests ------
    lines = ['', pyfunc, '']
    indent += 1

    if message:
        line = indent * TAB + '# ' + message.strip('"') + nl
        lines.append(line)

    # lines.append((indent * TAB + 'errors = []\n'))
    if use_log:
        lines.append((indent * TAB + 'oracles = defaultdict(list)\n'))

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(dvars) == 1:
        template = indent * TAB + "for {} in {}:".format(','.join(labels), dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)

    args = ', '.join(labels)
    fn_sig = '{}({})'.format(fn_name, args)

    header = f"""
try:
    result = {fn_sig}
except Exception as error:
    result = error

count = 0
"""

    # has_error = True    -> this was on the code, removing it...

    # line = textwrap.indent(header.format(fn_sig), TAB * 2)
    line = textwrap.indent(header, TAB * 2)
    lines.append(line)

    indent += 1

    for stub in entry['stubs']:

        # the actual test assertion
        stmt = make_assert_stmt(stub, 'result', None, True)

        if stub['kind'].startswith('predicate'):

            # this is cheating and bad form
            #remove the left
            test = stmt.lstrip('assert').lstrip()           # otherwise a weird bug with result < 4 --> sult < 4

            #remove the right, if needed
            if stub['error-message'] is not None:
                test = test.rstrip(', ' + stub['error-message'])

            lines.append((indent * TAB) + 'if ' + test + ':')
            lines.append(((indent+1) * TAB) + 'count += 1')

            if use_log:
                lines.append(((indent+1) * TAB) + f"oracles['{stub['predicate']}'].append((({', '.join(labels)}), repr(result)))")

            # lines.append(((indent+1) * TAB) + stmt)

            # # assume that the error has been caught
            # if PREDICATES[stub['predicate']][2]:
            #     lines.append(((indent+1) * TAB) + 'has_error = False')
        elif stub['kind'] == 'code':
            line = '\n' + (indent * TAB) + stub['value'] + '\n'
            lines.append(line)

    # finish    part of the has_error stuff
    # line = '\n' + (indent * TAB) + 'if has_error:\n' + ((indent+1) * TAB) + 'errors.append((({}), result))'.format(', '.join(labels))
    # lines.append(line)
    # lines.append('')

    # add an 'if not captured…'
    if use_log:
        line = '\n' + (indent * TAB) + 'if count == 0:\n' + ((indent+1) * TAB) + 'oracles["random-test"].append((({}), repr(result)))'.format(', '.join(labels))
        lines.append(line)

    lines.append('')

    line = (indent * TAB) + f'assert count >= {minimum}, f"The minimum number of predicates has not been met - met: {{count}}, min: {minimum}  [with {{result}}]"'
    lines.append(line)

    if maximum is not None:
        line = (indent * TAB) + f'assert count > {maximum}, f"Exceed number of predicates met - met: {{count}}, max: {maximum}"'
        lines.append(line)

    # this doesn't work...
    # line = (indent * TAB) + f'assert len(errors) == 0, f"Unaccounted for errors - {{len(errors)}} errors occurred"'
    # lines.append(line)

    indent -= 1         # out of the for-loop

    if use_log:
        logname = "./FalconTestLog.txt" if not log_name else log_name
        line = '\n' + (indent * TAB) + f'write_to_log("{logname}", {{"name": {fn_name}, "predicates": oracles}})'
        lines.append(line)

    lines.append('')

    return '\n'.join(lines)


# for unit tests -------

def unit_Assert(entry):

    # TODO:
    #   add directive for value = … \ assert predicate(value, args)...
    #   handle messages, ie assert …, <message>
    #   extra args!!! raise error!
    #   add explanations

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

    fn_name = entry['function']

    for stub in entry['stubs']:

        # if not stub['argument']['kind'] == 'assertion': raise "WTF"

        if stub['kind'] == 'code':
            lines.append((TAB * indent) + stub['value'])
            continue

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

        # TODO: 'message' should be in all the stubs, eventually
        if 'error-message' in stub and stub['error-message'] is not None:
            line += f", {stub['error-message']}"

        # line = (TAB * indent) + line
        lines.append((TAB * indent) + line)

    lines.append('')

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


def make_domain(entry) -> str:

    indent: int = 0

    # TODO: if name fails raise error
    #       add :annotate to add/or not "# domains"

    # format templates
    f1 = (indent * TAB) + '{} = {}()'              # x = Reals()
    f2 = (indent * TAB) + '{} = {}({})'            # x = Reals(lb, ub)
    f3 = (indent * TAB) + '{} = {}({}, {})'        # x = Reals(lb, ub, nrandom=10)
                                                   # x = Reals(nrandom=10) ???

    if entry['kind'] == 'domain':
        var = entry['var-name']
        name = domains.DOMAINS[entry['domain']]
        line = f1.format(var, name)
    elif entry['kind'] == 'domain-args':

        var = entry['var-name']
        name = domains.DOMAINS[entry['domain']]

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


def make_boolean(entry, fn_sig='') -> str:

    indent: int = 0
    case = []
    line = []

    for element in entry['values']:

        # if element == '(': continue
        # elif element == ')': continue

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

            predicate = element[0]
            use_symbolic = element[1]
            # args = element[2:] if len(element) > 2 else None
            args = element[3:] if element[2] is False else None

            if use_symbolic is not None:
                # line.append(f1.format(fn_sig, use_symbolic, ''.join(args[1:])))
                line.append(f1.format(fn_sig, use_symbolic, args[0]))
            elif not args:
                line.append(f2.format(predicate, fn_sig))
            else:
                line.append(f3.format(predicate, fn_sig, ', '.join([str(a) for a in args])))
                # line.append(f3.format(predicate, fn_sig, ', '.join(args)))
        else:
            line.append(element)

    return ''.join(line)


def make_assert_stmt(stub, fn_name, args=None, just_result=False):

    indent: int = 0

    # TODO: 2 & 3 are the same!
    f1 = 'assert {} {} {}'              # w/ symbol             result < 4
    f2 = 'assert {}({}, {})'            # pd( fn(arg), value)
    f3 = 'assert {}({}, {})'            # w/ function
    f4 = 'assert {}({})'                # ignoring True

    # deal with no function, just acting on the predicates
    if fn_name == '_':
        fn_sig = args
    else:
        fn_sig = '{}({})'.format(fn_name, args) if not just_result else fn_name

    indent += 1
    line = ''

    # find
    if (stub['kind'].startswith('predicate')) and (stub.get('predicate', '') not in PREDICATES):
        # raise FalconError(f'Predicate "{stub["predicate"]}" not found. Treating a "raw" predicate.')
        warnings.warn(f'Predicate "{stub["predicate"]}" not found. Treating a "raw" predicate.')

    use_symbolic = False
    error_type = False

    # TODO: refactor to this. Returns a namedtuple -> name, symbol, is_error, is_group
    # predicate = PREDICATES[stub['predicate']]
    # has_values = ...

    if stub['kind'].startswith('predicate') and stub['predicate'] in PREDICATES:
        # get the symbolic name if there is one, otherwise the function name

        if PREDICATES[stub['predicate']][1]:
            pd_name = PREDICATES[stub['predicate']][1]
            use_symbolic = True
        else:
            pd_name = PREDICATES[stub['predicate']][0]
            use_symbolic = False
    elif stub['kind'].startswith('predicate'):
        pd_name = PREDICATES[stub['predicate']][0]
    elif stub.get('predicate', False):
        # TODO: Does not handle symbolic tests!!!
        pd_name = PREDICATES[stub['predicate']][0]
    elif stub['kind'] in ('code', 'logical', 'assert-logical'):
        # These are the exception to the rule...
        pd_name = ''
    else:
        # raise FalconError(f"Predicate {stub['predicate']} not found")
        warnings.warn(f"Predicate {stub['predicate']} not found.")
        pd_name = stub['predicate']

    if stub['kind'] == 'predicate-value':
        if PREDICATES[stub['predicate']].is_error and not just_result:
            # it's an error
            line = f'assert {pd_name}({fn_name}, {args}, {stub["value"]})'
        elif PREDICATES[stub['predicate']].is_error and isinstance(stub["value"], tuple):
            line = f2.format(pd_name, 'result', ','.join(stub["value"]))
        elif PREDICATES[stub['predicate']].is_error:
            line = f4.format(pd_name, 'result')
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
    elif stub['kind'] == 'logical' or stub['kind'] == 'assert-logical':
        line = 'assert ' + make_boolean(stub['values'], fn_sig)
    elif stub['kind'] == 'code':
        line = stub['value']
    elif stub['kind'] == 'predicate-side-effect':
        line = f4.format(pd_name, stub['name'])
    elif stub['kind'] == 'predicate-side-effect+':
        args = ', '.join(stub['values'])
        line = f3.format(pd_name, stub['name'], args)
    elif stub['kind'] == 'predicate-fail-side-effect+':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f2.format(pd_name, fn_sig, ', '.join(stub['value']))
    elif stub['kind'] == 'predicate-fail-side-effect':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 2) * TAB) + f4.format(pd_name, fn_sig)
    elif stub['kind'] == 'assert-error+':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f2.format(pd_name, fn_sig, ', '.join(stub['value'][1:]))
    elif stub['kind'] == 'assert-error':
        e = 'Exception' if stub["error"] is None else stub['error']
        line = f'with pytest.raises({e}):\n' + ((indent + 1) * TAB) + f4.format(pd_name, fn_sig)

    # TODO: 'message' should be in all the stubs, eventually
    if 'error-message' in stub and stub['error-message'] is not None:
        line += f", {stub['error-message']}"

    return line


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


def get_directives(entry):

    # supported:
    # message, pyfunc, suffix, method (of enumeration), labels, only (groupby/winnow), algorithm, & algo-params

    directives = {}

    # directives --------

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

    # *** get the only args
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
        t_name = entry['directives'][':test-name']['value']
        directives['pyfunc'] = f'def {t_name}():'
    elif entry['directives'].get(':name', False):
        t_name = entry['directives'][':name']['value']
        directives['pyfunc'] = f'def {t_name}():' if t_name.startswith('test') else f'def test_{t_name}():'
    else:
        rand_name = ''.join((choices(ascii_letters+digits, k=randint(2, 5))))
        # fname = entry['directives'][':name']['value'] if entry['directives'].get(':name', False) else ''
        directives['pyfunc'] = f"def test_{fn_name}_{rand_name}():"
    # *** get suffix ***
    # looks for :no-suffix or :suffix <blank> or :suffix '' or :suffix '_i'
    if entry['directives'].get(':no-suffix', False):
        suffix = ''
    elif entry['directives'].get(':suffix', False):
        value = entry['directives'][':suffix']['value']
        suffix = value if (value is not None) else ''
    else:
        suffix = 'ᵢ'

    # *** get labels, ie, for <labels> in …: ***
    # that is, the labels of the domains used inside the loop

    # get the variable names
    dvars = entry['domain']                                         # the domain names

    if entry['directives'].get(':labels', False):
        # TODO: input must be a list - how to catch bad input?
        lbs = to_list(entry['directives'][':labels']['value'])
        directives['labels'] = [d.lower() + suffix for d in lbs]
    else:
        directives['labels'] = [d.lower() + suffix for d in dvars]                # the name of the values in the domain                                   # the domain names

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
            raise f"Directive :method not found {algo}"

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

    if entry['directives'].get(':object-update', False):
        directives['object-update'] = True
    else:
        directives['object-update'] = False

    return directives

# groupby tools ---------------------------------

# need:
#   make_test_assert, make_groupby_assert, make_satisfy_assert, make_assert_assert

def make_satisfy_assert(kind, predicate , error=None):
    pass

def get_predicate(stub, by_group=False):

    predicate, values = None, None

    # name
    if not by_group:
        if name := stub.get('predicate', False):
            predicate = PREDICATES.get(name, None)
    elif by_group:
        if name := stub.get('group-predicate', False):
            predicate = PREDICATES.get(name, None)

    # values
    if not by_group:
        if stub.get('value', False):
            values = stub['value']
        elif stub.get('values', False):
            values = stub['values']
    elif by_group:
        if stub.get('group-values', False):
            values = stub['group-values']
        elif stub.get('groupby-many-with-group', False):
            values = stub['groupby-many-with-group']

    return predicate, values


