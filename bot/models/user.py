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
    locale = CharField(max_length=3, null=True)
    start_conversation = TimestampField()

    @classmethod
    def create_user(cls, tg_user: types.User):
        cls.create(
            user_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
            locale=tg_user.language_code,
        )

    @classmethod
    def user_exist(cls, user_id) -> bool:
        return cls().select().where(user_id=user_id).exists()

    @classmethod
    @aiowrap
    def get_user(cls, tg_user: types.User) -> ("User", bool):
        return User.get_or_create(
            user_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
            locale=tg_user.locale,
        )
