import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array


class TestList(unittest.TestCase):
    def test_search_array_found(self):
        self.assertEqual(sort_and_search_array.search_array([3, 2, 5], 5), 2)

    def test_search_array_not_found(self):
        self.assertEqual(sort_and_search_array.search_array([3, 2, 5], 4), -1)

    def test_sort_array(self):
        self.assertEqual(sort_and_search_array.sort_array([3, 2, 5]), [2, 3, 5])
