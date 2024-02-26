#!/usr/bin/python
"""holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review"""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

    def to_json(self):
        """Converts the Review instance to a dictionary"""
        json_dict = self.to_dict()
        json_dict['__class__'] = 'Review'
        return json_dict

    def __str__(self):
        """String representation of the Review class"""
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)  # Remove SQLAlchemy state
        attributes.pop('password', None)  # Remove password if it exists
        attributes['created_at'] = attributes['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        # Remove 'updated_at' if it exists and is not None
        attributes.pop('updated_at', None)

        attributes['__class__'] = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, attributes) 
