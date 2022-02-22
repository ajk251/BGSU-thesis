from predicates import *
from domains import *

from utilities.utls import call

from utilities import FalconError
from algorithms import *
import unittest

from test_funcs import follow_up_func, fn, gb

# This file was generated automatically by falcon.
# from: Tests/winnow_tests3.fcn
# on 2022 Feb 22 Tue 13:26:29

X = Integers(0, 100)
Y = Integers(0, 100)

def test_winnow_fn():

    groups = {group: [] for group in ('a', 'b', 'c', 'd')}

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fn(xᵢ, yᵢ)
        except Exception as e:
            result = e
                
        try:
            group = gb(result)
        except Exception as e:
            raise FalconError('Failed to properly partition the function')
    
        if group == 'a':
            assert is_integer(result)
        elif group == 'b':
            assert between(result, 0, 1)
            groups['b'].append(result)
        elif group == 'c':
            assert is_float(result)
            groups['c'].append(result)
        elif group == 'd':
            assert result > 2
            groups['d'].append(result)
        else:
            raise FalconError("Failed to meet at least one group") 		# TODO…

        assert cardnality_gt(groups['a'], 1), "group str('a') failed to satisfy predicate"
        assert cardnality_plus_minus_n(groups['b'], 100, 10), "group str('b') failed to satisfy predicate"
        assert cardnality_lt(groups['c'], 3), "group str('c') failed to satisfy predicate"
        assert cardnality_gt(groups['d'], 1), "group str('d') failed to satisfy predicate"

        follow_up_func(groups)