from pyrogram import Client,  filters, enums
from pyromod import listen
from config import API_ID, API_HASH

@Client.on_message(filters.command("add"))
async def add_new_session(bot, message):
    user = message.from_user.id
    msg = await message.reply_text("processing")
    try:
        session = message.text.split(" ", maxsplit=1)[1]
    except Exception:
        await msg.edit("Give session")
        return
    try:
        string = Client(name="user-account",
              session_string=session,
              api_id=API_ID,
              api_hash=API_HASH,
              )
        await string.start()
    except Exception as e:
        print(e)
