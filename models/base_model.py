#!/usr/bin/python3
"""base model module that defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel():
    """ Base model class that defines all common attributes/methods for othe classes"""
    def __init__(self, *args, **kwargs):
        """Initializes the new instance of class BaseModel
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when is created and will be updated every time object change"""
        if kwargs is not None:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id =str(uuid.uuid4())
            self.create_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints a formated and readable string format"""
        print("[{}] ({}) {}". format(__name__, self.id,
            self.__dict__)

    def save(self):
        """updates public instance attribute updated_at to datetime now"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        dict_inst = self.__dict__
        dict_inst["__class__"] = type(self).__name__
        dict_inst["created_at"] = dict_inst["created_at"].isoformat()
        dict_inst["updated_at"] = dict_inst["updated_at"].isoformat()
        return dict_inst
