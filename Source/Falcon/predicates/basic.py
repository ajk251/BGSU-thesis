
import operator as op

from Falcon.predicates.predicates import predicate, onfail_false


# useful -----------------------------------------

# simple list, comes from:  https://docs.python.org/3/library/exceptions.html


@predicate(alias=['error?'])
@onfail_false
def is_error(error) -> bool:
    """Tests that the error is an Exception"""
    return isinstance(error, Exception)


@predicate(alias=['is-error?', 'raises?'])
@onfail_false
def raises_error(error, error_type) -> bool:
    """Tests that the error is an instance of the specified type"""
    return isinstance(error, Exception) or isinstance(error, error_type)


@predicate(alias=['error-and-says?'])
@onfail_false
def is_error_and_says(error, error_type, message) -> bool:
    """
    Tests that the error is of the specific type and the error message is the same or
    contained in the error message.
    """
    result =  isinstance(error, error_type) or isinstance(error, error_type)
    result &= error.args[0] == message or message in error.args[0]

    return result


@predicate(alias=['error-says?'])
@onfail_false
def is_error_and_contains(error, message) -> bool:
    """
    Tests that the error is an Exception and the message is the error message or the message
    is contained in the error message.
    """
    return (isinstance(error, Exception) or isinstance(error, Exception)) \
           (error.args[0] == message or message in error.args[0])


# must be of the form catches(fn, (args), ...)

# @predicate(alias=['error?', 'raises?'], is_error=True)
# def catch_error(fn, args, exception) -> bool:
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, exception)
#     finally:
#         return result
#
#
# @predicate(alias=['error-message?', 'error-says?', 'raises-with-message?', 'raises-message?'], is_error=True)
# def catch_error_message(fn, args, exception, message):
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, exception)
#     finally:
#         result = message in error.args[0]
#
#     return result
#
#
# @predicate(alias='zero-error?', is_error=True)
# def catch_zero_div(fn, args) -> bool:
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, ZeroDivisionError)
#     finally:
#         return result
#
#
# @predicate(alias=['asserts?', 'is-assertion?'], is_error=True)
# def catch_assertion(fn, args) -> bool:
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, AssertionError)
#     finally:
#         return result
#
#
# @predicate(alias='math-error?', is_error=True)
# def catch_arithmetic(fn, args) -> bool:
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, ArithmeticError)
#     finally:
#         return result
#
#
# @predicate(alias='lookup-error?', is_error=True)
# def catch_lookup(fn, args) -> bool:
#
#     result = False
#
#     try:
#         fn(*args)
#     except Exception as error:
#         result = isinstance(error, LookupError)
#     finally:
#         return result


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


@predicate(alias=['instance?'])
def is_instance(value, result) -> bool:
    # this was done for the triangle example
    return isinstance(result, value)


@predicate(alias=['is-a?'])
def is_a(kind, *value) -> bool:
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

@predicate(alias=['all-unique?'])
def all_unique(sequence) -> bool:
    """Tests that a sequence only contains unique values"""
    return len(frozenset(sequence)) == len(sequence)
