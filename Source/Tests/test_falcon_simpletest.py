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
# from: simpletest.fcn
# on 2022 Aug 09 Tue 10:59:16

Ints = integers(n=10)
def identity(n): return n


def test_satisfy_identity_Zk():

    for ints in Ints:

        try:
            result = identity(ints)
        except Exception as error:
            result = error

        count = 0

        if not (is_modulus_of(result)):
            count += 1
        if is_modulus_of(result, 2):
            count += 1
        if between(result, 0, 1):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"
