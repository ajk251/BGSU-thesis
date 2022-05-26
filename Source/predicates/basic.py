
import operator as op

from predicates.predicates import predicate


# useful -----------------------------------------

# simple list, comes from:  https://docs.python.org/3/library/exceptions.html

@predicate(alias=['error?', 'raises?'], is_error=True)
def catch_error(error, error_kind) -> bool:
    return isinstance(error, error_kind)


@predicate(alias=['error-message?', 'error-says?', 'raises-with-message?', 'raises-message?'], is_error=True)
def catch_error_message(error, error_kind, message):
    return isinstance(error, error_kind) and message in error.args[0]


@predicate(alias='zero-error?', is_error=True)
def catch_zero_div(error) -> bool:
    return isinstance(error, ZeroDivisionError)


@predicate(alias=['asserts?', 'is-assertion?'], is_error=True)
def catch_assertion(error) -> bool:
    return isinstance(error, AssertionError)


@predicate(alias='math-error?', is_error=True)
def catch_arithmetic(error) -> bool:
    return isinstance(error, ArithmeticError)


@predicate(alias='lookup-error?', is_error=True)
def catch_lookup(error) -> bool:
    return isinstance(error, LookupError)


# @predicate(alias=['raises?'], is_error=True)
# def raises(e, error) -> bool:
#
#     # try:
#     #     fn(*args, **kwargs)
#     # except Exception as e:
#     #     return isinstance(e, Exception)
#     # finally:
#     #     return False
#     return e is error
#
#
# # Be careful with this, you can't test for an AssertionError like in raises? --> it must be an instance of the
# #   error
# @predicate(alias=['asserts?', 'is_assertion', 'is-assertion', 'is-assertion?'], is_error=True)
# def assertion(fn, args, kwargs, error=AssertionError):
#
#     try:
#         fn(*args, **kwargs)
#     except AssertionError as ae:
#         return isinstance(ae, AssertionError)
#     finally:
#         return False

# basic -----------------------------------------


@predicate(alias=['is-None?', 'is-none?', 'None?', 'none?'])
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
    """Weak equality, ie a = b, and does not check for types. For instance, 1 = 1.0"""
    return op.eq(a, b)


@predicate(alias=['==', 'equals?'])
def equals(a, b) -> bool:
    """Strong equality, ie a == b, where type(a) == type(b) and a == b"""
    return type(a) == type(b) and a == b


@predicate(alias=['===', 'strong-equals?'])
def strong_equals(a, b) -> bool:
    """The strongest notion of equality, not the same object, where type(a) == type(b) and a == b"""
    return id(a) != id(b) and type(a) == type(b) and a == b


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

# search --------------------------------------------------

@predicate(alias=['sorted?', 'sorted≤?', 'sorted<=?'])
def is_sorted(sequence) -> bool:
    """Tests i≤j for all values in sequence"""
    return all((i <= j for i, j in zip(sequence, sequence[1:])))


@predicate(alias=['sorted<?', 'sorted-strict?'])
def is_strictly_sorted(sequence) -> bool:
    """Tests i<j for all values in sequence"""
    return all((i < j for i, j in zip(sequence, sequence[1:])))


@predicate(alias=['descending?'])
def descending(sequence) -> bool:
    """Tests for decending order, ie 100, 99, 98, …, where i > j"""
    return all((i > j for i, j in zip(sequence, sequence[1:])))


@predicate(alias=['ascending?'])
def ascending(sequence) -> bool:
    """Tests for ascending order, ie 1, 2, 3 …, where i < j"""
    return all((i < j for i, j in zip(sequence, sequence[1:])))
