import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
CMND = [".", "/", ":"]

@Client.on_message(filters.command(["run", "approve"], CMND) & (filters.group | filters.channel))                     
async def approve(client: Client, message: Message):
    chat=message.chat
    await message.delete()
    msg = await message.reply_text("Proccesing")
    try:
        await client.approve_all_chat_join_requests(chat.id)#1
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#2
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#3
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#4
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#5
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#6
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#7
        await asyncio.sleep(3)
        await client.approve_all_chat_join_requests(chat.id)#8
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#9
        await asyncio.sleep(2)
        await client.approve_all_chat_join_requests(chat.id)#10
        await msg.edit("Complted approved all Chat Join Reqs")
    except FloodWait as t:
        await asyncio.sleep(t.x)


@Client.on_message(filters.command(["nor", "appr"], CMND) & (filters.group | filters.channel))                     
async def approve(client: Client, message: Message):
    chat = message.chat.id
    limits = 3
    async for limit in limits:
         try:
             await client.approve_all_chat_join_requests(chat.id)#1
         except FloodWait as t:
             await asyncio.sleep(t.x)
             await client.approve_all_chat_join_requests(chat.id)#1
   
    
