
import argparse
import sys
import pprint

from antlr4 import *
import pytest

from Falcon.gen.FalconLexer import FalconLexer
from Falcon.gen.FalconParser import FalconParser
from Falcon.lang.falcon import Falcon
from Falcon.writers.UnitTestWriter import write_basic_unittest
from Falcon.writers.TestWriter import write_basic_test

# argument parser ----------------

parser = argparse.ArgumentParser(description="Generate Falcon test files")

# the input file mandatory
parser.add_argument('file', nargs=1, default=None, help='The name of Falcon file')

# the output file
parser.add_argument('output', nargs='*', default=None, action='append', help='The name of file for the generated code')

# the output type
parser.add_argument('--test', '-t', default=True, action='store_true',
                    required=False, help='Generate a PyTest file')
parser.add_argument('--unit', '-u', default=False, action='store_true',
                    required=False, help='Generate a unit test file')
parser.add_argument('--both', '-b', default=False, action='store_true',
                    required=False, help='Generate PyTest file & unit test file')

# show the tree
parser.add_argument('--debug', '-d', default=False, action='store_true',
                    required=False, help='Show the generated tree for Falcon')

# only keyword ---------
# invoke PyTest
parser.add_argument('--pytest', default=False, action='store_true',
                    required=False, help='Invoke PyTest and run on the output file')

args = parser.parse_args()


if __name__ == '__main__':

    print('The args: ', args)

    file = None if args.file[0] in ('-', '_') else args.file[0]

    if file is None:

        # file = 'Tests/namespace-test.fcn'
        # file = 'Tests/some-tests.fcn'
        # file = 'Tests/logical-tests.fcn'
        # file = 'Tests/initial-tests.fcn'
        # file = 'Tests/winnow_test.fcn'
        # file = 'Tests/unit-tests.fcn'
        # file = 'Tests/unit-test2.fcn'
        # file = 'Tests/pytest-tests.fcn'
        # file = 'Tests/winnow_test2.fcn'
        file = 'Tests/winnow_tests3.fcn'
        # file = 'Tests/satisfy-tests.fcn'
        # file = 'Tests/complex.fcn'
        # file = 'Tests/groupby-tests.fcn'
        # file = 'Tests/triangle-problem.fcn'
        # file = 'Tests/assert2.fcn'
        # file = 'Tests/complex-satisfy.fcn'
        # file = 'Tests/agreement.fcn'

        print(f'Using debugging file: {file}')

    input_stream = FileStream(file, encoding='utf-8')
    lexer = FalconLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    parser = FalconParser(token_stream)

    tree = parser.block()
    falcon = Falcon()
    falcon.visit(tree)

    # gets the dict/json-like tree from antlr
    falcon_tree = falcon.intermediate_tests()

    # the destination file is optional
    dest_file = None if args.output is None else args.output[0]

    if args.both:
        # can't generate two files with the same name
        ttest = args.output[0][0] if len(args.output[0]) == 2 else None
        utest = args.output[0][1] if len(args.output[0]) == 2 else None
        write_basic_test(falcon_tree, file, ttest)
        write_basic_unittest(falcon_tree, file, utest)

        print(f'Test file: "{ttest if ttest is not None else "default"}"  Unit Test file: "{utest if utest is not None else "default"}"')
    elif args.test:
        write_basic_test(falcon_tree, file, dest_file)
    elif args.unit:
        write_basic_unittest(falcon_tree, file, dest_file)

    # -------------------------------------------

    # show the tree - for debugging
    if args.debug:

        print('-'*45)
        print('tests:')

        pp = pprint.PrettyPrinter(2)
        pp.pprint(falcon_tree)

        print('='*45)
        print()


    # invoke PyTest
    #   https://docs.pytest.org/en/latest/how-to/usage.html

    if args.pytest:
        print('***RUNNING PyTest***')

        if dest_file is None:
            dest_file = 'Tests/tests.py'

        test = pytest.main([dest_file])
