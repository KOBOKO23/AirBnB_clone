#!/usr/bin/python3

"""Module base_model

This Module contains a definition for BaseModel Class
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class BaseModel"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, time_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        from models import storage
        storage.new(self)
        
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = self.created_at.isoformat()
        to_json['updated_at'] = self.updated_at.isoformat()
        return to_json

    def __str__(self):
        """Print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
