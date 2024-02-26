#!/usr/bin/python3
"""holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def to_json(self):
        """Converts the User instance to a dictionary"""
        json_dict = self.to_dict()
        json_dict['__class__'] = 'User'
        return json_dict

    def __str__(self):
        """String representation of the User class"""
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)  # Remove SQLAlchemy state
        attributes.pop('password', None)  # Remove password if it exists
        attributes['created_at'] = attributes['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        # Remove 'updated_at' if it exists and is not None
        attributes.pop('updated_at', None)
    
        attributes['__class__'] = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, attributes)


 
 
