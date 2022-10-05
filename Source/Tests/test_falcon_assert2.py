from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from ComplexNumber import Complex
from ComplexPredicates import *

# This file was generated automatically by Falcon.
# from: assert2.fcn
# on 2022 Aug 29 Mon 14:30:50


def test_Complex_assertions_0G4yY():

    assert Complex(1.0, 1.0) == Complex(1.0, 1.0)
    assert Complex(1, 1) == Complex(1.0, 1.0)
    assert Complex(10.0, 10.0) < Complex(20.0, 20.0)
    assert raises_error(Complex(nan, 1.0), AssertionError)
    assert between(Complex(1.0, 1.0), -1.0, 1.0)
    assert is_error_and_says(Complex, (inf, inf), Exception, "Value must be a float")
    assert is_complex(Complex(1.0, 0.0)) or is_float(Complex(1.0, 0.0))
    with pytest.raises(TypeError):
        assert is_a(Complex(inf, inf))
    with pytest.raises(Exception):
        assert is_a(Complex(nan, nan))
    with pytest.raises(Exception):
        assert between(Complex(nan, inf), -1, 1)
    with pytest.raises(TypeError):
        assert between(Complex(nan, inf), -1, 1)
    assert Complex(2, 2) == Complex(2.0, 2.0)


def test_Complex_assertions_Oy0WJ():

    assert raises_error(Complex(nan, 1.0), AssertionError)
    assert is_error_and_says(Complex, (inf, inf), Exception, "Value must be a float")
    x = Complex(1.0, 1.0)
    assert is_int(x)
    assert between(x, 1.0, 10.0)
    assert x > 10
