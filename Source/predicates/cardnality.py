
from predicates.predicates import predicate

# Used to test the cardnality of a sequence, ie #< 4 --> len(sequence) < 4


# these test the cardnality ---------------------

@predicate(alias=['#<', 'card-lt?'])
def cardnality_lt(sequence, n: int) -> bool:
    return len(sequence) < n


@predicate(alias=['#>', 'card-gt?'])
def cardnality_gt(sequence, n: int) -> bool:
    return len(sequence) > n


@predicate(alias=['#<=', '#≤', 'card-le?'])
def cardnality_le(sequence, n: int) -> bool:
    return len(sequence) <= n


@predicate(alias=['#<=', '#≥', 'card-lt?'])
def cardnality_ge(sequence, n: int) -> bool:
    return len(sequence) >= n


@predicate(alias=['#=', '#is', '#eq?', 'card-eq?'])
def cardnality_ge(sequence, n: int) -> bool:
    return len(sequence) == n


@predicate(alias=['#+-', '#±', 'card-pm?'])
def cardnality_plus_minus_n(sequence, n: int, pm: int) -> bool:
    return (n - pm) <= len(sequence) <= (n + pm)


@predicate(alias=['#!=', '#≠0', 'card-not0?'])
def cardnality_ne0(sequence) -> bool:
    return len(sequence) >= 0


@predicate(alias=['#between?', 'card-between?'])
def cardnality_between(sequence, lb: int, ub: int) -> bool:
    """Tests that the length of a sequence is greater-than-or-equal-to lb and less-than-or-equal-to ub, [lb, ub]"""
    return lb <= len(sequence) <= ub


@predicate(alias=['#within', 'card-within?'])
def cardnality_within(sequence, lb: int, ub: int) -> bool:
    """Tests that the length of a sequence is greater-than-or-equal-to lb and less-than ub, [lb, ub)"""
    return lb <= len(sequence) < ub


# these are useful!? --------------------------------------


