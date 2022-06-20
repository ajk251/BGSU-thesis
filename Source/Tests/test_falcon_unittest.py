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
from Tests.ComplexNumber import Complex
from Tests.ComplexPredicates import *

# This file was generated automatically by falcon.
# from: Tests/assert2.fcn
# on 2022 Jun 20 Mon 18:30:21


class Test(unittest.TestCase):

    def test_Complex_assertions_flu0D(self):

        assert raises_error(Complex(nan, 1.0), AssertionError)
        assert is_error_and_says(Complex(inf, inf), Exception, "Value must be a float")

    def test_Complex_assertions_Nle1U(self):

        assert eq(Complex, (1.0, 1.0), Complex(1.0, 1.0))
        assert eq(Complex, (1, 1), Complex(1.0, 1.0))
        assert lt(Complex, (10.0, 10.0), Complex(20.0, 20.0))
        assert raises_error(Complex(nan, 1.0), AssertionError)
        assert between(Complex(1.0, 1.0), -1.0, 1.0)
        assert is_error_and_says(Complex(inf, inf), Exception, "Value must be a float")
        assert is_complex(Complex(1.0, 0.0), False, False, False) or is_float(Complex(1.0, 0.0), False, False, False)
        with pytest.raises(TypeError):
            assert is_error_and_says(Complex(1.0, 0.0))
        with pytest.raises(Exception):
            assert is_error_and_says(Complex(1.0, 0.0))
        with pytest.raises(Exception):
            assert is_error_and_says(Complex(1.0, 0.0), -1, 1)
        with pytest.raises(TypeError):
            assert is_error_and_says(Complex(1.0, 0.0), -1, 1)

