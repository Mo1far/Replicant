from peewee import *

from bot.models.core import BaseModel
from bot.models.fraction import Fraction


class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    fraction = ForeignKeyField(Fraction, backref="member")
