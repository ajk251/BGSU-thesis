
from algorithms.algorithms import algorithm

# Adaptive Random Testing (ART)
# ART takes some distributions and generates some candidate points. If those
#   points are at least some distance away, it becomes the test point.

# distance measures ---------------------------------------


def euclidian(X, Y) -> float:
    return sum((x-y)**2.0 for x, y in zip(X, Y))


def manhattan(X, Y) -> float:
    return sum(abs(x-y) for x, y in zip(X, Y))


# Adaptive Random Testing ---------------------------------

# TODO: generate warning for failure to get min distance
#       raise errors…

@algorithm(alias=['art', 'ART'])
def ART(domains, initial=None, min_distance: float = 5.0, max_tests: int = 500,
        num_candidates: int = 10, distance=euclidian, max_candidates: int = 100_000):

    # candidates refers to the generated values, ie generate n, likely except 1
    # tests refers to the values accepted, because test << candidates

    n_candidates: int = 0      # total number of candidates produced
    n_tests: int = 0           # number of tests produced
    d: int = len(domains)

    case = tuple(next(domains[i]) for i in range(d)) if initial is None else initial
    stop = lambda : True if ((n_tests-1) > max_tests) or (n_candidates >= max_candidates) else False

    while not stop():

        candidates = [tuple(next(domains[i]) for i in range(d)) for _ in range(num_candidates)]
        cʹ = max(candidates, key=lambda c: distance(case, c))

        n_candidates += num_candidates

        if distance(case, cʹ) >= min_distance:
            case = cʹ

            n_tests += 1

            yield cʹ

    return







