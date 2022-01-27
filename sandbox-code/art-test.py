
import random


def euclidian(X, Y) -> float:
    return sum((x-y)**2.0 for x, y in zip(X, Y))


def urand(l, b):
    while True:
        yield random.uniform(l, b)


def ART(domains, initial=None, min_distance : float=5.0, max_tests: int=500, num_candidates : int=10,
        distance=euclidian, max_candidates: int=100_000, round:int=5):

    # candidates refers to the generated values, ie generate n, likely except 1
    # tests refers to the values accepted, because test << candidates

    n_candidates : int = 0      # total number of candidates produced
    n_tests : int = 0           # number of tests produced
    d = len(domains)

    # list of the temporary candidates
    case = tuple(next(domains[i]) for i in range(d)) if initial is None else initial
    candidates = [tuple(next(domains[i]) for i in range(d)) for _ in range(num_candidates)]

    stop = lambda : True if ((n_tests-1) > max_tests) or (n_candidates >= max_candidates) else False

    while not stop():

        candidates = [tuple(next(domains[i]) for i in range(d)) for _ in range(num_candidates)]
        cʹ = max(candidates, key=lambda c: distance(case, c))

        n_candidates += num_candidates

        if distance(case, cʹ) >= min_distance:
            # test_cases.append(cʹ)
            case = cʹ

            n_tests += 1

            print((n_tests) < max_tests)
            
            yield cʹ

    print('tests: ', n_tests, 'candidates: ', n_candidates, '\n')
    print('max tests: ', max_tests)

# ===============================================

print('euclidian: ', euclidian([3,3], [3,3]))
print('euclidian: ', euclidian([2,2], [3,3]))

R = urand(-10.0, 10)

for x,y,z in ART([R, R, R], [0, 0, 0], max_tests=10):
    print(x, y, z)

