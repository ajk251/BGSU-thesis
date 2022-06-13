
from random import choices, randint
from typing import Generator, List, Tuple

from domains.domains import domain
from predicates.predicates import predicate

from Examples.max_agreement import average_agreement, average_agreement2

# Note: based on
#           https://medium.com/homeaway-tech-blog/write-better-python-with-hypothesis-5b31ac268b69

# -> Generator[Tuple[List[str], List[str], int]]

@domain(alias=['Agreement'])
def agreement_critical():

    # simple examples that should fail
    yield [], [], 5
    yield ['a', 'b'], [], 5
    yield [], ['a', 'b', 'c'], 5
    yield ['a', 'b', 'c'], ['a', 'b', 'c'], 0


@domain(alias=['RandomAgreement'])
def agreement_example(size_min: int = 0, size_max: int = 100_000, depth_max: int = 100, n: int = 100) :

    alphabet = ['a', 'b', 'c', 'd', 'e']

    for _ in range(n):

        s1 = randint(size_min, size_max)
        s2 = randint(size_min, size_max)

        l1 = tuple(choices(alphabet, k=s1))
        l2 = tuple(choices(alphabet, k=s2))
        d  = randint(0, depth_max)

        yield l1, l2, d


@predicate(alias=['agree?'])
def agree(list1, list2, depth) -> bool:

    a = average_agreement(list1, list2, depth)
    b = average_agreement(list2, list1, depth)

    return a == b and (0.0 <= a <= 1.0) and (0.0 <= b <= 1.0)


@predicate(alias=['agree2?'])
def agree2(list1, list2, depth) -> bool:

    a = average_agreement2(list1, list2, depth)
    b = average_agreement2(list2, list1, depth)

    return a == b and (0.0 <= a <= 1.0) and (0.0 <= b <= 1.0)
