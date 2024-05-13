#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 1}}, ('a', 'b'), 1),
        ({'a': {'b': {'c': 1}}}, ('a', 'b', 'c'), 1),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access nested map exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
