from pyrogram import Client,  filters, enums
from pyrogram.types import Message 
from pyromod import listen
from config import API_ID, API_HASH
from asyncio.exceptions import TimeoutError

SI_TEXT = "Hey {} Send Your session Without error /cancel to cancel proccess"

@Client.on_message(filters.command("add"))
async def add_new_session(bot, message: Message):
    user = message.from_user.id
    msg = await message.reply_text("processing")
    session = message.text.split(" ", maxsplit=1)[1]
    try:        
        string = Client(name="user-account",
              session_string=session,
              api_id=API_ID,
              api_hash=API_HASH,
              plugins={"root": "user_plugins"},
              workers=300,
              )
        await string.start()
        await msg.edit("Completed Your Session Has Been Started type .run in your chat accept all request")
    except Exception as e:
        print(e)
        await msg.edit(f"error {e}")

