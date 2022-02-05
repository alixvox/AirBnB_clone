#!/usr/bin/python3
"""
This module contains the class BaseModel.
"""
import datetime
import uuid

class BaseModel:
    """
    BaseModel contains public instance attributes id,
    created_at and updated_at, as well as methods
    __str__, save(), and to_dict().
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization with kwargs key/value
        attributes, or a new uuid, and created_at and
        updated_at datetimes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__( self):
        """
        String representation of BaseModel
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates self.updated_at with current date/time.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of
        __dict__.
        """
        new_dict = {}
        new_dict["__class__"] = type(self).__name__
        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict["created_at"] = self.created_at.isoformat()
            elif key == "updated_at":
                new_dict["updated_at"] = self.updated_at.isoformat()
            else:
                new_dict[key] = value
        return new_dict
