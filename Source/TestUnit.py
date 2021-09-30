

from abc import ABC
from collections import namedtuple


Predicate = namedtuple('Predicate', 'predicate, assert_value, test_value')




class TestUnit(ABC):

    pass

# ---------------------------------------------------------

# Looks like:
# Test function:
#   | <values> 

class AssertionTest(TestUnit):

    def __init__(self):
        pass

# ---------------------------------------------------------

# Looks like:

#     winnow <function> <domain>:
#         | <group> <predicate>
#         | …

class WinnowTest(TestUnit):

    def __init__(self):
        pass