#!/usr/bin/python3
"""This module contains the  FileStorage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """It serializes instances to JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(pathL __file_path)"""
        dict_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(dict_obj, f)

    def reload(self):
        """deserializes the JSON file to _objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)
                for key, value in dict_obj.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
