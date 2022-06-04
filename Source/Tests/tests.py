from algorithms.algorithms import *
from domains import *
from macros import *
from predicates import *
from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError

from collections import defaultdict
import unittest

import pytest
from Examples.Triangle_problem import *

# This file was generated automatically by falcon.
# from: Tests/triangle-problem.fcn
# on 2022 Jun 03 Fri 23:46:51

values = permutations_of(values=[-1, 0, 1, 2, 3, 4, 5], repeat=3)
values2 = critical_values()

def test_classify_k2():

    groups = defaultdict(list)
    results = defaultdict(list)

    for side1ᵢ, side2ᵢ, side3ᵢ in all_triplets_of(values, n=3):

        try:
            result = classify(side1ᵢ, side2ᵢ, side3ᵢ)
        except Exception as e:
            result = e

    if not_triangle(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_instance(result, Triangle.not_triangle)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif all_equal(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_instance(result, Triangle.equilateral)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif all_different(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_instance(result, Triangle.scalene)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif two_equal(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_instance(result, Triangle.isosceles)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    else:
        raise FalconError('Failed to meet at least one group')



def test_classify_1OUcU():

    groups = defaultdict(list)
    results = defaultdict(list)

    for side1ᵢ, side2ᵢ, side3ᵢ in all_triplets_of(values, n=3):

        try:
            result = classify(side1ᵢ, side2ᵢ, side3ᵢ)
        except Exception as e:
            result = e

    if not_triangle(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_instance(result, Triangle.not_triangle)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif all_equal(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_equilateral(result)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif all_different(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_scalene(result)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    elif two_equal(side1ᵢ, side2ᵢ, side3ᵢ):
        assert is_isosceles(result)
        groups['Not-a-Triangle'].append(side1ᵢ, side2ᵢ, side3ᵢ)
        results['Not-a-Triangle'].append(result)
    else:
        raise FalconError('Failed to meet at least one group')



def test_classify_l6():

    groups = defaultdict(list)
    results = defaultdict(list)

    for s1, s2, s3 in all_triplets_of(values2, n=3):

        try:
            result = classify(s1, s2, s3)
        except Exception as e:
            result = e

    if not_positive_integers(s1, s2, s3) or not_satisfy_triangle_theorem(s1, s2, s3):
        assert not_triangle(result)
        groups['Not-a-Triangle'].append(s1, s2, s3)
        results['Not-a-Triangle'].append(result)
    elif all_equal(s1, s2, s3):
        assert is_equilateral(result)
        groups['Not-a-Triangle'].append(s1, s2, s3)
        results['Not-a-Triangle'].append(result)
    elif all_different(s1, s2, s3):
        assert is_scalene(result)
        groups['Not-a-Triangle'].append(s1, s2, s3)
        results['Not-a-Triangle'].append(result)
    elif two_equal(s1, s2, s3):
        assert is_isosceles(result)
        groups['Not-a-Triangle'].append(s1, s2, s3)
        results['Not-a-Triangle'].append(result)
    else:
        raise FalconError('Failed to meet at least one group')

