from predicates import *
from Domains import *

from algorithms import *
import unittest

import fractions
from fractions import Fraction
import fractions as F
from fractions import Fraction as F
from logicals import logical

# This file was generated automatically by falcon.
# from: Tests/logical-tests.fcn
# on 2021 Dec 02 Thu 18:55:38

X = Reals(0, 100)
Y = Reals(0, 100)
Z = Reals(0, 100)

# start test -----------------
for xᵢ, yᵢ, zᵢ in ART(X, Y, Z, initial=[0, 0, 0], max_tests=10):
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
