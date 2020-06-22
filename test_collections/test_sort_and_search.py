import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list


class TestList(unittest.TestCase):
    def test_search_list_found(self):
        self.assertEqual(sort_and_search_list.search_list([3, 2, 5], 5), 2)

    def test_search_list_not_found(self):
        self.assertEqual(sort_and_search_list.search_list([3, 2, 5], 4), -1)

    def test_sort_list(self):
        self.assertEqual(sort_and_search_list.sort_list([3, 2, 5]), [2, 3, 5])
