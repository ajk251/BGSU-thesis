
from dataclasses import dataclass
from numbers import Number
from typing import Type, Union, TypeVar, Tuple
from operator import eq, ne

# -----------------------------------------------

class Complex:

    __slots__ = ('n', 'i')

    def __init__(self, n: float, i: float):
        self.n: float = float(n)
        self.i: float = float(i)

    def __str__(self):
        return f'ℂ {round(self.n, 3)}+{round(self.i, 4)}𝑖'

    def __repr__(self):
        return f'Complex<{round(self.n, 2)},{round(self.i, 2)}𝑖>'

    def __hash__(self):
        return hash(self.n ** self.i)

    # ------------------

    def __add__(self, other: 'Complex'):
        return Complex(self.n + other.n, self.i + other.i)

    def __sub__(self, other: 'Complex'):
        return Complex(self.n - other.n, self.i - other.i)

    def __mult__(self, other: 'Complex'):
        return Complex(self.n * other.n, self.i * other.i)

    def __div__(self, other: 'Complex'):
        raise NotImplementedError

    # ------------------

    # def __radd__(self, other):

    #     if isinstance(other, Complex):
    #         self.n += other.n
    #         self.i += other.i
    #     else:
    #         self.n += float(other)

    #     return self

    # ------------------

    def __eq__(self, other: 'Complex'):
        return self.n == other.n and self.i == other.i

    def __ne__(self, other: 'Complex'):
        return self.n != other.n and self.i != other.i

    def __lt__(self, other: 'Complex'):
        return self.n < other.n and self.i < other.i

    def __le__(self, other: 'Complex'):
        return self.n <= other.n and self.i <= other.i

    def __gt__(self, other: 'Complex'):
        return self.n > other.n and self.i > other.i

    def __ge__(self, other: 'Complex'):
        return self.n >= other.n and self.i >= other.i

    def increment(self, n=0.0, i=0.0):
        self.n += float(n)
        self.i += float(i)
        return self

# -----------------------------------------------

def successor(c: Complex):
    return c + Complex(1.0, 1.0)

def predecessor(c: Complex):
    return c - Complex(1.0, 1.0)

# -----------------------------------------------

is_unique = lambda a,b: id(a) != id(b)

# -----------------------------------------------

print(Complex(2.3, 4.5))

c1 = Complex(2.3, 4.5)
c2 = Complex(5.23, 10.5)
c3 = c1 + c2

print(c3)
print(c2 < c1)
print(c2 > c1)
print(successor(c3))
print(predecessor(c3))

c3.increment(100, 0)
print(c3)

print('is unique: ', is_unique(c1, c2))
print('is unique: ', is_unique(c1, c1))