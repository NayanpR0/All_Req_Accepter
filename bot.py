from pyrogram import Client
from config import *

bot = Client(
           "Accepted-all",
           bot_token=TOKEN,
           api_id=API_ID,
           api_hash=API_HASH,
           plugins=dict(root='plugins'))

bot.run()
