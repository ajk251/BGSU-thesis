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
from Tests.ComplexNumber import Complex
from Tests.ComplexPredicates import *

# This file was generated automatically by falcon.
# from: Tests/assert2.fcn
# on 2022 May 27 Fri 15:05:08


def test_Complex_assertions_4U0hB():

    assert catch_error(Complex, (nan, 1.0), AssertionError)
    assert catch_error_message(Complex, (inf, inf), Exception, "Value must be a float")

def test_Complex_assertions_Ps():

    assert Complex(1.0, 1.0) == ('=', 'Complex(1.0, 1.0)')
    assert Complex(1, 1) == ('=', 'Complex(1.0, 1.0)', None, None), "This should never fail"
    assert Complex(10.0, 10.0) < ('<', 'Complex(20.0, 20.0)')
    assert catch_error(Complex, (nan, 1.0), AssertionError)
    assert between(Complex(1.0, 1.0), -1.0, 1.0)
    assert catch_error_message(Complex, (inf, inf), Exception, "Value must be a float")
    assert is_complex(Complex(1.0, 0.0)) or is_float(Complex(1.0, 0.0))
    with pytest.raises(TypeError):
        assert is_a(Complex(inf, inf))
    with pytest.raises(Exception):
        assert is_a(Complex(nan, nan))
    with pytest.raises(Exception):
        assert between(Complex(nan, inf), -1, 1)
    with pytest.raises(TypeError):
        assert between(Complex(nan, inf), -1, 1)
vals = ART()

# start test -----------------
def test_Complex_Vx():

    for valsᵢ in vals:
        assert is_integer(Complex(valsᵢ))
