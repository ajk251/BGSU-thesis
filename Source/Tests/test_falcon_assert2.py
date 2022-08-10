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
# on 2022 Aug 10 Wed 18:40:30


def test_Complex_assertions_hdEM():

    assert raises_error(Complex(nan, 1.0), AssertionError)
    assert is_error_and_says(Complex, (inf, inf), Exception, "Value must be a float")
    x = Complex(1.0, 1.0)
    assert is_int(x)
    assert between(x, 1.0, 10.0)
    assert x < 10
