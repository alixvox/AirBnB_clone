#!/usr/bin/python3
"""
This module contains class Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review inherits from BaseModel and contains
    public attribute strings place_id, user_id and text.
    """
    place_id = ""
    user_id = ""
    text = ""
