#!/usr/bin/python3
"""python interpreter"""


def class_to_json(obj):
    """funtion that returns the dictionary description"""
    return obj.__dict__
