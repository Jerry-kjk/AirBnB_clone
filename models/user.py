#!/usr/bin/python3
"""
User inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
