from predicates import *
from domains import *

from algorithms import *
import unittest

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/pytest-tests.fcn
# on 2022 Feb 14 Mon 14:20:15

Xvalues = Integers(-10, 10, nrandom=100)
Yvalues = Integers(-10, 10, nrandom=100)
Zvalues = Numbers(-1000, 1000)
Avalues = Boundary(-10, 10)

# Assertion test -------------
assert is_integer(add(1, 2, 3)), "Does this even work?"
assert add(4, 5, 6) > 0, "Does *this* even work?"

# Assertion test -------------
assert add2(1, 2, 3) > 4
assert add2(1, 2, three=3, four=4) != 5
x = 1 + 2
assert is_float(add2(1, [2.0], three=3.0))
assert card_lt_n(add2([1,2,3]), 5)

# start test -----------------
def test_add_rJA():

    # 'here I am testing to see if it works and it is the one with >'

    for x_i, y_i, z_i in ART(Xvalues, Yvalues, initial=[0, 0, 0]):
        assert is_integer(add(x_i, y_i, z_i)) or is_float(add(x_i, y_i, z_i)), "This is the error"
        assert add(x_i, y_i, z_i) > 1, "This is another problem"
        assert between(add(x_i, y_i, z_i), -100, 100)
        x = x_i + y_i + 1.0
        assert is_float(x)


# start test -----------------
def test_add_UeF():

    for xvaluesᵢ, zvaluesᵢ in zip(Xvalues, Zvalues):
        assert is_integer(add(xvaluesᵢ, zvaluesᵢ)) or is_float(add(xvaluesᵢ, zvaluesᵢ))
        assert add(xvaluesᵢ, zvaluesᵢ) >= 0.0 or add(xvaluesᵢ, zvaluesᵢ) <= 1.0
        assert between(add(xvaluesᵢ, zvaluesᵢ), 0, 1) and is_float(add(xvaluesᵢ, zvaluesᵢ))
        assert between(add(xvaluesᵢ, zvaluesᵢ), -100, 100)


def test_groupby_addg():

    for xvaluesᵢ in Xvalues:

        try:
            group = addg(xvaluesᵢ)
        except Exception as e:   
            assert False, "Function error"
            continue

        if group == 'a':
            assert is_float(xvaluesᵢ)
        elif group == 'b':
            assert is_integer(xvaluesᵢ)
        elif group == 'c':
            assert is_positive(xvaluesᵢ)
        elif group == 'd':
            assert result > xvaluesᵢ
        else:
            print("You shouldn't be here!") 		# TODO…


def test_groupby_addf():

    for xvaluesᵢ in Xvalues:

        try:
            result = addf(xvaluesᵢ)
        except Exception as e:
            assert False, "Function error"
            continue
                
        try:
            group = bin_fn(result)
        except Exception as e:
            assert False, "Group-by error"   
            continue
    
        if group == 'a':
            assert is_float(result)
        elif group == 'b':
            assert is_integer(result)
        elif group == 'c':
            assert is_positive(result)
        elif group == 'd':
            assert between(result, 0, 1)
        elif group == 'e':
            assert result >= 1
        else:
            print("You shouldn't be here!") 		# TODO…
