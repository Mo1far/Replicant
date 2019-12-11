from peewee import *


db = SqliteDatabase('replicant.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db
