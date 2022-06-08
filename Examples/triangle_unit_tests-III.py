
import unittest

from triangle import classify, Triangle

# The following is based on Software Testing: A Craftsman's Approach 4ED by Jorgensen
# I've used the examples from pages 105/106, 191, 122

# Note: • Jorgensen has several triangle examples
#       • he places bounds on the integers, < 200
#       • on 122, he tests the impossible classify(?, ? , ?)


class TriangleTests(unittest.TestCase):


    def test_invalid(self):
        
        # from 105
        # assert classify(4, 1, 2)  == Triangle.not_triangle
        # assert classify(-1, 5, 5) == Triangle.not_triangle
        # assert classify(5, -1, 5) == Triangle.not_triangle
        # assert classify(5, 5, -1) == Triangle.not_triangle

        # from 191
        assert classify(100, 100, 200) == Triangle.not_triangle
        assert classify(100, 200, 100) == Triangle.not_triangle
        assert classify(200, 100, 100) == Triangle.not_triangle

        # from 122
        assert classify(4, 1, 2) == Triangle.not_triangle
        assert classify(1, 4, 2) == Triangle.not_triangle
        assert classify(1, 2, 4) == Triangle.not_triangle


    def test_equilateral(self):
        
        # from 105 & 122
        # assert classify(5, 5, 5) == Triangle.equilateral

        assert classify(100, 100, 100) == Triangle.equilateral  # he repeats this 3 times‽


    def test_isosceles(self):

        # from 105
        # assert classify(2, 2, 3) == Triangle.isosceles

        # from 191
        assert classify(100, 100, 1) == Triangle.isosceles
        assert classify(100, 100, 2) == Triangle.isosceles
        assert classify(100, 100, 199) == Triangle.isosceles
        assert classify(100, 1, 100) == Triangle.isosceles
        assert classify(100, 2, 100) == Triangle.isosceles
        assert classify(100, 199, 100) == Triangle.isosceles
        assert classify(1, 100, 100) == Triangle.isosceles
        assert classify(2, 100, 100) == Triangle.isosceles
        assert classify(199, 100, 100) == Triangle.isosceles

        # from 122
        assert classify(2, 2, 3) == Triangle.isosceles
        assert classify(2, 3, 2) == Triangle.isosceles
        assert classify(3, 2, 2) == Triangle.isosceles

    def test_scalene(self):
        
        # from 105 & 122
        assert classify(3, 4, 5) == Triangle.scalene