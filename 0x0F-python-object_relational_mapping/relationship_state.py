#!/usr/bin/python3
"""
contains State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# creates Base
Base = declarative_base()


class State(Base):
    """
    defines State
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
