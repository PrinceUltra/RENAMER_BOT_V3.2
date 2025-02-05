import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7796785435:AAGeOejDJpt7jAsKvEM4mMa-sVj-sCoTIQ4")

API_ID = int(os.environ.get("API_ID", "24125441"))

API_HASH = os.environ.get("API_HASH", "0cebf5d00afb7cf120bfcb39a4afbab5")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
