from predicates import *

from test_functions import add

# This file was generated automatically by falcon.
# from: Tests/initial-tests.fcn
# on 2021 Dec 03 Fri 14:57:45

X = Integers(-1000, 1000)
Y = Integers(-500, 500)

# start test -----------------

def test_add():
    for xᵢ, yᵢ in zip(X, Y):
        assert between(add(xᵢ, yᵢ), -1500, 1500)
