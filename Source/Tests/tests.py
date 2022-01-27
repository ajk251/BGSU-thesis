from predicates import *
from domains import *

from algorithms import *
import unittest

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/pytest-tests.fcn
# on 2022 Jan 26 Wed 10:41:13

Xvalues = Integers(-10, 10, nrandom=100)
Yvalues = Integers(-10, 10, nrandom=100)
Zvalues = Numbers(-1000, 1000)
Avalues = Boundary(-10, 10)

# Assertion test -------------
assert add(1, 2, 3) > 4
assert add(1, 2, three=3, four=4) != 5
assert is_float(add(1, [2.0], three=3.0), True)

# start test -----------------
def test_add_Mjray():

    # 'here I am testing to see if it works'

    for xvalues_i, yvalues_i in ART(Xvalues, Yvalues, initial=[0, 0, 0]):
        assert is_integer(add(xvalues_i, yvalues_i))
        assert between(add(xvalues_i, yvalues_i), -100, 100)
        x = xvalues_i + 1.0
        assert is_float(x)


# start test -----------------
def test_add_YYoe():

    for xvaluesᵢ, zvaluesᵢ in zip(Xvalues, Zvalues):
        assert is_integer(add(xvaluesᵢ, zvaluesᵢ))
        assert between(add(xvaluesᵢ, zvaluesᵢ), -100, 100)

def test_groupby_addg():

    for xvaluesᵢ, yvaluesᵢ in zip(Xvalues, Yvalues):

        try:
            group = addg(xvaluesᵢ, yvaluesᵢ)
            #group = result
        except Exception as e:   
            assert False, "Function error"
            continue

        if group == 'a':
            assert is_float(xvaluesᵢ, yvaluesᵢ)
        elif group == 'b':
            assert is_integer(xvaluesᵢ, yvaluesᵢ)
        elif group == 'c':
            assert is_positive(xvaluesᵢ, yvaluesᵢ)
        else:
            print("You shouldn't be here!") 		# TODO…

def test_groupby_addf():

    for xvaluesᵢ, yvaluesᵢ in zip(Xvalues, Yvalues):

        try:
            result = addf(xvaluesᵢ, yvaluesᵢ)
        except Exception as e:
            assert False, "Function error"
            continue
                
        try:
            group = bin(result)
        except Exception as e_bin:
            assert False, "Group-by error"   
            continue
    
        if group == 'a':
            assert is_float(xvaluesᵢ, yvaluesᵢ)
        elif group == 'b':
            assert is_integer(xvaluesᵢ, yvaluesᵢ)
        elif group == 'c':
            assert is_positive(xvaluesᵢ, yvaluesᵢ)
        else:
            print("You shouldn't be here!") 		# TODO…
