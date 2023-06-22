#!/usr/bin/python3
'''model for the department class'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String


class Department(BaseModel, Base):
    '''department class'''
    __tablename__ = "departments"
    name = Column(String(255), nullable=False)
