#!/usr/bin/python3
'''model for the admin class'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, String
import hashlib


class Admin(BaseModel, Base):
    '''Admin class'''
    __tablename__ = "admins"
    surname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    position = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        '''class constructor'''
        if "password" in kwargs:
            password = kwargs["password"]
            m = hashlib.md5()
            m.update(str.encode(password))
            kwargs["password"] = m.hexdigest()
        super().__init__(*args, **kwargs)

    @property
    def name(self):
        '''returns Surname, firstname and lastname '''
        return "{} {} {}".format(self.surname, self.firstname, self.lastname)
