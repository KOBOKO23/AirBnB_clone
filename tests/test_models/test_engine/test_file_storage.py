#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class TestFileStorageInstantiation(unittest.TestCase):
    """
    Testing the instantiation of FileStorage.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertIsInstance(models.storage, FileStorage)


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage = FileStorage()
        models.storage._FileStorage__file_path = self.test_file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        self.assertIsInstance(models.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", models.storage.all())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_no_args(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.test_file
        new_storage.reload()

        self.assertIn(f"BaseModel.{obj1.id}", new_storage.all())
        self.assertIn(f"BaseModel.{obj2.id}", new_storage.all())

    def test_save_to_file(self):
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        with open(self.test_file, 'w') as f:
            f.write("{}")
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})

    def test_reload_missing_file(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
