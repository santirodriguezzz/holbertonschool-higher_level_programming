#!/usr/bin/python3
"""python interpreter"""


def class_to_json(obj):
    """funtion that returns the dictionary description with simple data structure"""
    return obj.__dict__