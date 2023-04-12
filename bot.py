from pyrogram import Client

Client = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins={"root": "plugins"},
             workers=300
             )

Client.start()
print("Bot Started!")

idle()

Client.stop()
print("Bot Stopped!")
