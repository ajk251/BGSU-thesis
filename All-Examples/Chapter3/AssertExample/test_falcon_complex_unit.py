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

from ComplexNumber import Complex, ComplexError
from math import nan, inf

# This file was generated automatically by Falcon.
# from: complex.fcn
# on 2022 Nov 13 Sun 14:59:04


class Test(unittest.TestCase):

    def test_Complex_assertions_6VPw(self):

        assert eq(Complex, (1.0, 1.0), Complex(1.0, 1.0))
        assert equals(Complex(1, 1), Complex(1.0, 1.0))
        with pytest.raises(ComplexError):
            assert equals(Complex((1, 1)))
        with pytest.raises(ComplexError):
            assert equals(Complex((1, 1)))
        with pytest.raises(ComplexError):
            assert equals(Complex((1, 1)))
        with pytest.raises(ComplexError):
            assert equals(Complex((1, 1)))
        with pytest.raises(ComplexError):
            assert equals(Complex((1, 1)))