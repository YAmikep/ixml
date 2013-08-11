# Testing toolbox
import unittest
from nose_parameterized import parameterized

from StringIO import StringIO

# Sets of data test
from .. import _test_datasets as tds


class APIBackendTests(unittest.TestCase):

    """
    Tests all the backends.

    """
    @parameterized.expand(tds.load_all_backends_tests)
    def test_parse(self, name, backend, i):
        testset = tds.XML_TEST_DATA_SETS[i]

        data = StringIO(testset[1])
        expected = testset[2]

        # Diff is 969 characters long. Set self.maxDiff to None to see it.
        self.maxDiff = None

        results = tuple(backend.parse(data))
        self.assertEquals(results, expected)

    @parameterized.expand(tds.load_all_backends_tests)
    def test_items(self, name, backend, i):
        testset = tds.XML_TEST_DATA_SETS[i]

        data = StringIO(testset[1])
        path = testset[3]
        expected = testset[4]

        # Diff is 969 characters long. Set self.maxDiff to None to see it.
        self.maxDiff = None

        results = tuple(backend.items(data, path))
        self.assertEquals(results, expected)
