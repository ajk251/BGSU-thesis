
import sys
import pprint

from antlr4 import *

from gen.FalconLexer import FalconLexer
from gen.FalconParser import FalconParser

from lang.falcon import Falcon

from utilities.UnitTestWriter import write_basic_unittest

if __name__ == '__main__':

    file = 'Tests/namespace-test.fcn'

    input_stream = FileStream(file, encoding='utf-8')
    lexer = FalconLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    parser = FalconParser(token_stream)

    tree = parser.program()
    falcon = Falcon()
    falcon.visit(tree)

    tests = falcon.intermediate_tests()

    print('-'*45)
    print('tests:')

    pp = pprint.PrettyPrinter(2)
    pp.pprint(tests)

    print('='*45)
    print()

    write_basic_unittest(tests, file)




