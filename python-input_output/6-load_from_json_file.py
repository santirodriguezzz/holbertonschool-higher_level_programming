#!/usr/bin/python3
"""python interpreter"""
import json


def load_from_json_file(filename):
    """funtion"""
    with open(filename, 'r') as tempFile:
        return json.load(tempFile)
