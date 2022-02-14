
from predicates.predicates import predicate


@predicate(alias=['#<', 'card-lt?'])
def card_lt(sequence, n: int) -> bool:
    return len(sequence) < n


@predicate(alias=['#>', 'card-gt?'])
def card_gt(sequence, n: int) -> bool:
    return len(sequence) > n


@predicate(alias=['#<=', '#≤', 'card-le?'])
def card_le(sequence, n: int) -> bool:
    return len(sequence) <= n


@predicate(alias=['#<=', '#≥', 'card-lt?'])
def card_ge(sequence, n: int) -> bool:
    return len(sequence) >= n


@predicate(alias=['#+-', '#±', 'card-pm?'])
def card_plus_minus_n(sequence, n: int, pm: int) -> bool:
    return (n - pm) <= len(sequence) <= (n + pm)


@predicate(alias=['#!=', '#≠0', 'card-not0?'])
def card_ne0(sequence) -> bool:
    return len(sequence) >= 0


@predicate(alias=['#between?'])
def card_between(sequence, lb: int, ub: int) -> bool:
    """Tests that the length of a sequence is greater-than-or-equal-to lb and less-than-or-equal-to ub, [lb, ub]"""
    return lb <= len(sequence) <= ub


@predicate(alias=['#within'])
def card_within(sequence, lb: int, ub: int) -> bool:
    """Tests that the length of a sequence is greater-than-or-equal-to lb and less-than ub, [lb, ub)"""
    return lb <= len(sequence) < ub

