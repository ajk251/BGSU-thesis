from predicates import *
from Domains import *

import unittest

import fractions
import fraction from Fraction
import fraction as F
import fractions from Fraction as F

# This file was generated automatically by falcon.
# from: Tests/logical-tests.fcn
# on 2021 Dec 02 Thu 12:03:38

X = Reals(0, 100)
Y = Reals(0, 100)
Z = Reals(0, 100)

# start test -----------------
for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
    assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) or not is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert logical(xᵢ, yᵢ, zᵢ) < 4 or between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
    assert is_modulus_of(logical(xᵢ, yᵢ, zᵢ), 10)
    assert between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ))
    assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ))
    assert (is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and (is_float(logical(xᵢ, yᵢ, zᵢ)) or is_fraction(logical(xᵢ, yᵢ, zᵢ)))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not (logical(xᵢ, yᵢ, zᵢ) > 8 and logical(xᵢ, yᵢ, zᵢ) < 10 and logical(xᵢ, yᵢ, zᵢ) == 9)
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) or is_float(logical(xᵢ, yᵢ, zᵢ)) or not is_fraction(logical(xᵢ, yᵢ, zᵢ)) and logical(xᵢ, yᵢ, zᵢ) > 0
