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
# from: testargs.fcn
# on 2022 Oct 11 Tue 11:46:25

Ints1 = integer_range(lower=1, upper=100, step=1)
Ints2 = integer_range(lower=1, upper=100, step=1)
def test_object_K6():
    for i in twise_combination(Ints1, Ints2, n=2):
        assert is_instance(i, tuple), 'The value is not the instance specified'
