from peewee import *
from bot.models.application_record import BaseModel


class Fraction(BaseModel):
    title = CharField(null=False)
    description = CharField(null=False)
   #leader = ForeignKeyField(User, backref='fraction')
