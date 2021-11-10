import unittest

# This file was generated automatically by falcon.
# from: Tests/namespace-test.fcn
# on 2021 Nov 10 Wed 13:12:42

x = [1,2,3]
y = [4,5,6]

def fn(a, b, three=None, four=None):
    pass

# Assertion test -------------
assert fn(1, 2, 3) > 4
assert fn(1, 2, three=3, four=4) != 5
assert fn(1, [2.0], three=3.0) is True

class ns_test_1(unittest.TestCase):

    # "Tests fn over D"


class Ns_1A(unittest.TestCase):

