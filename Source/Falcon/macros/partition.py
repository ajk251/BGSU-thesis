
from Falcon.macros.macros import macro
from Falcon.writers.tools import *

TAB = '    '

@macro(name='Partition')
def partition(fixture):

    # TODO:
    #   message
    #   what directives...
    #   min_cases?

    indent: int = 0
    lines = ['']

    directives = get_directives(fixture, 'partition')

    # message = directives['message']
    pyfunc = directives['pyfunc']
    dvars = fixture['domain']                                         # the domain names
    labels = directives['labels']
    algo = directives['algo']
    params = directives['params']
    fn_name = directives['fn_name']
    followup = directives['follow-up']
    save_results = directives['save-results']                 # if one is a group, it must be true
    save_cases = directives['save-cases']
    use_error_msg = directives['no-error-message']

    args = ', '.join(labels)
    fn_sig = '{}({})'.format(fn_name, args)

    # the def name
    lines.extend((f'{pyfunc}', ''))


    w2 = '''
try:
    result = {}
except Exception as e:
    result = e
'''

    indent += 1

    if save_cases:
        line = (indent * TAB) + 'cases = defaultdict(list)'
        lines.append(line)

    if save_results:
        line = (indent * TAB) + 'results = defaultdict(list)'
        lines.append(line)

    # this is for min cases
    # line = f"{indent * TAB}n_cases = defaultdict(int)\n"
    # lines.append(line)

    # build the for loop, naked/with custom iterator/generic & no parameters
    if len(labels) == 1:
        template = indent * TAB + "for {} in {}:".format(labels[0], dvars[0])
    elif len(params) > 0:
        template = indent * TAB + 'for {} in {}({}, {}):'.format(', '.join(labels), algo, ', '.join(dvars), ', '.join(params))
    elif len(labels) > 1 and len(dvars) == 1:
        # ie: n-labels, but 1 domain
        template = indent * TAB + "for {} in {}:".format(', '.join(labels), dvars[0])
    else:
        template = indent * TAB + "for {} in {}({}):".format(', '.join(labels), algo, ', '.join(dvars))

    lines.append(template)

    # have to avoid calling get_predicate because of name issues
    # have to get 2 predicates & 2 values

    # partition predicate
    if PREDICATES.get(fixture['predicate'], False):
        predicate = PREDICATES[fixture['predicate']]
    else:
        predicate = Predicate(fixture['predicate'], None, False, False, False, False)
        warnings.warn(f"Predicate '{predicate.name}' was not defined.")

    # test predicate
    if PREDICATES.get(fixture['test-predicate'], False):
        predicate = PREDICATES[fixture['test-predicate']]
    else:
        predicate = Predicate(fixture['test-predicate'], None, False, False, False, False)
        warnings.warn(f"Predicate '{predicate.name}' was not defined.")

    cond = 'if'

    for property in fixture['stubs']:

        # code
        # symbolic ...
        if property['kind'] == 'predicate-partition':
            line = (indent * TAB) + f"{cond} {predicate.name}({', '.join(labels)}:"

    # TODO: not all cases are here
    if followup and save_cases and save_results:
        line = f'\n{indent * TAB}{followup}(cases, results)'
        lines.append(line)
    elif followup and save_results:
        line = f'\n{indent * TAB}{followup}(results)'
        lines.append(line)
    elif followup and save_cases:
        line = f'\n{indent * TAB}{followup}(cases)'
        lines.append(line)

    lines.append('')

    return '\n'.join(lines)
