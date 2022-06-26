from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict
import unittest

import pytest
from ThesisExamples.Triangle_problem import *

# This file was generated automatically by falcon.
# from: ThesisExamples/FalconMotivation.fcn
# on 2022 Jun 26 Sun 19:32:15

values = permutations_of(values=[-1, 0, 1, 2, 3, 4, 5], repeat=3)

# this is code

# This is a code block
even = lambda n: n % 2 == 0

def test_classify_hw():

    for side1ᵢ, side2ᵢ, side3ᵢ in zip(values):

        try:
            result = classify(side1ᵢ, side2ᵢ, side3ᵢ)
        except Exception as e:
            result = e

        if not_triangle(side1ᵢ, side2ᵢ, side3ᵢ):
            assert is_instance(result, Triangle.not_triangle)
        elif all_equal(side1ᵢ, side2ᵢ, side3ᵢ):
            assert is_instance(result, Triangle.equilateral)
        elif all_different(side1ᵢ, side2ᵢ, side3ᵢ):
            assert is_instance(result, Triangle.scalene)
        elif two_equal(side1ᵢ, side2ᵢ, side3ᵢ):
            assert is_instance(result, Triangle.isosceles)
        else:
            raise FalconError('Failed to meet at least one group')

