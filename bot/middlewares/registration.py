import asyncio

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.db import User
from bot.middlewares.i18n import _


class RegistrationMiddleware(BaseMiddleware):
    async def on_process_message(self, msg: types.Message):
        if not User.user_exist(msg.from_user.id):
            User.create_user(
                user_id=msg.from_user.id,
                username=msg.from_user.username,
                first_name=msg.from_user.first_name,
                last_name=msg.from_user.last_name,
            )
        await msg.answer(_("Pagination"))
