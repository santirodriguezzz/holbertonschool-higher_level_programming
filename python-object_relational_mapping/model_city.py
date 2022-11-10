#!/usr/bin/python3
"""model city"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base): 
    """class: City"""


    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', String(
        128), ForeignKey('states.id'), nullable=False)
