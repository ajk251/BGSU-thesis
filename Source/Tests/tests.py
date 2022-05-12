from algorithms.algorithms import *
from domains import *
from predicates import *
from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError

from collections import defaultdict
import unittest

import pytest
from test_functions import add, add2, sub
from test_functions import *

# This file was generated automatically by falcon.
# from: Tests/satisfy-tests.fcn
# on 2022 May 12 Thu 19:55:09

X = Integers(-10, 10, nrandom=100)
Y = Integers(-10, 10, nrandom=100)

def test_add_sUXaj():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = add(xᵢ, yᵢ)
        except Exception as error:
            result = error

        count = 0

        if is_integer(result()):
            count += 1
        if is_float(result()):
            count += 1
        if result() < 4:
            count += 1
        if is_none(result()):
            count += 1
        if catch_error_message(result(), ZeroDivisionError, "0"):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"
        assert count <= 2, f"Exceed number of predicates met - met: {count}, max: 2"
