#!/usr/bin/python3
"""python file that contains the class definition of a State"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """class: State"""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)