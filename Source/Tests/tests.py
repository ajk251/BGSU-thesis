from predicates import *
from domains import *

from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError
from algorithms import *
import unittest

from collections import defaultdict

from Tests.ComplexNumber import Complex
from Tests.ComplexPredicates import *

# This file was generated automatically by falcon.
# from: Tests/complex.fcn
# on 2022 Mar 14 Mon 20:57:47

A = Reals2()
B = Reals2()
CT = ComplexTestDomain()

# start test -----------------
def test_Complex_BbEBe():

    # Test the unary properties

    for aᵢ,bᵢ in A:
        assert property_additive_identity(Complex(aᵢ, bᵢ))
        assert property_multiplicative_identity(Complex(aᵢ, bᵢ))
        assert property_additive_inverse(Complex(aᵢ, bᵢ))


def test_Complex_pP53G():

    oracles = defaultdict(list)

    for aᵢ,bᵢ in CT:

        try:
            result = Complex(aᵢ, bᵢ)
        except Exception as error:
            result = error

        count = 0

        if valid_number(result):
            count += 1
            oracles['valid-complex?'].append(((aᵢ, bᵢ), repr(result)))
        if valid_complex(result):
            count += 1
            oracles['complex-num?'].append(((aᵢ, bᵢ), repr(result)))

        if count == 0:
            oracles["random-test"].append(((aᵢ, bᵢ), repr(result)))

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"

    write_to_log("./FalconTestLog.txt", {"name": Complex, "predicates": oracles})
