#!/bin/bash

# created to run all the examples used in the thesis

echo "STARTING TESTS [saving to test-output]"
echo "starting Assert Example"

cd AssertExample
python3 ../../../Source/falcon.py complex.fcn -t --pytest 2> ../test-output/assert-test-output.test

echo "starting Falcon Motivation Example"
cd ../FalconMotivation
python3 ../../../Source/falcon.py FalconMotivation.fcn -t --pytest 2> ../test-output/falcon-motivaiton-output.test

echo "starting Groupby Example"
cd ../GroupbyExample
python3 ../../../Source/falcon.py commission.fcn -t --pytest 2> ../test-output/groubpy-test-output.test

echo "starting Satisfy Example"
cd ../SatisfyExample
python3 ../../../Source/falcon.py complex.fcn -t --pytest 2> ../test-output/satisfy-test-output.test

echo "starting Test Example"
python3 ../../../Source/falcon.py complex.fcn -t --pytest 2> ../test-output/test-test-output.test

cd ..
echo "\n\nDONE"
