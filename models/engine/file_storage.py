#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel


class Filestorage:
    """
    __file_path = "file.json"
    __objects = {}
    """

    def new(self, obj):
        """
        set __objects obj with keys
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        Filestorage.__objects[key] = obj

    def all(self):
        """
        return the dictionary __objects.

        """
        return Filestorage.__objects

    def save(self):
        """
        serilize __objects to json file.
        """
        all_objs = Filestorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(Filestorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the json file
        """
        if os.path.isfile(Filestorage.__file_path):

            with open(Filestorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)

                        instance  = cls(**values)

                        Filestorage.__objects[key] = instance

                except Exception:
                    pass
