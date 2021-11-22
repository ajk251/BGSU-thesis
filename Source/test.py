from predicates import *
from Domains import *

import unittest

# This file was generated automatically by falcon.
# from: Tests/logical-tests.fcn
# on 2021 Nov 22 Mon 14:48:56

# start test -----------------
for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
    assert logical(xᵢ, yᵢ, zᵢ) < 4 or (logical(xᵢ, yᵢ, zᵢ))
    assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ))
    assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ))
