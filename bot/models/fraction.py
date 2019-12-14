from peewee import *

from bot.models.core import BaseModel


class Fraction(BaseModel):
    title = CharField(null=False)
    description = CharField(null=False)
    # leader = ForeignKeyField(User, backref='fraction')
