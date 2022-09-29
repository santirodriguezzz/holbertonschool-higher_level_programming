#!/usr/bin/python3
"""python interpreter"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """initialize new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary"""
        self_dictionary = self.__dict__
        ndict = {}

        if attrs is None:
            return self_dictionary

        if type(attrs) is list:
            for elems in attrs:
                if hasattr(self, elems):
                    ndict[elems] = getattr(self, elems)
            return ndict

    def reload_from_json(self, json):
        self.__dict__.update(json)
