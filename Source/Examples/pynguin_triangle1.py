


def triangle(x: int, y: int, z: int) -> str:

    is_triangle = lambda x_, y_, z_: (x_ < y_ + z_) and (y_ < x_ + z_) and (z_ < x_ + y_)
    integers    = lambda x_,y_,z_: isinstance(x_, int) and isinstance(y_, int) and isinstance(z_, int)
    is_valid    = lambda x_,y_,z_: (x_ > 0) and (y_ > 0) and (z_ > 0)

    if not (integers(x, y, z) and is_triangle(x, y, z) and is_valid(x, y, z)):
        return "Not a triangle"
    elif x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
