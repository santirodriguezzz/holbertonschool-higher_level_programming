#!/usr/bin/python3
"""python interpreter"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
    print(f"{read_data}", end='')
