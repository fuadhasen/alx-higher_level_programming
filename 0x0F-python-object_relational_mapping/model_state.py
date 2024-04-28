#!/usr/bin/node
"""This module define First state model"""
import sqlalchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class defined."""
    __tablename__ = 'state'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
