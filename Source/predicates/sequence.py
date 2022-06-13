
from predicates.predicates import predicate

# TODO: • This requires better testing!
#       • How to handle tuples in sequences‽ ie *value


@predicate(alias=['all?'], is_group=True)
def is_all(sequence, predicate_fn):
    """Predicate must be True for all values"""
    return all(map(predicate_fn, sequence))


@predicate(alias=['any?'], is_group=True)
def is_any(sequence, predicate_fn):
    """The predicate must be True for 1 or more values"""
    return any(map(predicate_fn, sequence))


@predicate(alias=['most?'], is_group=True)
def is_at_most(sequence, predicate_fn, n: int = 1):
    """The predicate must be True for at most n, or 0 to n values"""
    # tests a sequence where the sequence must be 0 < fn ↦ sequence < n
    # the number true must be less than n
    # note does not handle anything other than single values...

    count: int = 0

    for value in sequence:
        if predicate_fn(value): count += 1
        if count > n: return False

    return True


@predicate(alias=['at-least?'], is_group=True)
def is_at_least_n(sequence, predicate_fn, n: int = 1):
    """The predicate must be True for at least n values or more"""
    # tests fn ↦ sequence < n
    # the number true is greater-or-equal to n
    # note does not handle anything other than single values...

    count: int = 0

    for value in sequence:
        if predicate_fn(value):  count += 1
        if count >= n: return True

    return False


@predicate(alias=['is-exactly?'], is_group=True)
def is_exactly(sequence, predicate_fn, n: int = 1):
    """The predicate must be True for at exactly n values"""

    count: int = 1

    for value in sequence:
        if predicate_fn(value): count += 1
        if count > n: return False

    return True if count == n else False


@predicate(alias=['lone?'], is_group=True)
def lone(sequence, predicate_fn):
    """The predicate must be True for 0 or 1 predicate"""
    # the number true must be 0 or 1

    count: int = 1

    for value in sequence:
        if predicate_fn(value): count += 1
        if count > 1: return False

    return True if count == 0 or count == 1 else False


@predicate(alias=['is-empty?', 'empty?'], is_group=True)
def empty(sequence) -> bool:
    return len(sequence) == 0


@predicate(alias=['not-empty?'], is_group=True)
def not_empty(sequence) -> bool:
    return len(sequence) >= 1
