#!/usr/bin/env python3
"""Parameterize a unit test"""

from typing import Dict
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Test get json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get json"""
        #  configure the mock object to return the test payload
        mock_get.return_value = Mock()   # create mock object
        mock_get.return_value.json.return_value = test_payload
        #  Call the get_json function with the test URL
        result = get_json(test_url)
        #  Assert that the mock object was called
        mock_get.assert_called_once_with(test_url)

        #  Assert that the return value is the test payload
        self.assertEqual(result, test_payload)
