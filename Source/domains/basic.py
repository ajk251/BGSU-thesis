
from itertools import count
from random import randrange, randint, random, uniform

from domains.domains import domain


# Todo:
#   • discrete
#   • empirical
#   • repeat
#   • numerical
#   • change nrnandom to number
#   • create RealRange/IntRange

@domain(alias=['ℝ', 'Reals', 'Floats'])
def Reals(lower=None, upper=None, nrandom=None, by=None):

    do_random = False if nrandom is None else True
    n_random = 100_000_000 if nrandom is None else int(nrandom)
    by = 1.0 if by is None else float(by)

    # make this system.min & max
    lower = -100.0 if lower is None else float(lower)
    upper = 100.0 if upper is None else float(upper)

    if do_random:
        n = 0
        while True:
            yield randrange(lower, upper)
            n += 1
            if n >= n_random: break
    else:
        n = 0
        while True:
            yield count(lower, by)
            n  += 1
            if n >= upper: break

    return


@domain(alias=['ℤ+', 'Naturals', 'Nats'])
def Naturals(lower=None, upper=None, nrandom=None, by=None):

    # TODO: enforce >= 0‽

    lower = 0 if lower is None else int(lower)
    upper = 100 if upper is None else int(upper)

    do_random = False if nrandom is None else True
    n_random = 100_000_000 if nrandom is None else int(nrandom)
    by = 1 if by is None else int(by)

    n = 0

    if do_random:

        while True:
            yield randint(lower, upper)
            n += 1
            if n >= n_random: break

    else:
        yield from range(lower, upper, by)


@domain(alias=['ℤ', 'Integers', 'Ints'])
def Integers(lower=None, upper=None, nrandom=None, by=None):

    lower = 0 if lower is None else int(lower)
    upper = 100 if upper is None else int(upper)

    do_random = False if nrandom is None else True
    n_random = 100_000_000 if nrandom is None else int(nrandom)
    by = 1 if by is None else int(by)

    n = 0

    if do_random:

        while True:
            yield randint(lower, upper)
            n += 1
            if n >= n_random: break

    else:
        yield from range(lower, upper, by)


# other kinds that might be useful --------------

# numbers - floats & ints
@domain(alias='Numbers')
def Numbers(lower=None, upper=None, pct_floats: float = 0.5, nrandom: int = 1000):

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    n = 0

    while n < nrandom:
        yield uniform(lower, upper) if random() < pct_floats else randint(lower, upper)
        n += 1


@domain(alias=['Integer-Boundary', 'Int-Boundary'])
def Integer_Boundary(lower: int = None, upper: int = None, epsilon: int = 5, values=10, nrandom: int = 100):

    assert values * 2 <= nrandom, "The number of points at the boundary cannot be greater than the total points"

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    # left boundary
    for _ in range(values):
        yield randint(lower - epsilon, lower + epsilon)

    # right
    for _ in range(values):
        yield randint(upper - epsilon, upper + epsilon)

    # middle
    for _ in range(nrandom - 2 * values):
        yield randint(lower, upper)


@domain(alias=['Boundary', 'Real-Boundary', 'Float-Boundary'])
def Boundary(lower=None, upper=None, epsilon=5.0, values: int = 10, nrandom: int = 100):

    assert values * 2 <= nrandom, "The number of points at the boundary cannot be greater than the total points"

    lower = -1_000_000 if lower is None else lower
    upper = 1_000_000 if upper is None else upper

    # left boundary
    for _ in range(values):
        yield uniform(lower - epsilon, lower + epsilon)

    # right
    for _ in range(values):
        yield uniform(upper - epsilon, upper + epsilon)

    # middle
    for _ in range(nrandom - (2 * values)):
        yield uniform(lower, upper)
