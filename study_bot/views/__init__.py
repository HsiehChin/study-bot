from . import record
from . import bot

blueprints = [(record.record_api, "/records"), (bot.bot_api, "/bot")]
