
from collections import defaultdict, namedtuple
from itertools import chain, product


#Triangle = Enum('Triagle', 'equilateral, isosceles, scalene, not_triangle')
Triangle = namedtuple('Triagle', 'equilateral, isosceles, scalene, not_triangle')
# Triangle = Type('Triangle', 'equilateral, isosceles, scalene, not_triangle')

class TriangleError(Exception): pass

def classify(a, b, c):

    is_triangle = lambda a_,b_,c_: (a < b+c) and (b < a+c) and (c < a+b)
    integers    = lambda a_,b_,c_: isinstance(a_, int) and isinstance(b_, int) and isinstance(c_, int)
    is_valid    = lambda a_,b_,c_: (a_ > 0) and (b_ > 0) and (c_ > 0)      

    assert integers(a, b, c), "All values must be integers"

    if not is_triangle(a, b, c): # and not is_valid(a, b, c):
        # print('sides too short ', end='')
        #return Triangle.not_triangle
        return 'not-triangle'
    elif not is_valid(a, b, c):
        # print('not a valid triangle ', end='')
        # return Triangle.not_triangle
        return 'not-triangle'
    elif a == b and b == c:
        # return Triangle.equilateral
        return 'equilateral'
    elif a != b and b != c and c != a:
        # return Triangle.scalene
        return 'scalene'
    elif a == b or b == c or a == c:
        # return Triangle.isosceles
        return 'isosceles'

    raise TriangleError('Could not classify input a -> %d, b -> %d, c  -> %d' % (a, b, c))


# print(classify(1, 1, 1))
# print(classify(2, 3, 4))
# print(classify(3, 3, 2))
# print(classify(1, 2, -1))
# print(classify('a', 'b', 'c'))


def all_triplets(*sequences):
    """Generates all triplets from the sequences"""
    # source: https://www.geeksforgeeks.org/python-all-pair-combinations-of-2-tuples/
    return chain(product(*sequences), product(*sequences), product(*sequences))

def all_triplets_of(sequence, n=3):
    """Builds n-copies of a sequence and generates all triplets"""
    return all_triplets(*(sequence for _ in range(n)))

# ---------------------------------------------------------

def positive_integers(a, b, c):
    """Tests that all values are positive integers"""
    if not (isinstance(a, int) and a > 0):
        return False

    if not (isinstance(b, int) and b > 0):
        return False

    if not (isinstance(c, int) and c > 0):
        return False

    return True


def satisfy_triangle_theorem(a, b, c):
    """The Triangle Theorem, ie. si < s2+s3, for all sides"""
    return (a < b+c) and (b < a+c) and (c < a+b)


def is_equalateral(a, b, c):
    """Triangle where all sides are equal"""
    return a == b and b == c


def is_isocoles(a, b, c):
    """Triangle where two sides are equal"""
    return a == b or b == c or a == c


def is_scalene(a, b, c):
    """Triangle where 3 sides are different"""
    return a != b and b != c and a != c
 
