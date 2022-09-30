#!/usr/bin/python3
"""python interpreter"""

import json
from os import path

class Base:
    """ class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """inizialize a base classe"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects