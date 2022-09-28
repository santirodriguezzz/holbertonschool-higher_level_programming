#!/usr/bin/python3
"""python interpreter"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename,'w') as tempFile:
        tempFile.write(json.dumps(my_obj))
