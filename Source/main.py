
import sys
import pprint

from antlr4 import *

from gen.FalconLexer import FalconLexer
from gen.FalconParser import FalconParser

from lang.falcon import Falcon

from utilities.UnitTestWriter import write_basic_unittest


# NOTE:
#   How to invoke pytest
#       https://docs.pytest.org/en/latest/how-to/usage.html

def main(argv):

    if len(argv) > 1:
        print(argv)

    return None


if __name__ == '__main__':

    file = main(sys.argv)

    if file is None:
        # file = 'Tests/namespace-test.fcn'
        # file = 'Tests/some-tests.fcn'
        # file = 'Tests/logical-tests.fcn'
        # file = 'Tests/initial-tests.fcn'
        # file = 'Tests/winnow_test.fcn'
        # file = 'Tests/unit-tests.fcn'
        file = 'Tests/pytest-tests.fcn'
        # file = 'Tests/winnow_test2.fcn'

    input_stream = FileStream(file, encoding='utf-8')
    lexer = FalconLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    parser = FalconParser(token_stream)

    tree = parser.program()
    falcon = Falcon()
    falcon.visit(tree)

    tests = falcon.intermediate_tests()
    write_basic_unittest(tests, file)

    print('-'*45)
    print('tests:')

    pp = pprint.PrettyPrinter(2)
    pp.pprint(tests)

    print('='*45)
    print()
