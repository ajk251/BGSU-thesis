
import unittest

from triangle import classify, Triangle

class TriangleTests(unittest.TestCase):

    def test_is_scalene(self):
        # conforms to: 1

        assert classify(3, 4, 5) == Triangle.scalene
        assert classify(4, 5, 3) == Triangle.scalene
        assert classify(5, 4, 3) == Triangle.scalene

        # self.assertTrue(classify(3, 4, 5), Triangle.scalene)

    def test_is_equilateral(self):
        # conforms to: 2

        assert classify(4, 4, 4) == Triangle.equilateral

    def test_is_isosceles(self):
        # conforms to: 3, 4

        assert classify(4, 4, 7) == Triangle.isosceles
        assert classify(4, 7, 4) == Triangle.isosceles
        assert classify(7, 4, 4) == Triangle.isosceles

    def test_bad_values(self):
        # conforms to: 5, 6

        assert classify(0, 1, 2) == Triangle.not_triangle
        assert classify(-1, 3, 4) == Triangle.not_triangle

    def test_violate_triangle_theorem(self):
        # conforms to: 7,8,9,10

        # 3 ints where length of one side is equal to the sum of the lengths
        assert classify(1, 2, 3) == Triangle.not_triangle
        assert classify(2, 1, 3) == Triangle.not_triangle
        assert classify(3, 1, 2) == Triangle.not_triangle

        # 3 ints where length of one side is less-than to the sum of the lengths
        assert classify(1, 2, 4) == Triangle.not_triangle
        assert classify(12, 15, 30) == Triangle.not_triangle
        assert classify(5, 2, 8) == Triangle.not_triangle

        # 10 - 3 permutations of above
        assert classify(1, 4, 2) == Triangle.not_triangle
        assert classify(4, 1, 2) == Triangle.not_triangle

    def test_all_zeros(self):
        # conforms to: 11

        assert classify(0, 0, 0) == Triangle.not_triangle
     
if __name__ == '__main__':
    unittest.main()
