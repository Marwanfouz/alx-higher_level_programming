#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    