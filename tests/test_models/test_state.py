#!/usr/bin/python3
"""Tests"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State Class"""

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

if __name__ == '__main__':
    unittest.main()
