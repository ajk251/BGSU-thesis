
def call(fn, *args, **kwargs):
    """Wraps the function in a try/except block. Returns the result of the function call or the error."""

    try:
        value = fn(*args, **kwargs)
    except Exception as error:
        value = error

    return value

