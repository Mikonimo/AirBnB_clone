#!/usr/bin/python3
"""Tests"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City"""

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

if __name__ == '__main__':
    unittest.main()
