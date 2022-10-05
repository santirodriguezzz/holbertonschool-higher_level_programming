#!/usr/bin/python3
"""python interpreter"""

import json
from os import path


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        If the id is not None,
        then the id is set to the id passed in. If the id is None,
        then the id is set
        to the number of objects created.
        :param id: the id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        It converts a list of dictionaries to a JSON string.
        :param list_dictionaries: a list of dictionaries
        :return: A JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        "Save a list of objects to a file in JSON format."
        The first line of the function is a docstring.
        It's a good idea to include a docstring in every
        function you write
        :param cls: the class that we're calling the method on
        :param list_objs: a list of instances who inherits of Base
        """

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
        """
        If the string is empty or None, return an empty list,
        otherwise return the list of dictionaries.
        :param json_string: the string to be converted
        :return: A list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        list_Dics = json.loads(json_string)
        return list_Dics

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy object of the class,
        update it with the dictionary, and return it.
        :param cls: the class that is calling the method
        :return: A new instance of the class with the attributes updated
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 3)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        It creates a list of instances from a json file.  
        :param cls: the class
        :return: A list of instances
        """
        my_List = []

        fileName = cls.__name__ + ".json"
        if path.exists(fileName):
            with open(fileName, encoding='utf-8') as f:
                list_Dict = cls.from_json_string(f.read())
            for list_Dict in list_Dict:
                my_List.append(cls.create(**dict()))
        return my_List
