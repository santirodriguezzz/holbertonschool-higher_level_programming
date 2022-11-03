#!/usr/bin/python3
"""python interpreter"""


def inherits_from(obj, a_class):
    """function"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
