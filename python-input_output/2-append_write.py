#!/usr/bin/python3
"""python3 interpreter"""


 def append_write(filename="", text=""):
    """fuction  that writes a string to a text file"""
    with open(filename, 'w')as tempFile:
        return tempFile.write(text)
