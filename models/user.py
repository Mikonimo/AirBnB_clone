#!/usr/bin/python3
"""Contains the User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """The User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
