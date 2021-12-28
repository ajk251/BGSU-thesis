
import operator as op



from predicates.predicates import predicate


# useful -----------------------------------------

@predicate(alias=['catches', 'raises', 'raises?'], is_error=True)
def raises(fn, args, kwargs, error) -> bool:

    try:
        fn(*args, **kwargs)
    except Exception as e:
        return isinstance(e, Exception)
    finally:
        return False


@predicate(alias=['is_assertion', 'is-assertion', 'is-assertion?'], is_error=True)
def assertion(fn, args, kwargs, error=AssertionError):

    try:
        fn(*args, **kwargs)
    except AssertionError as ae:
        return isinstance(ae, AssertionError)
    finally:
        return False

# basic -----------------------------------------


@predicate(alias=['is-None?', 'None?', 'none?'])
def is_none(value) -> bool:
    return value is None


@predicate(alias=['is-a?'])
def is_a(kind, value) -> bool:
    return isinstance(kind, value)


@predicate(alias=['same-as?'])
def same_instance(value_a, value_b) -> bool:
    return id(value_a) == id(value_b)


@predicate(alias=['in', 'in?', '∋', '∍'], symbol='in')
def is_in(value, container) -> bool:
    return op.contains(container, value)


@predicate(alias=['!in', '¬in', '∌'], symbol='not in')
def not_in(value, container) -> bool:
    return not op.contains(container, value)

# compare ---------------------------------------


@predicate(alias=['=', 'eq?'], symbol='==')
def eq(a, b) -> bool:
    return op.eq(a, b)


@predicate(alias=['!=', '¬=', '≠', 'ne?'], symbol='!=')
def ne(a, b) -> bool:
    return op.ne(a, b)


@predicate(alias=['<', 'lt?'], symbol='<')
def lt(a, b) -> bool:
    return op.lt(a, b)


@predicate(alias=['>', 'gt?'], symbol='>')
def gt(a, b) -> bool:
    return op.gt(a, b)


@predicate(alias=['<=', '≤', 'le?'], symbol='<=')
def le(a, b) -> bool:
    return op.le(a, b)


@predicate(alias=['>=', '≥', 'ge?'], symbol='>=')
def ge(a, b) -> bool:
    return op.ge(a, b)
