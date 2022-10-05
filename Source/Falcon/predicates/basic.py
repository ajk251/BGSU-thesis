
import operator as op

from time import process_time_ns

from Falcon.predicates.predicates import predicate, on_fail_false

# simple list, comes from:  https://docs.python.org/3/library/exceptions.html


# -----------------------------------------------

# identity/constant functions
@predicate(alias=['always-true', 'true!'])
def always_true(*args) -> bool:
    """Returns True"""
    return True

@predicate(alias=['always-false', 'false!'])
def always_true(*args) -> bool:
    """Returns False"""
    return False

# -----------------------------------------------

@predicate(alias=['finishes-ms?'], is_error=True)
def finishes_in_lt_ms(fn, args, ms):
    """Measures the amount of time it takes to execute <= ms"""

    start = process_time_ns()
    fn(*args)
    end = process_time_ns()

    return ((end - start) / 1_000_000) <= ms


# These are useful in Test ----------------------
# use error for these

@predicate(alias=['error-and-says?'], is_error=True)
@on_fail_false
def is_error_and_says(fn, args, error_type, message) -> bool:
    """
    Tests that the error is of the specific type and the error message is the same or
    contained in the error message.
    """

    is_error = False

    try:
        result = fn(*args)
    except Exception as err:
        result = err
        is_error = True

    if not is_error:
        return False

    # outcome = isinstance(result, error_type) and message in result.args[0]
    # result &= result.args[0] == message or message in result.args[0]

    return isinstance(result, error_type) and message in result.args[0]


@predicate(alias=['error?'], is_error=True)
@on_fail_false
def is_error(fn, args, error_type) -> bool:
    """Tests that the error is an instance of the specified type"""

    try:
        fn(*args)
    except Exception as error:
        outcome = error

    return isinstance(outcome, error_type)


# TODO: have to rework these...

# @predicate(alias=['error?', 'is-error?'], is_error=True)
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
# @predicate(alias=['error-message?', 'error-says?'], is_error=True)
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


# -----------------------------------------------
# these are define for use in Satisfy/Groupby ---
# they trap in try/except block & use result

# uses raises for these

@predicate(alias=['raises?'])
@on_fail_false
def raises_error(error, error_type=None) -> bool:
    """Tests that the error is an Exception"""
    return isinstance(error, Exception) or isinstance(error, error_type)


@predicate(alias=['asserts?'])
@on_fail_false
def raises_assertion_error(error) -> bool:
    return isinstance(error, AssertionError)


@predicate(alias=['raises-and-says?', 'raises&says?'])
@on_fail_false
def is_error_and_contains(error, message) -> bool:
    """
    Tests that the error is an Exception and the message is the error message or the message
    is contained in the error message.
    """
    return isinstance(error, Exception) and message in error.args[0]


# useful -----------------------------------------

@predicate(alias=['instance?', 'is?', '≡'], doc_error=True)
def is_instance(value, result) -> bool:
    """The value is not the instance specified"""
    return isinstance(result, value)


@predicate(alias=['is-a?'], doc_error=True)
def is_a(kind, *value) -> bool:
    """The value is not any of instances specified"""
    return isinstance(kind, value)


@predicate(alias=['isnt?'])
def is_not(kind, result) -> bool:
    """Tests that the value is not of instance kind"""
    return not isinstance(result, kind)


@predicate(alias=['is-not?', 'is-not-instance?', '≢'])
def is_not_instance_of(kind, *value) -> bool:
    return not isinstance(kind, value)


@predicate(alias=['same-as?'], doc_error=True)
def same_instance(value_a, value_b) -> bool:
    """The value must be the same instance"""
    return id(value_a) == id(value_b)


@predicate(alias=['in', 'in?', '∋', '∍'], symbol='in', doc_error=True)
def is_in(value, container) -> bool:
    """The value must in the sequence"""
    return op.contains(container, value)


@predicate(alias=['!in', '¬in', '∌'], symbol='not in', doc_error=True)
def not_in(value, container) -> bool:
    """The value must not be in the sequence"""
    return not op.contains(container, value)

# compare ---------------------------------------


@predicate(alias=['=', 'eq?'], symbol='==')
def eq(a, b) -> bool:
    """Weak equality, ie a = b"""
    return op.eq(a, b)


@predicate(alias=['==', 'equals?'])
def equals(a, b) -> bool:
    """Strong equality, ie a == b, where type(a) == type(b) and a == b"""
    return type(a) == type(b) and a == b


@predicate(alias=['===', 'strong-equals?'])
def strong_equals(a, b) -> bool:
    """The strongest notion of equality, not the same object, where type(a) == type(b) and a == b"""
    return id(a) != id(b) and type(a) == type(b) and a == b


@predicate(alias=['!=', '≠', 'ne?'], symbol='!=')
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

# special cases ----------------------------------


@predicate(alias=['not-lt?', '≮'])
def not_lt(a, b) -> bool:
    """Value a ≮ b"""
    return not (a < b)


@predicate(alias=['not-gt?', '≯'])
def not_gt(a, b) -> bool:
    """Value a ≯ b"""
    return not (a > b)


@predicate(alias=['not-le?', '≰'])
def not_le(a, b) -> bool:
    """Value a ≰ b"""
    return not (a <= b)


@predicate(alias=['not-ge?', '≱'])
def not_ge(a, b) -> bool:
    """Value a ≱ b"""
    return not (a >= b)

