from pyrogram import Client,  filters, enums
from pyrogram.types import Message,  InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyromod import listen
from pymongo import MongoClient
from config import API_ID, API_HASH, DB_URI, DB_NAME
from asyncio.exceptions import TimeoutError

mongo_client = MongoClient(DB_URI)
mongo_db = mongo_client[DB_NAME]


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
        users_id = me.id
        details = {
            'user_id': user,
            'session': session,
            'name': name,
            'session_id': users_id,
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
    if len(sessions) == 0:
        await message.reply_text("You haven't cloned any bots yet.")
        return
    text = "<b>Your cloned bots:</b>"
    btn = [
            [
                InlineKeyboardButton(
                    text=f"- {user['name']}",
                    callback_data=f"u_settings#{user['session_id']}",
                )
            ]
            for user in sessions
        ]
    await message.reply_text("Yor Session Select From Below", reply_markup=InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex('^u_settings'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, session_id = query.data.split('#')
    buttons = [[
            InlineKeyboardButton("Start Session", callback_data=f"start_s#{session_id}")
        ], [
            InlineKeyboardButton("Stop", callback_data=f"stop_s#{session_id}"),
            InlineKeyboardButton("Delete", callback_data=f"del_s#{session_id}")
       ]]
    await query.message.edit_text("Change your Session Settings", reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "stop_s":
        i, session_id = query.data.split('#')
        session = mongo_db.bots.find_one(session_id': session_id}))
        session_string = {session['session']}
        try:
            await session_string.stop()
