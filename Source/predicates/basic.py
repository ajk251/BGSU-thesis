
import operator as op



from predicates.predicates import predicate

# basic -----------------------------------------


@predicate(alias=['is-a?'])
def is_a(kind, value) -> bool:
    return isinstance(kind, value)


@predicate(alias=['same-as?'])
def same_instance(value_a, value_b) -> bool:
    return id(value_a) == id(value_b)


@predicate(alias=['in', 'in?', '∋', '∍'], symbolic='in')
def is_in(value, container) -> bool:
    return op.contains(container, value)


@predicate(alias=['!in', '¬in', '∌'], symbolic='not in')
def not_in(value, container) -> bool:
    return not op.contains(container, value)

# compare ---------------------------------------


@predicate(alias=['=', 'eq?'], symbolic='==')
def eq(a, b) -> bool:
    return op.eq(a, b)


@predicate(alias=['!=', '¬=', '≠', 'ne?'], symbolic='!=')
def ne(a, b) -> bool:
    return op.ne(a, b)


@predicate(alias=['<', 'lt?'], symbolic='<')
def lt(a, b) -> bool:
    return op.lt(a, b)


@predicate(alias=['>', 'gt?'], symbolic='>')
def gt(a, b) -> bool:
    return op.gt(a, b)


@predicate(alias=['<=', '≤', 'le?'], symbolic='<=')
def le(a, b) -> bool:
    return op.le(a, b)


@predicate(alias=['>=', '≥', 'ge?'], symbolic='>=')
def ge(a, b) -> bool:
    return op.ge(a, b)


