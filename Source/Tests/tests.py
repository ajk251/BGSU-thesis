from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict
import unittest

import pytest

# This file was generated automatically by falcon.
# from: Tests/some-tests.fcn
# on 2022 Jun 18 Sat 18:33:33

X = reals()
Y = reals(-1, 1)
Z = integers(0, 100, n=10)

# start test -----------------
def test_fn3_jmq():

    for xᵢ in X:
        assert is_modulus_of(fn3(xᵢ), 10)
        assert is_a(fn3(xᵢ), float)
        assert same_instance(fn3(xᵢ), [10,10,10])
        assert fn3(xᵢ) > 10
        assert raises_error(fn3(xᵢ), NumericalError)

X = integers(-10, 10, n=10)

# start test -----------------
def test_fn4_Ekw():

    for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
        assert is_modulus_of(fn4(xᵢ, yᵢ, zᵢ), 10)
        assert is_a(fn4(xᵢ, yᵢ, zᵢ), float, int, Fraction)
        assert same_instance(fn4(xᵢ, yᵢ, zᵢ), [10,10,10])


def test_fn_assertions_mCe():

    # This is a test of some random stuff
    assert fn(1, 2, 3) > ('>', '4')
    assert fn(1, 2, three=3, four=4) != ('≠', '5')
    assert is_float(fn(1, [2.0], three=3.0))