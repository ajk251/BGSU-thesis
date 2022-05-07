from predicates import *
from domains import *

from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError
from algorithms.algorithms import *
import unittest
from collections import defaultdict

import pytest

# This file was generated automatically by falcon.
# from: Tests/unit-test2.fcn
# on 2022 May 06 Fri 21:23:18

X = Integers()
Y = Integers()
Z = Integers()

class Test(unittest.TestCase):

    def test_fn_8riW6(self):

        for xᵢ, yᵢ in zip(X, Y):
            assert is_integer(fn(xᵢ, yᵢ))
            assert is_float(fn(xᵢ, yᵢ))


    def test_fn_assertions_h7TpH(self):

        # This is a test of some random stuff
        assert fn(1, 2, 3) > 4
        assert is_float(fn(1, [2.0], three=3.0))
        assert fn(1, 2, three=3, four=4) != 5

    def test_add(self):

        # please work and have a suffix
        for a_i, b_i, c_i in all_triplets(X, Y):
            assert is_integer(add(a_i, b_i, c_i))
            assert between(add(a_i, b_i, c_i), -1500, 1500)


def test_groupby_fna():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fna(xᵢ, yᵢ)
        except Exception as e:
            result = e
                
        try:
            group = fn_to_b(result)
        except Exception as e:
            raise FalconError('Failed to properly partition the function')
    
        if group == 'A':
            assert is_float(result)
            assert is_integer(result)
        elif group == 'B':
            assert between(result, 0, 1)
            assert between(result, -10, 10)
        elif group == 'Error':
            assert catch_error(result, ZeroDivisionError)
        else:
            raise FalconError("Failed to meet at least one group") 		# TODO…

# Satisfy here…
