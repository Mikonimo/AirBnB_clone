#!/usr/bin/python3
"""Tests"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        """Set up for tests."""
        self.user = User()

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test the default attributes of User."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_attributes(self):
        """Test setting attributes of User."""
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
