import html
import random
import SaitamaRobot.modules.gun_game_string as gun_game_string
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from telegram.ext import CallbackContext, run_async

@run_async
def guns_name2(update: Update, context: CallbackContext):
  args = context.args
  update.effective_message.reply_text(random.choice(gun_game_string.GUNS2))
