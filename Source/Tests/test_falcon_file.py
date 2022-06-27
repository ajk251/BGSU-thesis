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
# from: Tests/initial-tests.fcn
# on 2022 Jun 26 Sun 20:12:20

art1 = ART(max_candidates=100)
art2 = ART(max_candidates=200)
X = integers(-1000, 1000, nrandom=10)
Y = integers(-500, 500, nrandom=10)
Z = integers()

# start test -----------------
def test_add():

    # please work

    for art1ᵢ, art2ᵢ in zip(art1, art2):
        assert is_integer(add(art1ᵢ, art2ᵢ))
        assert between(add(art1ᵢ, art2ᵢ), -1500, 1500)

        art1()
        art2()

# start test -----------------
def test_add_QpcmH():

    for xᵢ, zᵢ in zip(X, Z):
        assert is_integer(add(xᵢ, zᵢ))
        assert between(add(xᵢ, zᵢ), -100, 100)
