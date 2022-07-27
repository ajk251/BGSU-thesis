from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest
from ComplexPredicates import *
from ComplexNumber import Complex, ComplexError

# This file was generated automatically by Falcon.
# from: complex.fcn
# on 2022 Jul 27 Wed 13:40:58

# [ComplexNumber, ComplexPredicates]
CT = ComplexTestDomain()

def test_satisfy_Complex_uQPIC():

    for r, i in CT:

        try:
            result = Complex(r, i)
        except Exception as error:
            result = error

        count = 0

        if valid_number(result):
            count += 1
        if valid_complex(result):
            count += 1
        if valid_number(result):
            count += 1
        if property_additive_identity(result):
            count += 1
        if property_multiplicative_identity(result):
            count += 1
        if raises_error(result, ComplexError):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1  [with {result}]"
        assert count <= 5, f"Exceed number of predicates met - met: {count}, max: 5"
