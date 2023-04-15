from pyrogram import Client,  filters, enums
from pyrogram.types import Message 
from pyromod import listen
from pymongo import MongoClient
from config import API_ID, API_HASH, DB_URI
from asyncio.exceptions import TimeoutError

mongo_client = MongoClient(DB_URI)
mongo_db = mongo_client["cloned_bots"]


SI_TEXT = "Hey {} Send Your session Without error /cancel to cancel proccess"

@Client.on_message(filters.command("add"))
async def add_new_session(bot, message):
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
        me = await string.get_me()
        name = me.first_name
        details = {
            'user_id': user,
            'session': session,
            'name': name,
            'status': True
        }
        mongo_db.bots.insert_one(details)
        await string.send_message("me", f"#Auto Accept Started By @MlZ_support")    
        await msg.edit("Completed Your Session Has Been Started type .run in your chat accept all request")
    except Exception as e:
        print(e)
        await msg.edit(f"error {e}")

@Client.on_message(filters.command("mystring"))
async def find_sessions(bot, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    sessions = list(mongo_db.bots.find({'user_id': user_id}))
    if len(bots) == 0:
        await message.reply_text("You haven't cloned any bots yet.")
        return
    text = "<b>Your cloned bots:</b>"
    btn = [
            [
                InlineKeyboardButton(
                    text=f"- {user['name']}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for user in sessions
        ]
