from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

import bot.keyboards as kb
from bot.middlewares.i18n import _
from bot.misc import dp
from bot.db import User


@dp.message_handler(commands=["card"])
async def user_card(msg: types.Message):
    user = User.get_user(types.User.get_current())
    await msg.reply(_("User №{}".format(user.user_id)), disable_notification=True)
