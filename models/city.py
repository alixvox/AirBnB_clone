#!/usr/bin/python3
"""
This module contains class City.
"""
from models.base_model import BaseModel



class City(BaseModel):
    """
    class City inherits from BaseModel and contains
    public attribute strings name and state_id.
    """
    name = ""
    state_id = ""
