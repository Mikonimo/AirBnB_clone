#!/usr/bin/python3
"""Tests"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up for tests."""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all returns the object dictionary."""
        new_dict = self.storage.all()
        self.assertIsInstance(new_dict, dict)

    def test_new_adds_object(self):
        """Test that new adds an object to the storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save properly saves objects to file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("test_file.json"))

    def test_save_and_reload(self):
        """Test save and reload functionality."""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj_id}"
        self.assertIn(key, self.storage.all())

    def test_reload_no_file(self):
        """Test reload from non-existing file."""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_save_with_different_classes(self):
        """Test saving and reloading objects of different classes."""
        objects = [BaseModel(), User(), State(), City(), Amenity(), Place(), Review()]
        for obj in objects:
            self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, self.storage.all())

    def test_serialization(self):
        """Test serialization of an object."""
        obj = User()
        obj.first_name = "John"
        obj.last_name = "Doe"
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"User.{obj.id}"
        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.first_name, "John")
        self.assertEqual(reloaded_obj.last_name, "Doe")

    def test_deserialization(self):
        """Test deserialization of an object."""
        obj = Place()
        obj.name = "My Place"
        obj.city_id = "1234"
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"Place.{obj.id}"
        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.name, "My Place")
        self.assertEqual(reloaded_obj.city_id, "1234")

if __name__ == '__main__':
    unittest.main()
