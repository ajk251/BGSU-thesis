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
from ComplexPredicates import *

# This file was generated automatically by Falcon.
# from: complex2.fcn
# on 2022 Nov 13 Sun 18:10:58

CT = ComplexTestDomain()

def test_satisfy_Complex_hCw():

    for real, im in CT:

        try:
            result = Complex(real, im)
        except Exception as error:
            result = error

        count = 0

        if valid_number(result):
            count += 1
        if valid_complex(result):
            count += 1
        if property_additive_identity(result):
            count += 1
        if property_multiplicative_identity(result):
            count += 1
        if raises_error(result, ComplexError):
            count += 1

        assert count in (4, 1), 'Count must be 1 of 4, 1'
