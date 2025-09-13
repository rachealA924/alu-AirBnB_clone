#!/usr/bin/python3
"""FileStorage module for AirBnB clone project"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects, if file exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                cls_name = val["__class__"]
                # Import dynamically (simplified for BaseModel only for now)
                if cls_name == "BaseModel":
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
