from predicates import *
from Domains import *

import unittest

# This file was generated automatically by falcon.
# from: Tests/logical-tests.fcn
# on 2021 Nov 23 Tue 13:47:35

X = Reals(0, 100)
Y = Reals(0, 100)
Z = Reals(0, 100)

def logical(x, y, z): pass

# start test -----------------
for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
    assert logical(xᵢ, yᵢ, zᵢ) < 4 or between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
    assert is_modof(logical(xᵢ, yᵢ, zᵢ), 10)
    assert between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ))
    assert (is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not (is_integer(logical(xᵢ, yᵢ, zᵢ)) or is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) or (is_float(logical(xᵢ, yᵢ, zᵢ)) and is_fraction(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not (logical(xᵢ, yᵢ, zᵢ) > 8 and logical(xᵢ, yᵢ, zᵢ) < 10 and logical(xᵢ, yᵢ, zᵢ) == 9)
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ)) or not is_fraction(logical(xᵢ, yᵢ, zᵢ)) or (logical(xᵢ, yᵢ, zᵢ), 0)
