#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class handles all application cities"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    def to_json(self):
        """Converts the City instance to a dictionary"""
        json_dict = self.to_dict()
        json_dict['__class__'] = 'City'
        return json_dict

    def __str__(self):
        """String representation of the City class"""
        attributes = self.__dict__.copy()
        attributes.pop('_sa_instance_state', None)  # Remove SQLAlchemy state
        attributes.pop('password', None)  # Remove password if it exists
        attributes['created_at'] = attributes['created_at'].strftime('%Y-%m-%dT%H:%M:%S.%f')

        # Remove 'updated_at' if it exists and is not None
        attributes.pop('updated_at', None)

        attributes['__class__'] = self.__class__.__name__
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, attributes)
