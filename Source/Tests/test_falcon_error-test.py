from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

# This file was generated automatically by falcon.
# from: error-test.fcn
# on 2022 Jul 08 Fri 13:34:25


def add(x, y):
    return x + y
Xs = integers(n=10)
Ys = integers(n=10)

# start test -----------------
def test_add_PXptD():

    for x, y in zip(Xs, Ys):
        assert is_instance(add(x, y), int), 'The value is not the instance specified'
        assert is_integer(add(x, y))
        assert add(x, y) >= x+y
