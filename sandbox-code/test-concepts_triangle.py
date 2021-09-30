
from collections import defaultdict, namedtuple
from enum import Enum
from itertools import product
from numbers import Number
from typing import Union
from operator import eq, ne

# how to handle passing of values, multiple args, and tuples.

numeric = Union[int, float, Number]

# helpers/utils --------

# just use a dataclass…
# BooleanTest = namedtuple('BooleanTest', 'predicate, outcome')   # ie predicate(x), implicilty True  → assert predicate(x)
TestValue = namedtuple('TestValue', 'test_fn, rvalue')                    # ie < 4, Test(lt, 4) is  lt(_, 4) ⇔ _<4, implicitly True
TestPredicate = namedtuple('TestPredicate', 'predicate, test_fn')

Predicates = {'=': eq,
              '≠': ne,
              '⊧': 'satisfies', # invoke call
              '⊤': True,
              '⊥': False}

def is_all(sequence, predicate, test_value):

    if isinstance(predicate, str):
        predicate = Predicates[predicate]

    # ⊤ ∀ v ∈ S
    return all(predicate(value, test_value) for value in sequence)

def is_all_over(sequence, predicate, test_fn):

    if isinstance(predicate, str):
        predicate = Predicates[predicate]

    return all(predicate(test_fn, args) for args in sequence)

# or truthy/falsy
# there might be a problem regarding various inputs!
def satisfies(predicate, value):
    return predicate(*value) == True

def doesnt_satisfy(predicate, value):
    return predicate(*value) == False


def winnow(fn, domain, test_cases):

    # is either enumerative or cartesian
    # how to handle errors?????
    #       catch it, test if is present, otherwise put into other, raise error when done

    groups = defaultdict(list)

    for args in product(*domain):
        
        result = fn(*args)
        groups[result].append(args)

    # if len(groups) ≠ len(group_tests) → there is a problem!
    # or groups ≠ a proper subset of group_tests

    for case in test_cases:
        # print(case, groups[case])

        # this simply tests all of them at once
        p  = test_cases[case].predicate
        tfn = test_cases[case].test_fn
        print('outcome: ', is_all_over(groups[case], p, tfn))
        
        # this enumerates all the cases
        for arg in groups[case]:
            # isinstance of TestPredicate
            print('assert ', fn.__name__, arg, ' is ', case)
            
            
# -----------------------------------------------

Triangle = Enum('Triangle', 'equalateral, isosceles, scalene, not_triangle')


def triangle_kind(a: numeric, b: numeric, c: numeric) -> Triangle:
    
    if a == 0 or b == 0 or c == 0:
        return Triangle.not_triangle
    elif a == b and a == c and b == c:
        return Triangle.equalateral
    elif a == b or a == c or b == c:
        return Triangle.isosceles
    elif a != b and a != c and b != c:
        return Triangle.scalene
    elif (a < c+b) & (b < a+c) & (c < a+b):
        return Triangle.not_triangle
    
    # shouldn't get here...
    return Triangle.not_triangle

not_zero       = lambda a,b,c: a != 0 and b != 0 and c != 0
is_equalateral = lambda a,b,c: a == b and a == c and b == c and not_zero(a,b,c)
is_isosceles   = lambda a,b,c: a == b or a == c or b == c and not_zero(a,b,c)
is_scalene     = lambda a,b,c: a != b and a != c and b != c and not_zero(a,b,c)
isnt_triangle  = lambda a,b,c: (a < c+b) & (b < a+c) & (c < a+b)

# bounds = (0, 1, 2, 100, 199, 200, 201)
bounds = (1, 2, 100, 199, 200, 201)


# =============================================================================

# print(is_all([1,1,1,1], eq, 1))

# test_triangle(test_triangle, (bounds, bounds, bounds), {})
winnow(triangle_kind, 
      (bounds, bounds, bounds),
      test_cases={Triangle.equalateral:   TestPredicate(satisfies, is_equalateral),
                  Triangle.isosceles:     TestPredicate(satisfies, is_isosceles),
                  Triangle.scalene:       TestPredicate(satisfies, is_scalene),
                  Triangle.not_triangle:  TestPredicate(satisfies, isnt_triangle)})
