import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    planet_from = Column(String(250), ForeignKey('planet.name'))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    size = Column(Integer)
    climate = Column(String(250))

class Vehicle(Base):
    __tablename__ ='vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vehicle_type = Column(String(250))
    pilot = Column(String(250), ForeignKey('character.name'))

class Favorites(Base):
    _tablename_ = 'favorites'
    date_added = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.user_id') , primary_key=True)
    favorite_characters = Column(String(250), ForeignKey('characters.name'))
    favorite_planets = Column(String(250), ForeignKey('planets.name'))
    favorite_vehicle = Column(String(250), ForeignKey('vehicles.name'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
