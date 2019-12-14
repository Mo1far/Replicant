import os

from bot.models.core import db
from bot.models.fraction import Fraction
from bot.models.user import User

if not os.path.exists("replicant.db"):
    db.create_tables([User, Fraction])
