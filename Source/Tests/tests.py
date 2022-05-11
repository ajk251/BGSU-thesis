from predicates import *
from domains import *

from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError
from algorithms.algorithms import *
import unittest
from collections import defaultdict

import pytest

# This file was generated automatically by falcon.
# from: Tests/initial-tests.fcn
# on 2022 May 11 Wed 13:24:42

art1 = ARTR2(max_candidates=100)
art2 = ARTR2(max_candidates=200)
X = Integers(-1000, 1000, nrandom=10)
Y = Integers(-500, 500, nrandom=10)
Z = Integers()

# start test -----------------
def test_add():

    # please work

    for art1ᵢ, art2ᵢ in zip(art1, art2):
        assert is_integer(add(art1ᵢ, art2ᵢ))
        assert between(add(art1ᵢ, art2ᵢ), -1500, 1500)

        art1()
        art2()

# start test -----------------
def test_add_iPIL():

    for xᵢ, zᵢ in zip(X, Z):
        assert is_integer(add(xᵢ, zᵢ))
        assert between(add(xᵢ, zᵢ), -100, 100)
