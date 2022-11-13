from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from ComplexNumber import Complex, ComplexError
from math import nan, inf

# This file was generated automatically by Falcon.
# from: complex.fcn
# on 2022 Nov 08 Tue 11:52:16


def test_Complex_assertions_5lIL2():

    assert Complex(1.0, 1.0) == Complex(1.0, 1.0)
    assert equals(Complex(1, 1), Complex(1.0, 1.0))
    with pytest.raises(ComplexError):
        assert is_a(Complex(inf, inf))
    with pytest.raises(ComplexError):
        assert is_a(Complex(nan, nan))
    with pytest.raises(ComplexError):
        assert is_a(Complex(1.0, nan))
    with pytest.raises(ComplexError):
        assert is_a(Complex(1.0, inf))
    with pytest.raises(ComplexError):
        assert is_a(Complex(inf, 1.0))
