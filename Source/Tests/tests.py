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
# on 2022 Mar 23 Wed 12:15:27

A = Reals2()
B = Reals2()
CT = ComplexTestDomain()

# start test -----------------
def test_Complex_aFnS():

    # Test the unary properties

    for aᵢ,bᵢ in A:
        assert valid_number(Complex(aᵢ, bᵢ))
        assert valid_complex(Complex(aᵢ, bᵢ))
        assert property_additive_identity(Complex(aᵢ, bᵢ))
        assert property_multiplicative_identity(Complex(aᵢ, bᵢ))
        assert property_additive_identity(Complex(aᵢ, bᵢ))

C1 = ComplexDomain()
C2 = ComplexDomain()

# start test -----------------
def test___sE():

    # Test the properties of Complex numbers

    for c1ᵢ, c2ᵢ in zip(C1, C2):
        assert property_closure_add(c1ᵢ, c2ᵢ)
        assert property_closure_multiply(c1ᵢ, c2ᵢ)
        assert property_commutative_add(c1ᵢ, c2ᵢ)
        assert property_commutative_multiply(c1ᵢ, c2ᵢ)
        assert property_multiplicative_inverse(c1ᵢ, c2ᵢ)


# start test -----------------
def test___Xk():

    # Test the mathematical properties

    for c1, c2 in zip(C1, C2):
        assert complex_add(c1, c2)
        assert complex_sub(c1, c2)
        assert complex_mult(c1, c2)
        assert complex_radd(c1, c2)
        assert complex_rsub(c1, c2)
        assert complex_rmul(c1, c2)
        c = c1 + c2
        assert valid_number(c)
        assert valid_complex(c)


def test_Complex_MTC():

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
            oracles['complex-number?'].append(((aᵢ, bᵢ), repr(result)))

        if count == 0:
            oracles["random-test"].append(((aᵢ, bᵢ), repr(result)))

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"

    write_to_log("./FalconTestLog.txt", {"name": Complex, "predicates": oracles})
