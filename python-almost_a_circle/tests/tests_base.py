#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base import Base



class basetests1(unittest.TestCase):
    """tests attribute id"""

    def setUp(self):
        self.k = Base()

    def test_0(self):
        self.assertEquals(self.k.id, 1)

    def test_1(self):
        self.assertEquals(self.k.id, 2)

    def test_2(self):
        self.assertEquals(self.k.id, 3)

class basetest2(unittest.TestCase):
    """test for id"""

    def test_1(self):
        self.b = Base(89)
        self.assertEquals(self.b.id, 89)