
from collections import defaultdict, namedtuple
from itertools import product
from numbers import Number
from typing import Union, Tuple
from operator import eq, ne


# -----------------------------------------------

# This project comes from Software Testing: A craftsman's approach. It is the nextdate
# problem, ie test if the NextDate() function returns a valid date. I adapted the code
# from the book and some help online.

# 3 ways to test this.
#   1 → just asserts
#   2 → build a list and test it against a known list/answer-set
#   3 → test over domain & validate answers using predicate


# → this gets applied to a function and saves a different result
#           rʹ    = fn(args)
#           group = predicate(rʹ)

 # iterate or product over the list in winnow? How to know? → use enum? it would be known from syntax...



#******************************************************************************

def next_date(year: int, month: int, day: int) -> Tuple[int, int, int]:

    is_modof = lambda m,n: m % n == 0
    leap_year = is_modof(year, 4) and (not is_modof(year, 100) or is_modof(year, 400))

    # kinda the special cases, Dec 31 & Feb
    if month == 12 and day == 31:
        return (year + 1, 1, 1)
    elif month == 2:
        if leap_year:             
            return (year, 3, 1) if day == 29 else (year, month, day+1)
        elif not leap_year:
            return (year, 3, 1) if day == 28 else (year, month, day+1)

    if month in [1,3,5,7,8,10,12]:
        return (year, month+1, 1) if day == 31 else (year, month, day+1)
    elif month in [4,6,9,11]:
        return (year, month+1, 1) if day == 30 else (year, month, day+1)

def is_valid_date(y: int, m: int, d: int) -> bool:

    # help from: https://codereview.stackexchange.com/questions/200634/program-to-check-if-a-date-is-valid-or-not

    is_modof = lambda m,n: m % n == 0

    leap_year = is_modof(y, 4) and (not is_modof(y, 100) or is_modof(y, 400))

    # valid months or years
    if not (1 <= d <= 31) or not (1 <= m <= 12):
        return False
    
    # month doesn't have 31 days
    if m in [1,3,5,7,8,10,12]:
        if d > 31: return False
    if m in [4,6,9,11]: 
        if d > 30: return False

    if leap_year and m == 2:
        if d > 28: return False
    elif m == 2:
        if d > 29: return False

    return True

# -----------------------------------------------


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

    # iterate or product ?

    groups = defaultdict(list)

    # !!! this changed !!!!
    for args in domain:
        result = fn(*args)
        groups[result].append(args)

    # if len(groups) ≠ len(group_tests) → there is a problem!
    # or groups ≠ a proper subset of group_tests

    for case in test_cases:

        # this simply tests all of them at once
        p  = test_cases[case].predicate
        tfn = test_cases[case].test_fn
        print('outcome: ', is_all_over(groups[case], p, tfn))
        
        # this enumerates all the cases
        for arg in groups[case]:
            # isinstance of TestPredicate
            print('assert ', fn.__name__, arg, ' is ', case) 


# -----------------------------------------------

# my basic tests...

# print('is valid', is_valid_date(1900, 1, 1),  '1/1/1900')
# print('is valid', is_valid_date(1900, 2, 1),  '2/1/1900')
# print('is valid', is_valid_date(2000, 2, 28),  '2/22/2000')
# print('is valid', is_valid_date(1900, 2, 29),  '1/2/1900')

# print('…'*25)

# print('is valid', is_valid_date(1900, 4, 31), '')
# print('is valid', is_valid_date(1813, 2, 30), '')
# print('is valid', is_valid_date(1812, 2, 30), '')
# print('is valid', is_valid_date(1812, 2, 31), '')

# print('…'*25)

# print(next_date(2001, 12, 31))
# print(next_date(2000, 12, 1))
# print(next_date(2001, 5, 30))
# print(next_date(2001, 5, 31))

# -----------------------------------------------



days   = (1, 2, 15, 30, 31)
months = (1, 2, 6, 11, 12)
years  = (1812, 1813, 1912, 1913, 2011, 2012)

test_days = [next_date(y,m,d) for y,m,d in product(years, months, days)]

# print(test_days)

# this doesn't work. next_date outputs a tuple/date and is not a predicate - it is organized by output
#
# Winnow next_date (years ⨯ months ⨯ days):
#   | True  ⊤ is_valid_date
#   | False ⊤ is_valid_date
#
# winnow(next_date, 
#       (years, months, days),
#       test_cases={True: TestPredicate(satisfies, is_valid_date),
#                   False: TestPredicate(satisfies, is_valid_date)})

winnow(is_valid_date,
       test_days,
       test_cases={True: TestPredicate(satisfies, is_valid_date),
                   False: TestPredicate(satisfies, is_valid_date) })