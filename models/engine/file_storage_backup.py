#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import os
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects 

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def get(self, cls, id):
        """
        Gets a specific object by class and id
        :param cls: class
        :param id: id of instance
        :return: object or None
        """
        all_class = self.all(cls)
        return next((obj for obj in all_class.values()
                    if id == str(obj.id)), None)

    def count(self, cls=None):
        """
        Count of instances
        :param cls: class
        :return: number of instances
        """
        return len(self.all(cls))

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
    
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialized_objects, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key, data in jo.items():
                class_name = data.get("__class__", "BaseModel")
                cls = classes.get(class_name, BaseModel)
                self.__objects[key] = cls(**data)
        except FileNotFoundError:
            pass  # File doesn't exist, ignore
        except Exception as e:
            print(f"Error during reload: {e}")

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
