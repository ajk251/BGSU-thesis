
from random import choices, random, randint



class TriangleDomain:

    def __init__(self, max_total: int=100, max_nt: int=10, max_eq: int = 10, max_sc: int = 10, max_is: int = 10):

        self.max = max_total
        self.max_nt = max_nt
        self.max_eq = max_eq
        self.max_sc = max_sc
        self.max_is = max_is

        self.n = 1
        self.e = 1
        self.s = 1
        self.i = 1

    def __call__(self, n, e, s, i):

        self.n = n
        self.e = e
        self.s = s
        self.i = i

    def __iter__(self):

        pass


def triangle_domain(n: int=100, max_nt: int=10, max_eq: int = 10, max_sc: int = 10, max_is: int = 10):

    triangles = ['not-triangle', 'equilateral', 'scalene', 'isosceles']
    weights = [max_nt, max_eq, max_sc, max_is]
    n, e, s, i = 1, 1, 1, 1

    n = n if n is not None else 100
    i = 0                               # iteration

    s1 = 0
    s2 = 0
    s3 = 0

    while i <= n:

        kind = choices(triangles, weights, k=1)

        if kind == 'not-triangle':
            s1 = randint(-1, 1)
            s2 = randint(-1, 1)
            s3 = randint(-1, 1)
        elif kind == 'equilateral':
            s = randint(1, 10)
            s1, s2, s3 = s,s,s
        elif kind == 'scalene':
            s1 = randint(1, 10)
            s2 = randint(1, 10)
            s3 = randint(1, 10)
        elif kind == 'isosceles':
            s = randint(1, 10)
            s_ = randint(1, 10)
            p = random()

            if p < 0.33:
                s1, s2, s3 = s, s, s_
            elif p < 0.66:
                s1, s2, s3 = s, s_, s
            else:
                s1, s2, s3 = s_, s, s

        weights = yield (kind, s1, s2, s3)

        i += 1

# ------------------------------------------

TD = triangle_domain(100)
n, e, s, i = 1, 1, 1, 1

for _ in range(100):
        
        kind = TD(n, e, s, i)

        if kind == 'not-triangle':
            n += 1
        elif kind == 'equilateral':
            e += 1
        elif kind == 'scalene':
            s += 1
        elif kind == 'isosceles':
            i += 1

print(f'n: {n} e: {e} s: {s} i: {i}')
