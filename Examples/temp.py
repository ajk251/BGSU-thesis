

# def not_positive_integers(a: int, b: int, c: int) -> bool:
#     """Tests that all values are positive integers"""
#     # return any(map(lambda n: (not isinstance(n, int)) or (not n >= 1), (a, b, c)))
#     if (not isinstance(a, int)) or (not a >= 1):
#         return False
#     elif (not isinstance(b, int)) or (not b >= 1):
#         return False
#     elif (not isinstance(c, int)) or (not c >= 1):
#         return False

#     return True

def not_positive_integers(a: int, b: int, c: int) -> bool:
    return any(map(lambda n: (not isinstance(n, int)) or (not n > 0), (a, b, c)))

# def not_positive_integers(a: int, b: int, c: int) -> bool:
#     """Tests that all values are positive integers"""
#     # return any(map(lambda n: (not isinstance(n, int)) or (not n >= 1), (a, b, c)))
#     if (not isinstance(a, int)) or (not a > 0) or \
#        (not isinstance(b, int)) or (not b > 0) or \
#        (not isinstance(c, int)) or (not c > 0):
#         return False

#     return True


print(not_positive_integers(1, 1, 1))

print(not_positive_integers(-1, -1, -1))
print(not_positive_integers(-1, 1, 1))
print(not_positive_integers(1, -1, 1))
print(not_positive_integers(1, 1, -1))
print(not_positive_integers(0, 1, 1))
print(not_positive_integers(0, 1, 0))
print(not_positive_integers(1, 0, 1))
print(not_positive_integers(0, 1.1, 0))
print(not_positive_integers(1, 0, 1.1))