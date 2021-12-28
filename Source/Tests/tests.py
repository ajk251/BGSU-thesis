from predicates import *
from domains import *

from algorithms import *
import unittest

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/pytest-tests.fcn
# on 2021 Dec 28 Tue 15:04:21

Xvalues = Integers(-100, 100, nrandom=100)
Yvalues = Integers(-100, 100, nrandom=100)

# start test -----------------
def test_add_6ZDA6():

    for answer_i, case_i in zip(Xvalues):
        assert is_integer(add(answer_i, case_i))
        assert between(add(answer_i, case_i), -200, 200)
