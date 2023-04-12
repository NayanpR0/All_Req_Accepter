from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep

START_MSG = "HI {}"

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton('Oᴡɴᴇʀ', user_id='1957296068'),
        InlineKeyboardButton('Gʀᴏᴜᴘ', url='https://t.me/MaSTeR_filims')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=START_MSG.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
    )
