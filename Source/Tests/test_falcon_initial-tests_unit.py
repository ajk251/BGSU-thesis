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
# on 2022 Nov 03 Thu 13:55:43


class Test(unittest.TestCase):
    def test_add(self):
        # please work

        for x, y in ART(art1, art2, min_distance=3, max_distance=10):
            assert is_int(add(x, y))
            assert between(add(x, y), -1500, 1500)

    def test_add_6ym(self):
        for xᵢ, zᵢ in zip(X, Z):
            assert is_int(add(xᵢ, zᵢ))
            assert between(add(xᵢ, zᵢ), -100, 100)
