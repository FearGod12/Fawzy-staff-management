#!/usr/bin/python3
'''model for the staff class'''

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Staff(BaseModel, Base):
    '''staff class'''
    __tablename__ = "staffs"

    surname = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    phone = Column(String(15), nullable=True, unique=True)
    address = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
    passport = Column(String(255), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    date_engaged = Column(Date, nullable=True)
    next_of_kin_surname = Column(String(255), nullable=True)
    next_of_kin_firstname = Column(String(255), nullable=True)
    next_of_kin_address = Column(String(255), nullable=True)
    next_of_kin_id = Column(String(255), nullable=True)
    department_id = Column(String(255), ForeignKey('departments.id'),
                           nullable=False)

    @property
    def department(self):
        '''returns the name of the department of the object'''
        from models.department import Department
        from models import storage
        name = storage.get(Department, self.department_id, attr="name")
        return name

    @property
    def name(self):
        '''returns Surname, firstname and lastname '''
        return "{} {} {}".format(self.surname, self.firstname, self.lastname)

    @property
    def next_of_kin_name(self):
        '''returns next of kin full name'''
        return "{} {}".format(self.next_of_kin_surname,
                              self.next_of_kin_firstname)
