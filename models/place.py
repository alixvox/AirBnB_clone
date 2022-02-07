#!/usr/bin/python3
"""
This module contains class Place.
"""
from models.base_model import BaseModel



class Place(BaseModel):
    """
    class Place inherits from BaseModel and contains
    public attributes:
    strings name, city_id, user_id, and description,
    ints number_rooms, number_bathrooms,  max_guest, and price_by_night,
    floats latitude and longitude, and list amenity_ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
