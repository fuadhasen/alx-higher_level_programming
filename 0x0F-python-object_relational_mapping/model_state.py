#!/usr/bin/python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:@localhost:3306/')

Base = declarative_base()


class State(Base):
    """ state tabel schema """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
