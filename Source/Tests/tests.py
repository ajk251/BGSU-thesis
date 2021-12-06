from predicates import *
from domains import *

from algorithms import *
import unittest


# This file was generated automatically by falcon.
# from: Tests/some-tests.fcn
# on 2021 Dec 06 Mon 12:44:07

x = [1, 2, 3]
y = [4, 5, 6]
X = Reals()
Y = Reals(4, 5)
Z = Naturals(1, 2, nrandom=10)

# start test -----------------
def test_fn3_QrWI7():
    for xᵢ in X:
        assert is_modulus_of(fn3(xᵢ), 10)
        assert is_a(fn3(xᵢ), float)
        assert same_instance(fn3(xᵢ), [10,10,10])
        assert fn3(xᵢ) > 10
        assert raises(fn3, xᵢ, NumericalError)

X = Integers(-10, 10, nrandom=10)

# start test -----------------
def test_fn4_5wTcv():
    for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
        assert is_modulus_of(fn4(xᵢ, yᵢ, zᵢ), 10)
        assert is_a(fn4(xᵢ, yᵢ, zᵢ), float, int, fraction)
        assert same_instance(fn4(xᵢ, yᵢ, zᵢ), [10,10,10])

# Assertion test -------------
assert fn(1, 2, 3) > 4
assert fn(1, 2, three=3, four=4) != 5
assert is_float(fn(1, [2.0], three=3.0), True)