from predicates import *
from domains import *

from algorithms import *
import unittest

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/pytest-tests.fcn
# on 2022 Jan 04 Tue 15:21:35

Xvalues = Integers(-100, 100, nrandom=100)
Yvalues = Integers(-100, 100, nrandom=100)
Zvalues = Numbers(-1000, 1000)
x = x + 1

# start test -----------------
def test_add_mUdrl():

    for answer_i, case_i in ART(Xvalues, initial=[0, 0, 0]):
        assert is_integer(add(answer_i, case_i))
        assert between(add(answer_i, case_i), -200, 200)
        x = x + 1
        assert is_float(x)

def test_groupby_add():

    for xvaluesᵢ in XValues:

        try:
            result = add(xvaluesᵢ)
            group = result
        except Exception as e:   
            assert False, "Function error"
            continue

        if group == 'a':
            assert is_string(result)
        elif group == 'b':
            assert is_integer(result)
        elif group == 'c':
            assert is_list(result)
        else:
            print("You shouldn't be here!") 		# TODO…
