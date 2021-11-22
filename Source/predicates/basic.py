
import operator as op



from predicates.predicates import predicate

# basic -----------------------------------------


@predicate(alias=['in', 'in?', '∋', '∍'], symbolic='in')
def is_in(value, container) -> bool:
    return op.contains(container, value)


@predicate(alias=['!in', '¬in', '∌'], symbolic='not in')
def not_in(value, container) -> bool:
    return not op.contains(container, value)

# compare ---------------------------------------


@predicate(alias=['='], symbolic='==')
def eq(a, b) -> bool:
    return op.eq(a, b)


@predicate(alias=['!=', '¬=', '≠'], symbolic='!=')
def ne(a, b) -> bool:
    return op.ne(a, b)


@predicate(alias='<', symbolic='<')
def lt(a, b) -> bool:
    return op.lt(a, b)


@predicate(alias='>', symbolic='>')
def gt(a, b) -> bool:
    return op.gt(a, b)


@predicate(alias=['<=', '≤'], symbolic='<=')
def le(a, b) -> bool:
    return op.le(a, b)


@predicate(alias=['>=', '≥'], symbolic='>=')
def ge(a, b) -> bool:
    return op.ge(a, b)


