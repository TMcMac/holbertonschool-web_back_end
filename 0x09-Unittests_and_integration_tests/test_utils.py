#!/usr/bin/env python3
""" Tests for utils.py """
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ This class will test the function
        access_nested_map in utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test for correct functioning """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for fail conditions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ This class will test the function
        get_json in utils.py
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """ Use mock to test an http call and json return """
        with patch('requests.get') as mock_request:
            mock_request().json.return_value = test_payload
            mock_resquest.assert_called_once()
            result = get_json(url)
            mock_request.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()
