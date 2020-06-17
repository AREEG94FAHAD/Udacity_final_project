import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'areeg'
database_path = "postgres://{}:{}@{}/{}".format('postgres', 'areeg','localhost:5432', database_name)

db = SQLAlchemy()

# setup_db(app)

def setup_db(app, database_path = database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Person(db.Model):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    department = Column(String)
    relationship("Artical", backref="articals", lazy='dynamic')

    
    def __init__(self, name, department):
        self.name = name
        self.department = department

    

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        
        return {
            'id':self.id,
            'name':self.name,
            'department':self.department
        }

class Artical(db.Model):
    __tablename__ = 'articals'

    id = Column(Integer, primary_key = True)
    data = Column (String)
    category = Column (String)
    person_id = Column(Integer, ForeignKey('persons.id'))

    def __init__(self, data, person_id, category):
        self.data = data
        self.category = category
        # self.person_id = person_id

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            'id':self.id,
            'data':self.data,
            'category':self.category,
            'person_id':self.person_id
        }


    

