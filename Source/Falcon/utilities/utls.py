
from functools import wraps

def call(fn, *args, **kwargs):
    """Wraps the function in a try/except block. Returns the result of the function call or the error."""

    try:
        value = fn(*args, **kwargs)
    except Exception as error:
        value = error

    return value

# -----------------------------------------------

def onfail_false(fn) -> bool:
    @wraps(fn)
    def call_fn(*args, **kwargs):
        """Decorates a predicate. If the predicate fails, it returns False"""

        try:
            result = fn(*args, **kwargs)
        except Exception as error:
            result = False

        return result
    return call_fn

# -----------------------------------------------
