import asyncio
from pyrogram import Client, filters
from AnonXMusic import app
import random
from config import BANNED_USERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app
from AnonXMusic.utils.database import get_served_chats
from config import LOGGER_ID

iddof=[] 

@app.on_message(
    filters.command(["صورتي"],"")
    & filters.group
    & ~BANNED_USERS
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا طرف انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
      

#             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #



async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"🌹 تم اضافة البوت لجروب جديد ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ **الدردشة** › : {matlabi_jhanto}\n┣★ **ايدي الدردشة** › : {chat_id}\n┣★ **يوزر الدردشه** › : {chatusername}\n┣★ **مجموع الدردشات** › : {served_chats}\n┣★ **اضيف بواسطة** › :\n┗━━━ {added_by}"
        await lul_message(LOGGER_ID, lemda_text)
