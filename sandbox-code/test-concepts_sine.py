
from decimal import Decimal, Context
from math import factorial, isclose, sin, pi


# from: https://www.piday.org/million/
#       https://www.mymathtables.com/trigonometric/sine-tables-0-to-90.html


# https://docs.python.org/3/library/decimal.html
# http://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-sinx/
# https://en.wikipedia.org/wiki/Sine

def bhaskara(x, precision=50):

    # from:
    #   https://datagenetics.com/blog/july12019/index.html
    
    con = Context(prec=precision)

    π = Decimal('3.1415926535897932384626433832795028841971693993751058209749445')
    x = Decimal(x)
    return (16 * x * (π - x)) / (5 * con.power(π, Decimal(2)) - 4 * x * (π - x))

# -----------------------------------------------

# From book: Annotated Algorithms in Python, CH 4, 4.3+

def _sin(x: Decimal, con, iterations: int):
    
    t = x
    s = x

    for k in range(1, iterations):
        t = t * (-1) * x * x / (2 * k) / (2 * k + 1)  
        s += t
        # ε = con.power(x, 2*k+1)

    # print('error: ', ε)
    return s


def sine(x, precision=100, iterations=1000, in_degrees=False):

    # in radians…

    #      (-1)^n     2n+1
    #  Σ  -------- x^
    #      (2n+1)!

    con = Context(prec=precision)

    # Constants
    zero = Decimal('0.0')
    one = Decimal('1.0')
    two = Decimal('2.0')
    π = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    τ = two * π
    π2 = con.divide(π, two)
    π4 = con.divide(π, two * two)
    π180 = con.divide(π, Decimal('180.0'))

    x = Decimal(x)

    if in_degrees:
        x = x * π180
    
    if x == zero:  return zero
    elif x < zero: return -_sin(-x, con, iterations)
    elif x > two:  return _sin(x % τ, con, iterations)
    elif x > π2:   return _sin(π - x, con, iterations)
    elif x > π4:   return con.sqrt(one - con.power(_sin(π2-x, con, iterations), two))
    
    return _sin(x, con, iterations)

# -----------------------------------------------

# from: http://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-sinx/

def _sin2(x: Decimal, con, iterations: int):
    
    o = Decimal('-1')
    x = Decimal(x)

    for k in range(3, iterations, 2):
        x += o * (con.power(x, k) / Decimal(factorial(k)))
        o *= -1
        # print(f'x={x}  0={o}')

    return x


def sine2(x, precision=100, iterations=50, in_degrees=False):

    # in radians…

    #      (-1)^n     2n+1
    #  Σ  -------- x^
    #      (2n+1)!

    con = Context(prec=precision)

    # Constants
    zero = Decimal('0.0')
    one = Decimal('1.0')
    two = Decimal('2.0')
    π = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    τ = two * π
    π2 = con.divide(π, two)
    π4 = con.divide(π, two * two)
    π180 = con.divide(π, Decimal('180.0'))

    x = Decimal(x)

    if in_degrees:
        x = x * π180
    
    if x == zero:  return zero
    elif x < zero: return -_sin(-x, con, iterations)
    elif x > two:  return _sin(x % τ, con, iterations)
    elif x > π2:   return _sin(π - x, con, iterations)
    elif x > π4:   return con.sqrt(one - con.power(_sin(π2-x, con, iterations), two))
    
    return _sin2(x, con, iterations)

# -----------------------------------------------

π = Decimal('3.1415926535897932384626433832795028841971693993751058209749445')
τ = Decimal(2.0) * π
d_to_r = lambda d: d * (pi/180.)

print('sine(1):    ', sine(1))
print('sine(0):    ', sine(0))
print('sine(-1):   ', sine(-1))
print('sine(π):    ', sine(π))
print('sine(π/2):  ', sine(π/2))
print('-'*25)
print('math.sin 1   : ', sin(1.0))
print('math.sin 0   : ', sin(0.0))
print('math.sin -1  : ', sin(-1.0))
print('math.sin π   : ', sin(3.141592653589793238462643383))
print('math.sin π/2 : ', sin(3.141592653589793238462643383/2.0))


print('45° : ', sin(d_to_r(45)), sine(45, in_degrees=True))
print('90° : ', sin(d_to_r(90)), sine(90, in_degrees=True))
print('89° : ', sin(d_to_r(89)), sine(89, in_degrees=True))
print('Δ 89: ', sine(89, in_degrees=True) - Decimal(sin(d_to_r(89))))

print('180°: ', sin(d_to_r(45)), sine(45, in_degrees=True))
print('75° : ', sin(d_to_r(75)), sine(75, in_degrees=True))
print('105°: ', sin(d_to_r(105)), sine(105, in_degrees=True))
print('75/105: 0.965925826289068')

x = Decimal('1.0')
print(sine(x), -sine(τ - x))
print(sine(x, precision=25) == -sine(τ - x, precision=25))
print(sine(x, precision=25) == sine(π - x, precision=25))

print('―'*25)

print(sin(1.0) == sin(pi - 1.0))
print(isclose(sin(1.0), sin(pi - 1.0)))


print('―'*25)

print(d_to_r(45))
print('bhaskara: ', bhaskara(d_to_r(45)))
print('sine 2:   ', sine2(d_to_r(45)))
print('sine:     ', sine(d_to_r(45)))
print('sin:      ', sin(d_to_r(45)))

print('―'*25)
x = Decimal('1.0')
print(sine(x), -sine(τ - x))
print(sine(x, precision=25) == -sine(τ - x, precision=25))
print(sine(x, precision=25) == sine(π - x, precision=25))

print(sine(x, precision=25) == -sine(τ - x, precision=25))
print(sine(x, precision=25) == sine(π - x, precision=25))
