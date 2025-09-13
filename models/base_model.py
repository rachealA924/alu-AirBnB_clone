#!/usr/bin/python3
"""
Module base_model
Defines the BaseModel class for AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all AirBnB objects.
    Handles id, creation, update, and serialization.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        If kwargs is not empty, create attributes from the dictionary.
        Otherwise, create a new instance with a unique id and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Update updated_at timestamp and save object to storage.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of instance,
        converting datetime attributes to ISO format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
