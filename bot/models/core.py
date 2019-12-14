from peewee import *

db = SqliteDatabase("replicant.db")


class BaseModel(Model):
    class Meta:
        database = db
