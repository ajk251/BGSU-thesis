from predicates import *
from Domains import *

import unittest

# This file was generated automatically by falcon.
# from: Tests/some-tests.fcn
# on 2021 Nov 16 Tue 14:15:49
x = [1, 2, 3]
y = [4, 5, 6]
X = Reals()
Y = Reals(4, 5)
Z = Naturals(1, 2, nrandom=10)

# start test -----------------
for xᵢ in X:
    assert is_modof(fn3(xᵢ), 10)
    assert OOPS(fn3(xᵢ), float)
    assert OOPS(fn3(xᵢ), [10,10,10])
    assert gt(fn3(xᵢ), 10)

X = Integers(-10, 10, nrandom=10)

# start test -----------------
for xᵢ,yᵢ,zᵢ in zip(X,Y,Z):
    assert is_modof(fn4(xᵢ, yᵢ, zᵢ), 10)
    assert OOPS(fn4(xᵢ, yᵢ, zᵢ), ('float', 'int', 'fraction'))
    assert OOPS(fn4(xᵢ, yᵢ, zᵢ), [10, 10, 10])

# Assertion test -------------
# This is a test of some random stuff
assert fn(1, 2, 3) > 4
assert fn(1, 2, three=3, four=4) != 5
assert is_float(fn(1, [2.0], three=3.0))
