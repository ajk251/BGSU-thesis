#!/usr/bin/env python
# it's: chmod +x falcon.py

import argparse
import pathlib
import pprint
import os

from antlr4 import *
import pytest

from Falcon.gen.FalconLexer import FalconLexer
from Falcon.gen.FalconParser import FalconParser
# from Falcon.gen.FalconLexer import FalconLexer
# from Falcon.gen.FalconParser import FalconParser
# from Falcon.lang.falcon import Falcon
from Falcon.lang.falcon import Falcon
from Falcon.writers.UnitTestWriter import write_basic_unittest, SUT
from Falcon.writers.TestWriter import write_basic_test, SUT
from Falcon.writers.tools import add_pytest_config_file

# argument parser ----------------

parser = argparse.ArgumentParser(description="Generate Falcon test files")

# the input file mandatory
parser.add_argument('file', nargs=1, default=None, action='store', help='The name of Falcon file')

# the output file
parser.add_argument('output', nargs='*', default=None, action='store', help='The name of file for the generated code')

# the output type
parser.add_argument('--test', '-t', default=False, action='store_true',
                    required=False, help='Generate a PyTest file')
parser.add_argument('--unit', '-u', default=False, action='store_true',
                    required=False, help='Generate a unit test file')

# show the tree
parser.add_argument('--debug', '-d', default=False, action='store_true',
                    required=False, help='Show the generated tree for Falcon')

# only keyword ---------
# invoke PyTest
parser.add_argument('--pytest', default=False, action='store_true',
                    required=False, help='Invoke PyTest and run on the output file')

parser.add_argument('--coverage', default=False, action='store_true',
                    required=False, help='When using PyTest, measure coverage')

parser.add_argument('--cov', default=None, #action='store_true',
                    required=False, help='When using PyTest, measure coverage')

if __name__ == '__main__':

    # TODO: do better file handling, at least using test file...

    args = parser.parse_args()

    # the input file
    if args.file[0] in ('.', '-', '_'):         # use the default/debug file
        file = None
    elif args.file[0] is None:
        file = None
    else:
        file = args.file[0]

    # file = None if args.file[0] in ('.', '-', '_') else os.getcwd() + '/' + args.file[0]
    # output = None if args.output[0] is None else args.output[0]

    # these are defaults / for testing
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
        # file = 'Tests/winnow_tests3.fcn'
        # file = 'Tests/satisfy-tests.fcn'
        file = 'Tests/complex.fcn'
        # file = 'Tests/groupby-tests.fcn'
        # file = 'Tests/triangle-problem.fcn'
        # file = 'Tests/assert2.fcn'
        # file = 'Tests/complex-satisfy.fcn'
        # file = 'Tests/agreement.fcn'
        # file = 'Tests/commission.fcn'

        # thesis examples
        # file = 'ThesisExamples/FalconMotivation.fcn'

        # print(f"Using debugging file: '{file}'")

    if not os.path.exists(file):
        raise FileExistsError(f"File '{file}' was not found")

    # the output file
    if args.output == [] or args.output is None:
        path = os.path.basename(file)
        name, ext = os.path.splitext(path)                      # uses the falcon file name
        # output = os.getcwd() + f'/test_falcon_{name}.py'
        output = (os.getcwd(), f'/test_falcon_{name}')
    else:
        # output = os.getcwd() + '/' + args.output[0]
        output = (os.getcwd(), '/' + args.output[0])
    # add pytest.toml
    # if not os.path.exists(os.getcwd() + '/' + 'pyproject.toml'):
    #     add_pytest_config_file(os.getcwd() + '/' + 'pyproject.toml')
    #     print('added pyproject.toml')

    print('Using file:      ', file)

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

    # files_written = []                              # for pytest

    # one or both
    if args.test is False and args.unit is False:
        # have to do one...
        out = ''.join(output) + '.py'
        write_basic_test(falcon_tree, file, out)
        print('Generating test file: ', out)
    elif args.test:
        out = ''.join(output) + '.py'
        write_basic_test(falcon_tree, file, out)
        print('Generating test file: ', out)
    elif args.unit:
        out = ''.join(output) + '_unit.py'
        write_basic_unittest(falcon_tree, file, out)
        print('Generating unit test file: ', out)

    print('*****   Done   *****')

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
    #   https://pytest-cov.readthedocs.io/en/latest/config.html
    #   https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-pythonpath
    #   https://stackoverflow.com/questions/46652192/py-test-gives-coverage-py-warning-module-sample-py-was-never-imported
    #   https://pytest-cov.readthedocs.io/en/latest/readme.html#documentation

    if args.pytest:

        print('***** RUNNING PyTest *****')

        if args.coverage:
            name = '.' if SUT is None else ', '.join(SUT)

            if name.endswith('.py'):
                name = name.strip('.py')
                print('*** Removing .py from name')

            test = pytest.main([out, '--maxfail=10', f'--cov={name}', '--cov-report=html'])
        elif args.cov:
            if name.endswith('.py'):
                name = name.strip('.py')
                print('*** Removing .py from name')
            test = pytest.main([out, '--maxfail=10', f'--cov={args.cov}', '--cov-report=html'])
        else:
            test = pytest.main([out, '--maxfail=10'])

    print('***** Finished *****')
