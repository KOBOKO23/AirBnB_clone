#!/usr/bin/python3

import json
import os

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Sets __objects with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    from models.base_model import BaseModel
                    for key, value in obj_dict.items():
                        cls_name = key.split('.')[0]
                        cls = globals().get(cls_name)
                        if cls:
                            self.new(cls(**value))
                except Exception as e:
                    print(f"Failed to load from {FileStorage.__file_path}: {e}")

# Initialize the storage
storage = FileStorage()
storage.reload()
