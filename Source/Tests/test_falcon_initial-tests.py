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
# from: initial-tests.fcn
# on 2022 Aug 23 Tue 16:48:53

art1 = ART(max_candidates=100)
art2 = ART(max_candidates=200)
X = integers(-1000, 1000, nrandom=10)
Y = integers(-500, 500, nrandom=10)
Z = integers()
def add(x, y): return x + y

def test_add():
    # please work

    for art1ᵢ, art2ᵢ in ART(art1, art2, min_distance=3, max_distance=10):
        assert is_int(add(art1ᵢ, art2ᵢ))
        assert between(add(art1ᵢ, art2ᵢ), -1500, 1500)

def test_add_j4w8():
    for xᵢ, zᵢ in zip(X, Z):
        assert is_int(add(xᵢ, zᵢ))
        assert between(add(xᵢ, zᵢ), -100, 100)
