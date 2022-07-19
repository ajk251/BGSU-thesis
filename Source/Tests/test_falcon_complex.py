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
# on 2022 Jul 19 Tue 14:28:39

A = Reals2()
B = Reals2()
lower = integers(lower=0, upper=100)
upper = integers(lower=-100, upper=100)
critical = CSVDomain('./tests/special-case.txt')

def test_Complex_assertions_ERo():

    assert eq(Complex(1.0, 1.0), Complex(1.0, 1.0))
    assert eq(Complex(1, 1), Complex(1.0, 1.0)), "This should never fail"
    assert lt(Complex(10.0, 10.0), Complex(20.0, 20.0))
    assert is_error(Complex(nan, 1.0), AssertionError)
    assert between(Complex(1.0, 1.0), -1.0, 1.0)
    assert is_error_and_contains(Complex(inf, inf), Exception, "Value must be a float")
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
def test_Complex_hn():

    # Test the unary properties blah blah blah

    for a, b in A:
        assert not (is_none(Complex))
        with pytest.raises(Exception):
            assert valid_number(Complex)
        with pytest.raises(ZeroDivisionError):
            assert valid_number(Complex)
        with pytest.raises(TypeError):
            assert between(Complex, -10, 10)
        with pytest.raises(Exception):
            assert between(Complex, 1, 2)
        assert valid_number(Complex)
        assert valid_complex(Complex)
        assert property_additive_identity(Complex)
        assert property_multiplicative_identity(Complex)
        assert property_additive_identity(Complex)
        assert complex_div(Complex)

C1 = ComplexDomain()
C2 = ComplexDomain()

# start test -----------------
def test___aCFY():

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
def test___qk():

    # Test the mathematical properties

    for c1, c2 in zip(C1, C2):
        assert complex_add(c1, c2)
        assert complex_sub(c1, c2)
        assert complex_mult(c1, c2)
        assert complex_radd(c1, c2)
        assert complex_rsub(c1, c2)
        assert complex_rmul(c1, c2)

CT = ComplexTestDomain()

def test_Complex_qASI():

    for r,i in CT:

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

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1  [with {result}]"
