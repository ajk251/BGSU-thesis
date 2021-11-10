

from itertools import count

from more_itertools import numeric_range


# ---------------------------------------------------------

def reals(lower, upper, step):

    for n in count(lower, step):
        yield n

        if n >= upper: break

def integers(lower, upper, step):

    for n in range(lower, upper, step):
        yield n

def numeric(lower, upper, step):

    for n in numeric_range(lower, upper, step):
        yield n

# ---------------------------------------------------------





# ---------------------------------------------------------

def composite(*domains):

    for ds in domains:
        yield ds


# ---------------------------------------------------------

r = reals(0, 1, 0.02)
i = integers(0, 10, 2)

for n in r:
    print(n)

for n in reals(-1, 1, 0.5):
    print(n)

for n in i:
    print(n)

for ds in composite(reals(0, 1, 0.3), reals(0, 1, 0.3)):
    d = tuple(d for d in ds)
    print(d)