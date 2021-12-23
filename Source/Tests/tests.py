from predicates import *
from domains import *

from algorithms import *
import unittest


# This file was generated automatically by falcon.
# from: Tests/winnow_test.fcn
# on 2021 Dec 23 Thu 15:35:47

X = Integers(0, 100)
Y = Integers(0, 100)

# start test -----------------
def test_fn_1qg():

    for xᵢ, yᵢ in zip(X, Y):
        assert is_integer(fn(xᵢ, yᵢ))
        assert fn(xᵢ, yᵢ) > 1
        assert between(fn(xᵢ, yᵢ), 0, 100)
        x = fn(xᵢ, yᵢ) / 2.0
        assert is_float(x)
        assert between(x, -1.0, 1.0)

def group_test_fna():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fna(xᵢ, yᵢ)
        except Exception as e:
            assert False, "Function error"
            continue
                
        try:
            group = fn_to_b(result)
        except Exception as e_bin:
            assert False, "Group-by error"   
            continue
    
        if group == 'A':
            assert is_float(result)
        elif group == 'B':
            assert between(result, 0, 1)
        else:
            print("You shouldn't be here!") 		# TODO…

def group_test_fnb():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fnb(xᵢ, yᵢ)
            group = result
        except Exception as e:   
            assert False, "Function error"
            continue

        if group == C:
            assert is_integer(result)
        elif group == D:
            assert between(result, -50, 50)
        else:
            print("You shouldn't be here!") 		# TODO…

def group_test_fnc():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fnc(xᵢ, yᵢ)
            group = result
        except Exception as e:   
            assert False, "Function error"
            continue

        if group == 'E':
            assert is_fraction(result)
        if group == 'F':
            assert between(result, Fraction(1,3), Fraction(2,3))
