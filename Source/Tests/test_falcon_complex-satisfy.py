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
from ComplexPredicates import *
from math import nan, inf

# This file was generated automatically by Falcon.
# from: complex-satisfy.fcn
# on 2022 Aug 05 Fri 21:02:43

CT = ComplexTestDomain()

def test_satisfy_Complex_f0h():

    for r, i in CT:

        try:
            result = Complex(r, i)
        except Exception as error:
            result = error

        count = 0

        if is_error_and_contains(result, 'Real'):
            count += 1
        if is_error_and_contains(result, 'Imaginary'):
            count += 1
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

        assert count in (1, 5), 'Count must be 1 of 1, 5'

values = permutations_of(values=[nan, inf, 1, 1.0])

def test_satisfy_Complex_cXar():

    for r, i in values:

        try:
            result = Complex(r, i)
        except Exception as error:
            result = error

        count = 0

        if valid_number(result):
            count += 1
        if valid_complex(result):
            count += 1
        if is_error_and_contains(result, 'Real'):
            count += 1
        if is_error_and_contains(result, 'Imaginary'):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"
