from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest


# This file was generated automatically by Falcon.
# from: some-tests.fcn
# on 2022 Aug 25 Thu 13:39:45

x = [1, 2, 3]

y = [4, 5, 6]

def add(x,y):
    return x + y

X = reals()
Y = reals(-1, 1)
Z = integers(0, 100, n=10)

def test_add_assertions_Mjie():

    assert add(1, 2) == 3
    print("hello world")

def test_fn3_1J3h3():
    for xᵢ in X:
        print("hello world")
        assert is_modulus_of(fn3(xᵢ), 10), 'Value a % n != 0'
        assert is_a(fn3(xᵢ), float), 'The value is not any of instances specified'
        assert same_instance(fn3(xᵢ), [10,10,10]), 'The value must be the same instance'
        assert gt(fn3(xᵢ))
        assert raises_error(fn3(xᵢ), NumericalError)

X = integers(-10, 10, n=10)
def test_fn4_665x4():
    for xᵢ, yᵢ, zᵢ in zip(X, Y, Z):
        assert is_modulus_of(fn4(xᵢ, yᵢ, zᵢ), 10), 'Value a % n != 0'
        assert is_a(fn4(xᵢ, yᵢ, zᵢ), float, int, Fraction), 'The value is not any of instances specified'
        assert same_instance(fn4(xᵢ, yᵢ, zᵢ), [10,10,10]), 'The value must be the same instance'


def test_fn_assertions_GFkPF():

    # This is a test of some random stuff
    assert fn(1, 2, 3) > 4
    assert fn(1, 2, three=3, four=4) != 5
    assert is_float(fn(1, [2.0], three=3.0), u, e)
