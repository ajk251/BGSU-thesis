from predicates import *
from domains import *

from algorithms import *
import unittest


# This file was generated automatically by falcon.
# from: Tests/winnow_test.fcn
# on 2021 Dec 08 Wed 10:00:36

X = Integers(0, 100)
Y = Integers(0, 100)

# start test -----------------
def test_fn_dEWB():
    for xᵢ, yᵢ in zip(X, Y):
        assert is_integer(fn(xᵢ, yᵢ))
        assert fn(xᵢ, yᵢ) > 1
        assert between(fn(xᵢ, yᵢ), 0, 100)
        x = fn(xᵢ, yᵢ) / 2.0
        assert is_float(x)
        assert between(x, -1.0, 1.0)

def test_fn():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fn()
        except Exception as e:
            group = 'Unspecified function error'
            result = e
                
        try:
            group = fn_to_b(result)
        except Exception as e_bin:
            group = 'Unspecified binning error'
            result = e_bin     
    
def test_fn():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fn()
            group = result
        except Exception as e:
            group = 'Unspecified function error'
            result = e    
