#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)

    def to_json(self):
        """Converts the Amenity instance to a dictionary"""
        json_dict = self.to_dict()
        json_dict['__class__'] = 'Amenity'
        return json_dict

    def __str__(self):
        """String representation of the Amenity class"""
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)  # Remove SQLAlchemy state
        attributes.pop('password', None)  # Remove password if it exists
        attributes['created_at'] = attributes['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        # Remove 'updated_at' if it exists and is not None
        attributes.pop('updated_at', None)

        attributes['__class__'] = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, attributes)

