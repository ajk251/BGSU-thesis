
import unittest

from triangle import classify, Triangle


# The following is adapted from Foundations of Software Testing, 2ED by Mathur, pg 606

# Note: • Mathur uses ints & floats ￫ this uses ints only
#       • It has a right triangle, given the floats
#       • It returns 0, 1, 2, 3 for result ￫ not_triangle, equilateral
#       • It was orginally written in Java & JUnit

class TriangleTests(unittest.TestCase):

    def test_invalid(self):

        assert classify(1, 1, 1) == Triangle.not_triangle

    # def test_right_angled(self):

    #     assert classify(4, 4, 5.65) == Triangle.right

    def test_equilateral(self):
        
        assert classify(1, 1, 1) == Triangle.equilateral

    def test_isosceles(self):

        assert classify(1, 1, 2) == Triangle.isosceles

    def test_scalene(self):

        assert classify(1, 2, 3) == Triangle.scalene

    