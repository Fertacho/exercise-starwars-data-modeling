import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250),nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    description = Column(String(250),nullable=False)
    
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    description = Column(String(250),nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character_name = Column(String(250), ForeignKey('characters.name'))
    planet_name = Column(String(250), ForeignKey('planets.name'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(Users)
    character = relationship(Characters)
    planets = relationship(Planets)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')