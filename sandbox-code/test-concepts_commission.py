
from collections import defaultdict, namedtuple
from itertools import product
from operator import eq, ne
from random import randint

# -----------------------------------------------------------------------------
# This project comes from Software Testing: A craftsman's approach. It is the lock, 
# stock, and barrels problem. I assume the the calculation isn't trival for the 
# purposes of testing it, ie calculate(x,y,z) == test_caclulation(x,y,z) isn't
# feasible.

# The challenge with this is how to test it. It returns a float. Either test by 
# enumerating assertions or over a domain and analyse the results.

# -----------------------------------------------------------------------------
# right from the problem
# should this return sales too? (100, 10), (7800, 1420)

def commission(nlocks: int, nstocks: int, nbarrels: int) -> float:

    inner = lambda xs,ys: sum(x*y for x,y in zip(xs,ys))

    assert nlocks <= 70,   'Exceeded lock sales inventory'
    assert nstocks <= 80,  'Exceeded stock sales inventory'
    assert nbarrels <= 90, 'Exceeded barrels sales inventory'

    assert nlocks >= 1,   'Must sell more than 1 lock'
    assert nstocks >= 1,  'Must sell more than 1 stock'
    assert nbarrels >= 1, 'Must sell more than 1 barrel'
    
    # the costs
    lock   = 45
    stock  = 30
    barrel = 25

    # sales = lock * nlocks + stocks * nstocks + nbarrels * barrel
    sales = inner([lock, stock, barrel], [nlocks, nstocks, nbarrels])

    if sales > 1800:
        commission = inner([.1, .15, .2], [1_000, 800, (sales-1_800)])
    elif sales > 1000:
        commission = inner([.1, .15], [1_000, (sales-1_000)])
    else:
        commission = 0.1 * sales

    return commission

# -----------------------------------------------------------------------------

TestCase = namedtuple('TestCase', 'predicate, test_value, test_solution')

# for the groupby
TestValue = namedtuple('TestValue', 'label, test_fn, rvalue')                    # ie < 4, Test(lt, 4) is  lt(_, 4) ⇔ _<4, implicitly True
TestPredicate = namedtuple('TestPredicate', 'label, predicate, test_fn')

#-----------------------

def satisfies_predicate(predicate, value):
    return predicate(*value) == True

def doesnt_satisfy_predicate(predicate, value):
    return predicate(*value) == False

def raises_error(fn, args, error_kind):
    
    try:
        _ = fn(*args)
    except error_kind as e:
        return True
    except Exception as e:
        return False
    
    return False

def is_all(sequence, predicate, test_value):

    if isinstance(predicate, str):
        predicate = Predicates[predicate]

    # ⊤ ∀ v ∈ S
    return all(predicate(value, test_value) for value in sequence)

def is_all_over(sequence, predicate, test_fn):

    if isinstance(predicate, str):
        predicate = Predicates[predicate]

    return all(predicate(test_fn, args) for args in sequence)

# to use symbols rather than functions
Predicates = {'=': eq,
              '==': lambda v,t: isinstance(v, type(t)) and eq(v, t),                # assert type and value
              '≠': ne,
              '!': raises_error,
              '⊧': 'satisfies_predicate', # invoke call
              '⊤': True,
              '⊥': False}

#-----------------------

# test by enumeration
def test(function, cases):

    strong_equality = lambda v,t: isinstance(v, type(t)) and eq(v, t)

    for case in cases:
        
        # this is what the tests would look like
        print(f'assert {function.__name__}{case.test_value} {case.predicate} {case.test_solution}', end='')

        # actual tests & handle special cases
        if case.predicate == '!':
            raises_error(function, case.test_value, case.test_solution)
            # continue
        else:
            assert Predicates[case.predicate](function(*case.test_value), case.test_solution), f'Assertion case {case.test_value} failed'
        
        # print('== : ', strong_equality(function(*case.test_value), case.test_solution))
        # print('  ', function(*case.test_value), case.test_solution)
        
        print('\t[PASSED]')


    print()


# this doesn't work here...
# def winnow(fn, domain, test_cases):

#     # is either enumerative or cartesian
#     # how to handle errors?????
#     #       catch it, test if is present, otherwise put into other, raise error when done

#     # iterate or product ?

#     groups = defaultdict(list)

#     # have to wrap this in try/except!
#     for args in domain:
#         result = fn(*args)
#         groups[result].append(args)

#     # if len(groups) ≠ len(group_tests) → there is a problem!
#     # or groups ≠ a proper subset of group_tests

#     for case in test_cases:

#         # this simply tests all of them at once
#         p  = test_cases[case].predicate
#         tfn = test_cases[case].test_fn
#         print('outcome: ', is_all_over(groups[case], p, tfn))
        
#         # this enumerates all the cases
#         for arg in groups[case]:
#             # isinstance of TestPredicate
#             print('assert ', fn.__name__, arg, ' is ', case) 


def satisfies(fn, domain, test_cases):

    groups = defaultdict(list)

    for args in domain:
        result = fn(*args)
        groups[result].append(args)

    for case in test_cases:
        pass



# =============================================================================


# method 1
# Test commission (locks ⨯ stocks ⨯ barrels):
#   | <1,1,1>    == 10.0
#   | <70,80,90> == 1420.0

test(commission, [TestCase('=', (1,1,1), 10),                               # type & value --> it fails too!
                  TestCase('==', (1,1,2), 12.5),                            # value, ie 3=3.0
                  TestCase('==', (70,80,90), 1420.0),
                  TestCase('!', (100, 100, 100), AssertionError),
                  TestCase('!', (1,1,0), AssertionError)])

# ------------------------------------------

locks   = [0, 1, 5, 10, 50, 70, 71] + [randint(0, 100) for _ in range(25)]
stocks  = [0, 1, 5, 10, 50, 80, 81] + [randint(0, 100) for _ in range(25)]
barrels = [0, 1, 5, 10, 50, 90, 91] + [randint(0, 100) for _ in range(25)]


is_float = lambda v: isinstance(v, float)
is_gt0   = lambda v: v > 0

satisfies(commission, product(locks, stocks, barrels), [TestPredicate('True', True, is_float),
                                                        TestValue('False', True, is_gt0),  
                                                        TestCase('==', (70,80,90), 1420.0),
                                                        TestCase('!', (100, 100, 100), AssertionError),
                                                        TestCase('!', (1,1,0), AssertionError)])



