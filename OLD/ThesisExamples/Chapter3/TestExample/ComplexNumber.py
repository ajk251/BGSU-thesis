
from math import isinf, isnan
from numbers import Number


class ComplexError(Exception):
    pass


class Complex(Number):

    __slots__ = ('n', 'j')

    def __init__(self, real: float, imaginary: float = 0.0):

        if isnan(real) or isinf(real):
            raise ComplexError('Real component cannot be nan or inf')
        if isnan(imaginary) or isinf(imaginary):
            raise ComplexError('Imaginary component cannot be nan or inf')

        self.n = float(real)
        self.j = float(imaginary)

    @property
    def real(self):
        return self.n

    @property
    def imaginary(self):
        return self.j

    def __hash__(self):
        return hash(self.n ^ self.j)

    def __str__(self):
        return f'ℂ {self.n:.3f}+{self.j:.3f}𝑗'

    def __repr__(self):
        return f'Complex<{self.n:.3f},{self.j:.3f}j>'

    def __eq__(self, other):
        return self.n == other.n and self.j == other.j

    def __ne__(self, other):
        return self.n != other.n and self.j != other.j

    def __neg__(self):
        return Complex(-self.n, -self.j)

    def __invert__(self):
        return Complex( self.n / (self.n**2 + self.j**2), -self.j / (self.n**2 + self.j**2))

    def __add__(self, other):
        return Complex(self.n + other.n, self.j + other.j)

    def __radd__(self, other):
        self.n += other.n
        self.j += other.j

    def __sub__(self, other):
        return Complex(self.n - other.n, self.j - other.j)

    def __rsub__(self, other):
        self.n -= other.n
        self.j -= other.j

    def __mul__(self, other):
        return Complex(self.n * other.n, self.j * other.j)

    def __rmul__(self, other):
        self.n *= other.n
        self.j *= other.j

    def __div__(self, other):
        raise NotImplementedError('"div" is not implemented.')

    def __rdiv__(self, other):
        raise NotImplementedError('"rdiv" is not yet implemented')
