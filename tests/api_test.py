# Testing toolbox
import unittest
from nose_parameterized import parameterized

from StringIO import StringIO

# Sets of data test
import _test_datasets as tds

import ixml


class APITests(unittest.TestCase):

    """
    Tests the API from ixml which must not failed no matter what backend 
    dependencies are installed (fallback to standard library).

    """
    backend = ixml

    @parameterized.expand(tds.load_backend_tests(backend))
    def test_parse(self, name, backend, i):
        testset = tds.XML_TEST_DATA_SETS[i]

        data = StringIO(testset[1])
        expected = testset[2]

        # Diff is 969 characters long. Set self.maxDiff to None to see it.
        self.maxDiff = None

        results = tuple(backend.parse(data))
        self.assertEquals(results, expected)

    @parameterized.expand(tds.load_backend_tests(backend))
    def test_items(self, name, backend, i):
        testset = tds.XML_TEST_DATA_SETS[i]

        data = StringIO(testset[1])
        path = testset[3]
        expected = testset[4]

        # Diff is 969 characters long. Set self.maxDiff to None to see it.
        self.maxDiff = None

        results = tuple(backend.items(data, path))
        self.assertEquals(results, expected)
