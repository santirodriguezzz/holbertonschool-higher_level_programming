#!/usr/bin/python3
"""python interpreter"""


def write_file(filename="", text=""):
    """fuction  that writes a string to a text file"""
    with open(filename, 'w')as tempFile:
        return tempFile.write(text)
