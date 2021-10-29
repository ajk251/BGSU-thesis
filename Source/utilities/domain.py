

from random import randint, randrange


# ---------------------------------------------------------

def enumerate_integers(lb : int, ub : int, step=1) -> int:
    yield from range(lb, ub, step)


def enumerate_reals(lb, ub, step=1.0):

    r = lb

    while True:

        yield r
        r += step

        if r >= ub: break

# ---------------------------------

def random_integers(lb, ub):
    
    while True:
        yield randint(lb, ub)

def random_reals(lb, ub):

    while True:
        yield randrange(lb, ub)

# ---------------------------------



I = enumerate_integers(1, 15, 1)
R = enumerate_reals(1.0, 10.0, 0.5)

for i in range(10):
    print(next(I))

for i in range(10):
    print(next(R))