#!/usr/bin/python3
"""
This module contains class User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User inherits from BaesModel and contains attributes:
    Public strings email, password, first_name, and last_name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
