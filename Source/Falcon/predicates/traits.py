
from Falcon.predicates import predicate

# NOTE: This is experimental. I'm not sure if it makes sense.

# help from:
#   https://rszalski.github.io/magicmethods/

#   https://eli.thegreenplace.net/2018/partial-and-total-orders/
#   https://codereview.stackexchange.com/questions/152460/determining-if-a-relation-is-reflexive
#   https://stackoverflow.com/questions/43153333/python-relations-with-sets-of-tuples

def _dunderify(name):
    return '__' + name + '__'

# all of
_COMPARISON = tuple(map(_dunderify, ('eq', 'ne', 'lt', 'gt', 'le', 'ge')))
_NUMERICAL   = tuple(map(_dunderify, ('add', 'sub', 'mul', 'div')))
_BOOLEAN     = tuple(map(_dunderify, ('and', 'or', 'xor')))
_CONTEXTABLE = tuple(map(_dunderify, ('enter', 'exit')))
_PRINTABLE   = tuple(map(_dunderify, ('str', 'repr')))

satisfy_all = (_COMPARISON, _NUMERICAL, _BOOLEAN)

# from EOP
# regular     = ('init', 'copy')

# any of
_PRINTABLE   = tuple(map(_dunderify, ('str', 'repr')))
_CALLABLE_   = tuple(map(_dunderify, ('call')))
_CONTEXTABLE = tuple(map(_dunderify, ('enter')))
_COPYABLE    = tuple(map(_dunderify, ('copy', 'deepcopy')))

satisfy_any = (_PRINTABLE, _COPYABLE, _CONTEXTABLE, _COPYABLE)

# -----------------------------------------------


@predicate(alias=['is-of?', 'trait?'])
def has_trait(obj, trait) -> bool:

    if trait in satisfy_any:
        return any(map(lambda t: hasattr(obj, t), satisfy_any))
    elif trait in satisfy_all:
        return all(map(lambda t: hasattr(obj, t), satisfy_all))

    return False

# These require more thought and justification

@predicate(alias=['is-comparable?'])
def is_comparable(obj) -> bool:
    """Tests that an object implements the operators: 'eq', 'ne', 'lt', 'gt', 'le', 'ge'"""
    return all(map(lambda t: hasattr(object, t), _COMPARISON))


@predicate(alias=['is-numerical?'])
def is_numerical(obj) -> bool:
    """Test that an object implements the operators: 'add', 'sub', 'mul', 'div'"""
    return all(map(lambda t: hasattr(obj, t), _NUMERICAL))


@predicate(alias=['is-printable?'])
def is_printable(obj) -> bool:
    """Tests that an object is representable or printable, having either repr or str implemented."""
    return any(map(lambda t: hasattr(obj, t), satisfy_any))
