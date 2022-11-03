#!/usr/bin/python3
"""pyhon interpreter"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """initialize new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary"""
        return self.__dict__
