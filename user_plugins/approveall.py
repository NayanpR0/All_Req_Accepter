import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["run", "approve"], CMND) & main_chat)                     
async def approve(client: Client, message: Message):
    chat=message.chat
    await message.delete()
    msg = await message.reply_text("Proccesing")
    try:
        await client.approve_all_chat_join_requests(chat.id)#1
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#2
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#3
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#4
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#5
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#6
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#7
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#8
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#9
        await asyncio.sleep(4)
        await client.approve_all_chat_join_requests(chat.id)#10
        await msg.edit("Complted approved all Chat Join Reqs")
  except FloodWait as x:
