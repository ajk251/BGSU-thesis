from predicates import *
from domains import *

from algorithms import *
import unittest


# This file was generated automatically by falcon.
# from: Tests/unit-tests.fcn
# on 2021 Dec 23 Thu 17:12:55

x = [1, 2, 3]
y = [4, 5, 6]

X = Integers(-1000, 1000, nrandom=10)
Y = Integers(-500, 500, nrandom=10)
Z = Reals(0, 100)

class Test(unittest.TestCase):

    def test_add(self):

        # please work

        for xᵢ, yᵢ in ART(X, Y):
            assert is_integer(add(xᵢ, yᵢ))
            assert between(add(xᵢ, yᵢ), -1500, 1500)

    def test_logical_floats(self):

        # 'here I am testing to see if it works'

        for xᵢ, yᵢ, zᵢ in ART(X, Y, Z, initial=[0, 0, 0], max_tests=10):
            assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) or not is_float(logical(xᵢ, yᵢ, zᵢ)))
            assert logical(xᵢ, yᵢ, zᵢ) < 4 or between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
            assert is_modulus_of(logical(xᵢ, yᵢ, zᵢ), 10)
            assert between(logical(xᵢ, yᵢ, zᵢ), 0, 100)
            assert is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ))
            assert not (not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ)))
            assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not is_float(logical(xᵢ, yᵢ, zᵢ))
            assert (is_integer(logical(xᵢ, yᵢ, zᵢ)) and is_float(logical(xᵢ, yᵢ, zᵢ)))
            assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and (is_float(logical(xᵢ, yᵢ, zᵢ)) or is_fraction(logical(xᵢ, yᵢ, zᵢ)))
            assert not is_integer(logical(xᵢ, yᵢ, zᵢ)) and not (logical(xᵢ, yᵢ, zᵢ) > 8 and logical(xᵢ, yᵢ, zᵢ) < 10 and logical(xᵢ, yᵢ, zᵢ) == 9)
            assert is_integer(logical(xᵢ, yᵢ, zᵢ)) or is_float(logical(xᵢ, yᵢ, zᵢ)) or not is_fraction(logical(xᵢ, yᵢ, zᵢ)) and logical(xᵢ, yᵢ, zᵢ) > 0

    def test_groupby_fna(self):

        for xᵢ, yᵢ in zip(X, Y):

            try:
                result = fna(xᵢ, yᵢ)
            except Exception as e:
                assert False, "Function error"
                continue
                
            try:
                group = fn_to_b(result)
            except Exception as e_bin:
                assert False, "Group-by error"   
                continue
    
            if group == 'A':
                assert is_float(result)
            elif group == 'B':
                assert between(result, 0, 1)
            else:
                print("You shouldn't be here!") 		# TODO…

    def test_groupby_fnb(self):

        for xᵢ, yᵢ in zip(X, Y):

            try:
                result = fnb(xᵢ, yᵢ)
                group = result
            except Exception as e:   
                assert False, "Function error"
                continue

            if group == C:
                assert is_integer(result)
            elif group == D:
                assert between(result, -50, 50)
            else:
                print("You shouldn't be here!") 		# TODO…

    def test_satisfy_fnc(self):

        for xᵢ, yᵢ in zip(X, Y):

            count = 0

            try:
                result = fnc(xᵢ, yᵢ)
                group = result
            except Exception as e:   
                assert False, "Function error"
                continue

            if group == 'E':
                assert is_fraction(result)
                count += 1
            if group == 'F':
                assert between(result, Fraction(1,3), Fraction(2,3))
                count += 1
            assert count >= 1, f"Case {xᵢ,yᵢ} did not satisfy at least 1 case"

