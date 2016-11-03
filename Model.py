from  peewee import *

from Database import *



db = SqliteDatabase('meteorLibrary.db')

class Base_model(Model):
    class Meta:
        database = db
        # to create database
class meteorite_sighting_model(Base_model):
    name = CharField(70, default=None, unique=True)
    mass = FloatField(70, default=0.0)
    year = IntegerField(70, default=0000)
    latitude = FloatField(70, default=0.00)
    longitude = FloatField(80, default=0.00)
