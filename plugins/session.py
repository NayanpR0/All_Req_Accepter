from pyrogram import Client,  filters, enums
from config import API_ID, API_HASH

@Client.on_message(filters.command("clone") & filters.user(ADMINS))
async def add_new_session(bot, message):
    user = message.from_user.id
    msg = await message.reply_text("processing")
    try:
        session = message.text.split(" ", maxsplit=1)[1]
    except Exception:
        await msg.edit("Give session")
    
