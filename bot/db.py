import os

from peewee import *

db = PostgresqlDatabase('users.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    pass

class Fraction(BaseModel):
    title = CharField(null=False)
    description = CharField(null=False)
    leader = ForeignKeyField(User, backref='fraction')

class User(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = IntegerField(unique=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    fraction = ForeignKeyField(Fraction, backref='member')

if not os.path.exists('users.db'):
    db.create_tables([User, Fraction])
