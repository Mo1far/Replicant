import os

from bot.models.user import User
from bot.models.fraction import Fraction
from bot.models.core import db


if not os.path.exists("replicant.db"):
    db.create_tables([User, Fraction])
