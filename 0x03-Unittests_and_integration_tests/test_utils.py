#!/usr/bin/env python3
"""Parameterize a unit test"""

from typing import Dict
import unittest
from unittest.mock import Mock
from parameterized import parameterized
from requests import patch
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
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
