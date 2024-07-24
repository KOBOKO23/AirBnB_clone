#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = to_json['created_at'].isoformat()
        to_json['updated_at'] = to_json['updated_at'].isoformat()
        return to_json

    def __str__(self):
        """Print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    # Recreate an instance using the dictionary
    new_model = BaseModel(**my_model_json)
    print(new_model)
    print(type(new_model.created_at))
    print(type(new_model.updated_at))
    print(new_model == my_model)  # This should print False because they are different instances
