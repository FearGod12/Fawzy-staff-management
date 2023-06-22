#!/usr/bin/python3
'''init file with the storage instance to be usedfor thwe project'''

from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
