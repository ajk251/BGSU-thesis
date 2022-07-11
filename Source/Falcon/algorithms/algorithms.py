
from itertools import chain, combinations, product, tee
from random import choice

ALGORITHMS = {}


def algorithm(_fn=None, *, alias=None):

    def function(func):

        # don't really need the function itself...
        values = func.__name__

        if isinstance(alias, (list, tuple)):
            for name in alias:
                ALGORITHMS[name] = values
        elif alias:
            ALGORITHMS[alias] = values

        ALGORITHMS[func.__name__] = values

        return func

    return function if _fn is None else function(_fn)

# ---------------------------------------------------------


@algorithm(alias=['⨯', 'product', 'cartesian'])
def cartesian_product(*args):
    return product(*args)


@algorithm(alias=['all-pairs', 'all_pairs'])
def all_pairs(*sequences):
    """Generate all pairs from the sequences."""
    # source: https://www.geeksforgeeks.org/python-all-pair-combinations-of-2-tuples/
    return chain(product(*sequences), product(*sequences))


@algorithm(alias=['all-triplets', 'all_triplets'])
def all_triplets(*sequences):
    """Generates all triplets from the sequences"""
    # source: https://www.geeksforgeeks.org/python-all-pair-combinations-of-2-tuples/
    return chain(product(*sequences), product(*sequences), product(*sequences))


@algorithm(alias=['covering', 't-wise', 'twise'])
def twise_combination(*sequences, tway: int = 3):
    """
    Generates t-wise combinations of sequences, without unnecessary values. Like IPOG, but more clear and practical, though less efficient.
    Builds t-wise tuples, then randomly assigns missing values, ie non-deterministic. Holds intermediate values.
    """

    take_rand = lambda i: (choice(sequences[i]), )

    N = len(sequences)
    S = tuple(combinations(range(N), tway))                                    # all the orderings of the sequences
    found = set()                                                              # collection of all the combos found

    # generated = 0
    # repeats = 0

    for s in S:

        missing = set(range(N)).difference(set(s))
        solutions = product(*(sequences[i_] for i_ in s))                       # product of the particular ordering

        for solution in solutions:

            solution = list(solution)
            solution.reverse()

            answer = tuple()

            for j in range(N):                                                  # the solution only contains the t-wise ordering,
                                                                                # not the full answer. Put it together, in order.
                if j in missing:
                    answer += take_rand(j)
                else:
                    answer += (solution.pop(),)

            # generated += 1

            # there is a chance to try different combinations here...
            if answer in found:
                #repeats += 1
                continue                                                        # has it already been found?
            else:
                found.add(answer)

            yield answer


# these take one list, then build the combinations --------

@algorithm(alias=['all-pairs-of', 'all_pairs_of'])
def all_pairs_of(sequence, n: int = 3):
    """Build n-copies of a sequence and generate all pairs."""
    return all_pairs(*(sequence for _ in range(n)))


@algorithm(alias=['all-triplets-of', 'all_triplets_of'])
def all_triplets_of(sequence, n: int = 3):
    """Builds n-copies of a sequence and generates all triplets"""
    return all_triplets(*(sequence for _ in range(n)))


@algorithm(alias=['combs-of', 'all-combinations-of', 'all-orderings-of'])
def combinations_of(sequence, n=3):
    """Builds the cartesian product of n copies of a sequence"""
    return product(*(sequence for _ in range(n)))


@algorithm(alias=['all-perms-of', 'all-permutations-of'])
def all_permutations_of(sequence, repeat: int = 2):
    return (s for s in product(sequence, repeat=repeat))
