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
# from: Tests/complex.fcn
# on 2022 May 26 Thu 15:09:47

A = Reals2()
B = Reals2()
# not implemented yet
lower = Integers(lower=0, upper=100)
upper = Integers(lower=-100, upper=100)
critical = CSVDomain('./tests/special-case.txt')

def test_Complex_assertions_Py5Y():

    assert Complex(1.0, 1.0) == ('=', 'Complex(1.0, 1.0)')
    assert Complex(1, 1) == ('=', 'Complex(1.0, 1.0)', None, None), "This should never fail"
    assert Complex(10.0, 10.0) < ('<', 'Complex(20.0, 20.0)')
    assert catch_error(Complex(nan, 1.0), ('raises?', 'AssertionError'))
    assert between(Complex(1.0, 1.0), -1.0, 1.0)
    assert catch_error_message(Complex(inf, inf), Exception, "Value must be a float")
    assert is_complex(Complex(1.0, 0.0)) or is_float(Complex(1.0, 0.0))
    with pytest.raises(TypeError):
        assert is_a(Complex(inf, inf))
    with pytest.raises(Exception):
        assert is_a(Complex(nan, nan))
    with pytest.raises(Exception):
        assert between(Complex(nan, inf), -1, 1)
    with pytest.raises(TypeError):
        assert between(Complex(nan, inf), -1, 1)

# start test -----------------
def test_Complex_EISde():

    # Test the unary properties blah blah blah

    for aᵢ,bᵢ in A:
        assert not (is_none(Complex(aᵢ, bᵢ)))
        with pytest.raises(Exception):
            assert valid_number(Complex(aᵢ, bᵢ))
        with pytest.raises(ZeroDivisionError):
            assert valid_number(Complex(aᵢ, bᵢ))
        with pytest.raises(TypeError):
            assert between(Complex(aᵢ, bᵢ), -10, 10)
        with pytest.raises(Exception):
            assert between(Complex(aᵢ, bᵢ), 1, 2)
        assert valid_number(Complex(aᵢ, bᵢ))
        assert valid_complex(Complex(aᵢ, bᵢ))
        assert property_additive_identity(Complex(aᵢ, bᵢ))
        assert property_multiplicative_identity(Complex(aᵢ, bᵢ))
        assert property_additive_identity(Complex(aᵢ, bᵢ))

C1 = ComplexDomain()
C2 = ComplexDomain()

# start test -----------------
def test___KXgq():

    # Test the properties of Complex numbers

    for c1, c2 in zip(C1, C2):
        assert property_closure_add(c1, c2)
        assert property_closure_multiply(c1, c2)
        assert property_commutative_add(c1, c2)
        assert property_commutative_multiply(c1, c2)
        assert property_multiplicative_inverse(c1, c2)
        with pytest.raises(Exception):
            assert property_closure_add(c1, c2)
        with pytest.raises(TypeError):
            assert property_closure_add(c1, c2)


# start test -----------------
def test___LW():

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

CT = ComplexTestDomain()

def test_Complex_sCnX():

    oracles = defaultdict(list)

    for aᵢ,bᵢ in CT:

        try:
            result = Complex(aᵢ, bᵢ)
        except Exception as error:
            result = error

        count = 0

        if valid_number(result()):
            count += 1
            oracles['valid-complex?'].append(((aᵢ, bᵢ), repr(result)))
        if valid_complex(result()):
            count += 1
            oracles['complex-number?'].append(((aᵢ, bᵢ), repr(result)))

        if count == 0:
            oracles["random-test"].append(((aᵢ, bᵢ), repr(result)))

        assert count <= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"

    write_to_log("./FalconTestLog.txt", {"name": Complex, "predicates": oracles})
