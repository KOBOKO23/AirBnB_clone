#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_attributes(self):
        """Test attributes of the BaseModel instance"""
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_to_dict(self):
        """Test conversion to dictionary"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['name', "My First Model"])
        self.assertEqual(model_dict['my_number', 89])
        self.assertEqual(model_dict['__class__'], "BaseModel")
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_recreate_instance_from_dict(self):
        """Test recreation of an instance from a dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
