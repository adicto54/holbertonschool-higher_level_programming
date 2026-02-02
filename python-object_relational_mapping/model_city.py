#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.
    
    Attributes:
        id (int): Auto-generated, unique integer, primary key.
        name (str): String of 128 characters, not null.
        state_id (int): Integer, foreign key to states.id, not null.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)