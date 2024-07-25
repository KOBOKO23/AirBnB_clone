#!/usr/bin/python3
import unittest
import time
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        bm = BaseModel()
        bm.name = "My First Model"
        model_dict = bm.to_dict()
        self.assertEqual(model_dict['name'], "My First Model")

    def test_save_method(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        time.sleep(1)  # Sleep for a second to ensure time difference
        bm.save()
        new_updated_at = bm.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

if __name__ == '__main__':
    unittest.main()
