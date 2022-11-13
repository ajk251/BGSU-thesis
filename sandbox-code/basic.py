
from itertools import combinations, count, product
from random import choice, randrange, randint, random, uniform
from typing import Any, Iterator, Tuple, Union

# from domains.domains import domain


Number = Union[int, float]

# Note:
#   - numpy as linspace, geospace, logspace


# linear ranges -------------------------------------------

def real_range(lower: float=0.0, upper: float = 100.00, step: float=1.0) -> Iterator[float]:
    """Produce a linear sequence of floats from the lower bound to the upper bound, non-inclusive"""

    lower = float(lower)
    upper = float(upper)

    c = count(start=lower, step=step)
    n = next(c)

    while n < upper:
        yield n
        n = next(c)


def integer_range(lower: int = 1, upper: int = 1_000_000, step: int = 1) -> Iterator[int]:
    """Produce a linear sequence of ints from the lower bound to the upper bound, non-inclusive"""

    lower = int(lower)
    upper = int(upper)

    c = count(start=lower, step=step)
    n = next(c)

    while n < upper:
        yield n
        n = next(c)


# randomized ----------------------------------------------

def reals(lower: float=0.0, upper: float = 100.00, n: int = 100) -> Iterator[float]:
    """Produces n random floats"""

    lower = float(lower)
    upper = float(upper)

    i = 0

    while i < n:
        yield uniform(lower, upper)
        i += 1


def integers(lower: int=0, upper: int = 100, n: int = 100) -> Iterator[int]:
    """Produces n random integers"""

    lower = int(lower)
    upper = int(upper)

    i = 0

    while i < n:
        yield randrange(lower, upper)
        i += 1


def numbers(lower: Number = -1, upper: Number = 1, pct_floats: float = 0.5, nrandom: int = 1000) -> Iterator[Number]:
    """Produces n random integers or floats"""

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    n = 0

    while n < nrandom:
        yield uniform(lower, upper) if random() < pct_floats else randint(lower, upper)
        n += 1


# special

def int_boundary(lower: int = -1, upper: int = 1, epsilon: int = 5, bdry_values: int = 10, n: int = 100) -> Iterator[int]:
    """Produces n values in total, bdry_values in [lower-epsilon, lower], bdry_values in [lower, upper], and bdry_values in [upper, upper+epsilon]"""

    assert bdry_values * 2 <= n, "The number of points at the boundary cannot be greater than the total points"

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    # left boundary
    for _ in range(bdry_values):
        yield randint(lower - epsilon, lower + epsilon)

    # right
    for _ in range(bdry_values):
        yield randint(upper - epsilon, upper + epsilon)

    # middle
    for _ in range(n - 2 * bdry_values):
        yield randint(lower, upper)   


def boundary(lower: float = -1.0, upper: float = 1.0, epsilon: float = 5.0, bdry_values: int = 10, n: int = 100) -> Iterator[float]:
    """Produces n values in total, bdry_values in [lower-epsilon, lower], bdry_values in [lower, upper], and bdry_values in [upper, upper+epsilon]"""

    assert bdry_values * 2 <= n, "The number of points at the boundary cannot be greater than the total points"

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    # left boundary
    for _ in range(bdry_values):
        yield uniform(lower - epsilon, lower)

    # middle
    for _ in range(n - 2 * bdry_values):
        yield uniform(lower, upper)

    # right
    for _ in range(bdry_values):
        yield uniform(upper, upper + epsilon)

  
# combinatorial -------------------------------------------

def cartesian(sequences) -> Iterator[Tuple[Any, ...]]:
    return product(*sequences)


def permutations_of(sequence, repeat: int = 2) -> Iterator[Tuple[Any, ...]]:
    return (s for s in product(sequence, repeat=repeat))


def twise_combination(sequences, tway: int = 3) -> Iterator[Tuple[Any, ...]]:
    """
    Generates t-wise combinations of sequences, without unnecessary values. Like IPOG, but more clear and practical, though less efficient.
    Builds t-wise tuples, then randomly assigns missing values, ie non-deterministic. Holds intermediate values.
    """

    take_rand = lambda i: (choice(sequences[i]), )

    N: int = len(sequences)
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

            answer: Tuple = tuple()

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



# -------------------------------------------------------------

for n in real_range(0, 1, 0.1):
    print(n)

for n_ in integer_range(0, 5, 1):
    print(n_)

print('-' * 25)

r = reals(-10.0, 10, 20)

for n in r:
    print(n)

for n in integers(-100, 100, 10):
    print(n)

for n in numbers(-10, 10, 0.25, 10):
    print(n)

for n in int_boundary(-10, 10, 5, 4, 12):
    print(n)

for n in boundary(-10, 10, 2.0, 4, 12):
    print(n)

for s in permutations_of([1,2,3,4], 3):
    print(s)

print('-' *  24)

for s in cartesian([[1, 2, 3], ['a', 'b', 'c'], ['*', '.', '!']]):
    print(s)

print('twise')

for s in twise_combination([[1, 2, 3], ['a', 'b', 'c'], ['*', '.', '!']], 2):
    print(s)