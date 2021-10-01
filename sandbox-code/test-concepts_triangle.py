
from collections import defaultdict, namedtuple
from enum import Enum
from itertools import product
from numbers import Number
from typing import Union
from operator import eq, ne



# The problem comes from Software Testing: A craftsmans approach. It is straight-forward - ensure the classification
#  of triangle_kind identifies the triangle correctly. As long as the inputs are positive integers, the function
#  will always return an answer.

# I solve it by using the TestGroup or Winnow test - every result falls into one category. Then use a predicate over
# that category.

# Implementation problems: 
#   • how to handle the cartesian-product of arguments. What does the product of optional args look like?
#   • do these problems get implemented as functions for the user or enumerated as assert statements?
#   • how to know if the domain is by random, enumeration, or product?
#   • winnow | should change to <label> <value> <predicate> <arg> 
#           - ie | 'equalateral' Triangle.equalateral ⊤ is_equalateral
#           - this solves the problem of when the category is an error or something
#   • can create a cousin of Winnow → Satisfies, for a result that falls into at least 1 category or more


# what to call these? ↓
# assert fn(arg) == test_answer         ← this kind?  Test-by-Predicate
#        ↑   ↑   ↑      ↑
#
# assert x < 4                          ← this kind?  Test-by-Value
#        ↑ ↑ ↑      
# 
#******************************************************************************

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

# -----------------------------------------------

# the actual function should be similiar to this
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

# predicates for a triangle
not_zero       = lambda a,b,c: a != 0 and b != 0 and c != 0
is_equalateral = lambda a,b,c: a == b and a == c and b == c and not_zero(a,b,c)
is_isosceles   = lambda a,b,c: a == b or a == c or b == c and not_zero(a,b,c)
is_scalene     = lambda a,b,c: a != b and a != c and b != c and not_zero(a,b,c)
isnt_triangle  = lambda a,b,c: (a < c+b) & (b < a+c) & (c < a+b)

# bounds = (0, 1, 2, 100, 199, 200, 201)
bounds = (1, 2, 100, 199, 200, 201)


# =============================================================================

# What it should look in the language

# bounds := <1, 2, 100, 199, 200, 201>
#
# Winnow triangle_kind bounds ⨯ bounds ⨯ bounds:
#    | equalateral ⊤ is_equalateral
#    | isosoceles  ⊤ is_isosoceles
#    | scalene     ⊤ is_scalene
#    | not_trangle ⊤ isnt_triangle

# ----------------------------------

winnow(triangle_kind, 
      (bounds, bounds, bounds),
      test_cases={Triangle.equalateral:   TestPredicate(satisfies, is_equalateral),
                  Triangle.isosceles:     TestPredicate(satisfies, is_isosceles),
                  Triangle.scalene:       TestPredicate(satisfies, is_scalene),
                  Triangle.not_triangle:  TestPredicate(satisfies, isnt_triangle)})
