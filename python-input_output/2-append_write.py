#!/usr/bin/python3
"""python interpreter module"""


def append_write(filename="", text=""):
    """fuction  that writes a string to a text file"""
    with open(filename, 'a') as tempFile:
        return tempFile.write(text)
