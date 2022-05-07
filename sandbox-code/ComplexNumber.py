
from numbers import Number

class Complex(Number):

    def __init__(self, real: float, imaginary: float=0.0):
        self.n = real
        self.j = imaginary

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
        return f'Complex<{self.n:.3f},{self.j:.3f}𝑗>'

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


# print('-' * 25)

# from random import uniform

# for _ in range(100):

#     c1 = (uniform(-100., 100), uniform(-100.0, 100))
#     c2 = (uniform(-100., 100), uniform(-100.0, 100))

#     print('\nMath')
#     print('+ ', complex_add(c1, c2))
#     print('- ', complex_sub(c1, c2))
#     print('⨯ ', complex_mult(c1, c2))
    
#     a = Complex(uniform(-100., 100), uniform(-100., 100))
#     b = Complex(uniform(-100., 100), uniform(-100., 100))
#     c = Complex(uniform(-100., 100), uniform(-100., 100))
    
#     print('\n', a, b, c)
#     print('Valid?  ', valid_complex(a), valid_complex(b), valid_complex(c))
#     print('Number? ', valid_number(a), valid_number(b), valid_number(c))

#     print('-= ', complex_rsub(a, b))

#     print('\nUnary')
#     print(property_additive_identity(a))
#     print(property_multiplicative_identity(a))
#     print(property_additive_inverse(a))
#     print(property_multiplicative_inverse(a))

#     print('\nBinary')
#     print(property_closure_add(a, b))
#     print(property_closure_multiply(a, b))
#     print(property_commutative_add(a, b))
#     print(property_commutative_multiply(a, b))
    
#     print('\nDistributative')
#     print(property_distributive(a, b, c))

#     print('\n', '*' * 10, '\n')
#     print(a, -a, a + -a, a + -a == Complex(0.0, 0.0))