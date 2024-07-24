import unittest
from datetime import datetime
from time import sleep
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.model

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.model.updated_at
        sleep(0.1)  # Sleep for a short period to ensure datetime difference
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_str(self):
        """Test __str__ method"""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


if __name__ == "__main__":
    unittest.main()
