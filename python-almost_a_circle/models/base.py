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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation"""
        fileName = cls.__name__ + ".json"
        list_Dict = []

        if list_objs is not None:
            for i in list_objs:
                list_Dict.append(i.to_dictionary())

        j_string = cls.to_json_string(list_Dict)

        with open(fileName, mode='w') as f:
            f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON in string"""
        if json_string is None:
            return "[]"
        if len(json_string) == 0:
            return "[]"
        list_Dics = json.loads(json_string)
        return list_Dics
