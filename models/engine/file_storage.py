#!/usr/bin/python3
"""
This module contains class FileStorage Serializes instances to a 
    JSON file and deserializes JSON file to instances
"""
import json

class FileStorage:
    """
    FileStorade Model contains private class attr __file_path
    and __objects. as well as public instance methods all(),
    new(), save(), and reload (). 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        key = "{}: {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        
        """

    

