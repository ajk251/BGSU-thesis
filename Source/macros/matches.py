
from macros.macros import macro


@macro(alias=['Matches'])
def matches(entry):
    print('here at macro-matches')
    return ['# not implemented yet']


@macro(alias=['Cases'])
def case_enumerate(entry):
    return ['# not implemented yet']
