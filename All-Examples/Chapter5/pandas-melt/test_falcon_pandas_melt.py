from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from falcon_melt import *

# This file was generated automatically by Falcon.
# from: pandas_melt.fcn
# on 2022 Oct 19 Wed 19:38:38

dfs = df_generator()

def test_satisfy_melt_sut_UoR():

    for dfsᵢ in dfs:

        try:
            result = melt_sut(dfsᵢ)
        except Exception as error:
            result = error

        count = 0

        if valid_dataframe(result):
            count += 1
        if sums_correctly(result):
            count += 1
        if is_melted_no_args(result):
            count += 1
        if is_melted_id_args(result):
            count += 1
        if is_melted_value_vars(result):
            count += 1
        if is_melted_id_value(result):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"
