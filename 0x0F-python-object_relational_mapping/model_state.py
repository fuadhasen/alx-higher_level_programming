#!/usr/bin/python3
import SQLAlchemy
from SQLAlchemy import Column, String, Integer
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ state tabel schema """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
