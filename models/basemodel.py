#!/usr/bin/python3
'''the basemodel from which other models inherit'''

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage

Base = declarative_base()

class BaseModel:
    '''Basemodel class and its methods'''
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=lambda: datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """class constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key not in ["created_at", "updated_at"]:
                    setattr(self, key, value)

    def save(self):
        """saves object to storage"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """deletes an object from storage"""
        storage.delete(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of an object"""
        obj = {}
        attr = ['_sa_instance_state', 'password']
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        obj.updated(self.__dict__)
        for item in attr:
            if item in obj.keys():
                obj.pop(item)

        for item in ["created_at", "updated_at"]:
            if obj.get(item):
                obj.update({item: str(obj.get(item).strftime(date_format))})
        return obj
