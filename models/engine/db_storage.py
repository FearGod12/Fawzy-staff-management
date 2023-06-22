#!/usr/bin/python3
'''SQLAchemy storage engine'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.basemodel import Base
from models.staff import Staff
from models.admin import Admin
from models.department import Department

classes = [Admin, Staff, Department]


class DBStorage:
    '''DBStorage class'''
    __engine = None
    __session = None

    def __init__(self):
        '''class constructor'''
        FSM_MYSQL_USER = getenv('FSM_MYSQL_USER')
        FSM_MYSQL_PWD = getenv('FSM_MYSQL_PWD')
        FSM_MYSQL_HOST = getenv('FSM_MYSQL_HOST')
        FSM_MYSQL_DB = getenv('FSM_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(FSM_MYSQL_USER, FSM_MYSQL_PWD,
                                             FSM_MYSQL_HOST, FSM_MYSQL_DB))

    def reload(self):
        '''reload data from Mysql database'''
        Base.metadata.create_all(self.__engine)
        mysession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(mysession)

    def new(self, obj):
        '''adds obj to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''save or commits all changes of the current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes obj from database'''
        if obj is not None:
            self.__session.delete(obj)

    def rollback(self):
        '''rolls back the current Sqlalchemy session
        after a failed flush occurred
        just for testing purposes'''
        self.__session.rollback()

    def all(self, cls=None):
        '''returns all obj in storage associated with the cls
        if cls is None then it returns all objs'''
        objs_dict = {}
        if cls is None:
            for each in classes:
                objs = self.__session.query(each).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    objs_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                objs_dict[key] = obj

        return objs_dict

    def close(self):
        '''closes the current database session'''
        self.__session.remove()

    def get(self, cls, id, attr=None):
        '''returns an obj of class cls with the matching id
        or None if not exist. if attr is given then returns the given attribute
        of the obj in question'''
        if not cls or cls not in classes:
            return None
        if attr is not None:
            obj = self.all(cls).get(cls.__name__ + '.' + id, None)
            if obj is None:
                return obj
            return getattr(obj, attr, None)
        return self.all(cls).get(cls.__name__ + '.' + id, None)

    def match(self, cls, attr={}):
        '''returns the object belonging to the class cls
        that has the email'''
        if not cls or cls not in classes or len(attr) == 0:
            return None
        for key, value in attr.items():
            result = self.__session.query(cls).filter(getattr(cls, key) == value).first()
            if result is None:
                return None
        return result
