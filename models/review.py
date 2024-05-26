#!/usr/bin/python3
"""Contains the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Class"""
    place_id = ""
    user_id = ""
    text = ""
