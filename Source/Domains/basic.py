
from itertools import count
from random import randrange, randint

from Domains.domains import domain


@domain(alias=['ℝ', 'Floats'])
def Reals(lower=None, upper=None, n_random=None, by=None):

    do_random = False if n_random is None else True
    n_random = 100_000_000 if n_random is None else int(n_random)
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
def Naturals(lower=None, upper=None, n_random=None, by=None):

    # TODO: enforce >= 0‽

    lower = 0 if lower is None else int(lower)
    upper = 100 if upper is None else int(upper)

    do_random = False if n_random is None else True
    n_random = 100_000_000 if n_random is None else int(n_random)
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
def Integers(lower=None, upper=None, n_random=None, by=None):

    lower = 0 if lower is None else int(lower)
    upper = 100 if upper is None else int(upper)

    do_random = False if n_random is None else True
    n_random = 100_000_000 if n_random is None else int(n_random)
    by = 1 if by is None else int(by)

    n = 0

    if do_random:

        while True:
            yield randint(lower, upper)
            n += 1
            if n >= n_random: break

    else:
        yield from range(lower, upper, by)


