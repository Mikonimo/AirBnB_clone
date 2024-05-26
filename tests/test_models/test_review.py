#!/usr/bin/python3
"""Tests"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

if __name__ == '__main__':
    unittest.main()
