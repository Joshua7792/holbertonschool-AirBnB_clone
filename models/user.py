#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""


    def __str__(self):
        """str method\n"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
