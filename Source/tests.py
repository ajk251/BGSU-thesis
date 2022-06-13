from predicates import *

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/pytest-tests.fcn
# on 2021 Dec 27 Mon 18:46:22

X = Integers(-300, 100, nrandom=100)
Y = Integers(-300, 100, nrandom=100)

# start test -----------------
def test_add_agpT():

    for xᵢ, yᵢ in zip(X, Y):
        assert is_integer(add(xᵢ, yᵢ))
        assert between(add(xᵢ, yᵢ), -20, 20)
