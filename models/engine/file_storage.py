#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel  # Ensure BaseModel is imported

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                from models.base_model import BaseModel  # Ensure BaseModel is available
                # Add all necessary classes here
                class_map = {
                    'BaseModel': BaseModel,
                    # Add other model classes here as needed
                }
                self.__objects = {k: class_map[v['__class__']](**v) for k, v in objects.items()}
        except FileNotFoundError:
            self.__objects = {}
        except json.JSONDecodeError:
            self.__objects = {}
