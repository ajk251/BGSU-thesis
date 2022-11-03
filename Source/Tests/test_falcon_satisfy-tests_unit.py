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


class Test(unittest.TestCase):

    def test_satisfy_add_LA(self):

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
