#!/usr/bin/python3

""" It Defines the Review class """

from models.base_model import BaseModel

class Review(BaseModel):

    """ It intializes the class attributes """
    place_id = ""
    user_id = ""
    text = ""
