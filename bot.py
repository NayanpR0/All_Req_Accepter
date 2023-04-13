from pyrogram import Client
from pyromod import listen
from config import *

bot = Client(
           "Accepted-all",
           bot_token=BOT_TOKEN,
           api_id=API_ID,
           api_hash=API_HASH,
           plugins=dict(root='plugins'))

bot.run()
