from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from iconv_test2 import *

# This file was generated automatically by Falcon.
# from: iconv.fcn
# on 2022 Oct 20 Thu 13:26:29

Cases = generate_cases(n=100)

def test_satisfy_identity_iconv_JSSa():

    for casesᵢ in Cases:

        try:
            result = identity_iconv(casesᵢ)
        except Exception as error:
            result = error

        count = 0

        if does_load(result):
            count += 1
        if valid_points(result):
            count += 1
        if like_iconv(result):
            count += 1
        if most(result):
            count += 1
        if most_128(result):
            count += 1
        if most_256(result):
            count += 1


PyCases = generate_pycases(n=100)

def test_satisfy_iconv_sut_py_nH():

    for pycasesᵢ in PyCases:

        try:
            result = iconv_sut_py(pycasesᵢ)
        except Exception as error:
            result = error

        count = 0

        if loads_in_iconv(result):
            count += 1
        if converts_in_iconv(result):
            count += 1
        if matchs_python_codec(result):
            count += 1
        if matches_iconv(result):
            count += 1

