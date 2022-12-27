#!/usr/bin/python3
"""
contains State
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# creates Base
Base = declarative_base()


class State(Base):
    """
    defines State
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
