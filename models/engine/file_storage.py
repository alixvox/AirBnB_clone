#!/usr/bin/python3
"""
This module contains class FileStorage.
"""
import json
import os


class FileStorage:
    """
    FileStorage is a class that serializes an instance to a JSON file,
    and converts JSON files to instances.
    They contain attributes __file_path which is the path to the
    JSON file, and __objects, which is a dictionary of objects that are saved.
    They include methods all(), new(), save(), and reload().
    """

    def __init__(self):
        """
        Initialization with a placeholder file path
        and an empty dictionary of objects.
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds obj to the __objects dictionary.
        """
        self.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """
        Serializes an object to a JSON file.
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        json_string = json.dumps(obj_dict)
        with open(self.__file_path, 'w+') as f:
            data = f.read()
            f.seek(0)
            f.write(json_string)
            f.truncate()

    def reload(self):
        """
        Deserializes an object from a JSON file and
        saves it to the __objects dictionary.
        """
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                self.__objects[key] = BaseModel(**value)

