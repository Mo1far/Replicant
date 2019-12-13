from aiogram import types
from peewee import *

from bot.models.core import BaseModel
from bot.models.fraction import Fraction
from bot.utils import aiowrap


class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    fraction = ForeignKeyField(Fraction, backref="member", null=True)
    locale = CharField(max_length=3, default="en")

    @classmethod
    def create_user(cls, tg_user: types.User):
        cls.create(
            user_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
            locale=tg_user.locale,
        )

    @classmethod
    def user_exist(cls, user_id) -> bool:
        return cls().select().where(user_id=user_id).exists()

    @classmethod
    @aiowrap
    def get_user(cls, tg_user: types.User) -> (bool, "User"):
        query = User.select().where(cls.user_id == tg_user.id)
        is_new = False
        if not query.exists():
            is_new = True
            User.create_user(tg_user)

        return is_new, query.get()
