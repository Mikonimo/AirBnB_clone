#!/usr/bin/python3
"""Tests"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity"""

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))


if __name__ == '__main__':
    unittest.main()
