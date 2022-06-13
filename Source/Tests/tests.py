from algorithms.algorithms import *
from domains import *
from macros import *
from predicates import *
from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError

from collections import defaultdict
import unittest

import pytest
from Examples.max_agreement import *
from Examples.agreement_test import *

# This file was generated automatically by falcon.
# from: Tests/agreement.fcn
# on 2022 Jun 13 Mon 17:03:14

examples = agreement_critical()

# start test -----------------
def test___cji6():

    for l1ᵢ,l2ᵢ,depthᵢ in examples:
        with pytest.raises(Exception):
            assert agree2(l1ᵢ, l2ᵢ, depthᵢ)

values = agreement_example()

# start test -----------------
def test___Gt():

    for l1ᵢ,l2ᵢ,depthᵢ in values:
        assert agree(l1ᵢ, l2ᵢ, depthᵢ)
