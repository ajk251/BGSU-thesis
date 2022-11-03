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
# from: satisfy-tests.fcn
# on 2022 Nov 03 Thu 14:28:03

X = integers(-10, 10, n=100)
Y = integers(-10, 10, n=100)
x = 1 # this is a test


def test_satisfy_add_XM2():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = add(xᵢ, yᵢ)
        except Exception as error:
            result = error

        count = 0

        if is_int(result):
            count += 1
        if is_float(result):
            count += 1
        if lt(result):
            count += 1
        if is_none(result):
            count += 1
        if error-says?(result, ZeroDivisionError, "0"):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"
        assert count <= 4, f"Exceed number of predicates met - met: {count}, max: 4"
