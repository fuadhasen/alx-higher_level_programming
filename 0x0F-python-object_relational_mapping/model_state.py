#!/usr/bin/python3
""" python script for modeling state """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """ state tabele schema """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
