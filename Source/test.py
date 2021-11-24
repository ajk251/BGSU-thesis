from predicates import *
from Domains import *

import unittest

# This file was generated automatically by falcon.
# from: Tests/logical-tests.fcn
# on 2021 Nov 24 Wed 12:07:47

X = Reals(0, 100)
Y = Reals(0, 100)
Z = Reals(0, 100)

# start test -----------------
for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
    assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) or not is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert logical(xᵢ, yᵢ, zᵢ) lt  or between(logical(xᵢ, yᵢ, zᵢ), 100)
    assert is_modulus_of(logical(xᵢ, yᵢ, zᵢ), 10)
    assert between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ))
    assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ))
    assert (is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and (is_float(logical(xᵢ, yᵢ, zᵢ)) or is_fraction(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not (logical(xᵢ, yᵢ, zᵢ) gt  and logical(xᵢ, yᵢ, zᵢ) lt  and logical(xᵢ, yᵢ, zᵢ) eq )
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) or is_float(logical(xᵢ, yᵢ, zᵢ)) or not is_fraction(logical(xᵢ, yᵢ, zᵢ)) and logical(xᵢ, yᵢ, zᵢ) gt 
