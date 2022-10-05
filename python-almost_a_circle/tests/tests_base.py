#!/usr/bin/python3
"""python interpreter"""
import unittest
from models.base import Base



class basetests1(unittest.TestCase):
    """tests attribute id"""

    def setUp(self):
        self.k = Base()

    def test_id(self):
        self.assertEquals(k, id, 0)
