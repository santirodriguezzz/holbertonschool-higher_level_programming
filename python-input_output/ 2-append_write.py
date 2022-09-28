#!/usr/bin/python3
"""python interpreter"""


def append_write(filename="", text=""):
    """fuction  that writes a string to a text files"""
    with open(filename, 'a') as tempFile:
        return tempFile.write(text)
