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
# from: complex.fcn
# on 2022 Jul 28 Thu 12:56:06

R2 = Reals2()
def test_Complex_mrvb():
    # The unary properties of the complex numbers

    for real, im in R2:
        assert valid_number(Complex(real, im))
        assert valid_complex(Complex(real, im))
        assert property_additive_identity(Complex(real, im))
        assert property_multiplicative_identity(Complex(real, im))
