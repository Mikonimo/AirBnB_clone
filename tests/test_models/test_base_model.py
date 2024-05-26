#!/usr/bin/python3
""""Test for the base_model class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """The BaseModel testcases"""

    def test_id_is_string(self):
        c1 = BaseModel()
        self.assertIsInstance(c1.id, str)

    def test_id_is_unique(self):
        c1 = BaseModel()
        c2 = BaseModel()
        self.assertNotEqual(c1.id, c2.id)

    def test_created_at(self):
        c1 = BaseModel()
        self.assertIsInstance(c1.created_at, datetime)

    def test_updated_at(self):
        c1 = BaseModel()
        self.assertIsInstance(c1.updated_at, datetime)
        self.assertEqual(c1.created_at, c1.updated_at)

    def test_str_method(self):
        c1 = BaseModel()
        expected_str = f"[BaseModel] ({c1.id}) {c1.__dict__}"
        self.assertEqual(str(c1), expected_str)

    def test_save_method(self):
        c1 = BaseModel()
        prev_updated_at = c1.updated_at
        c2 = BaseModel()
        c2.save
        self.assertNotEqual(c2.updated_at, prev_updated_at)
        self.assertGreater(c2.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        c1 = BaseModel()
        c1_dict = c1.to_dict()
        self.assertEqual(c1_dict['__class__'], 'BaseModel')
        self.assertEqual(c1_dict['id'], c1.id)
        self.assertIsInstance(c1_dict['created_at'], str)
        self.assertIsInstance(c1_dict['updated_at'], str)
        self.assertEqual(c1_dict['created_at'], c1.created_at.isoformat())
        self.assertEqual(c1_dict['updated_at'], c1.updated_at.isoformat())

    def test_to_dict_contains_correct_keys(self):
        c1 = BaseModel()
        c1.name = "Test Model"
        c1.number = 123
        c1_dict = c1.to_dict()
        self.assertIn('id', c1_dict)
        self.assertIn('created_at', c1_dict)
        self.assertIn('updated_at', c1_dict)
        self.assertIn('__class__', c1_dict)
        self.assertIn('name', c1_dict)
        self.assertIn('number', c1_dict)

    def test_to_dict_creates_copy(self):
        c1 = BaseModel()
        c1_dict_1 = c1.to_dict()
        c1.save()
        c1_dict_2 = c1.to_dict()
        self.assertNotEqual(c1_dict_1['updated_at'], c1_dict_2['updated_at'])

    def test_instance_creation_from_dict(self):
        c1 = BaseModel()
        c1.name = "My_First_Model"
        c1.number = 89
        c1_dict = c1.to_dict()
        c2 = BaseModel(**c1_dict)
        self.assertEqual(c1.id, c2.id)
        self.assertEqual(c1.created_at, c2.created_at)
        self.assertEqual(c1.updated_at, c2.updated_at)
        self.assertEqual(c1.name, c2.name)
        self.assertEqual(c2.number, c1.number)
        self.assertIsInstance(c2.updated_at, datetime)
        self.assertIsInstance(c2.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
