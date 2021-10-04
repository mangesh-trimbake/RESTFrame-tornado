
from rest_sqalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    print("Base class called")
    __abstract__  = True
    __private_list__ = list()

    def isBaseFrom():
        return True
