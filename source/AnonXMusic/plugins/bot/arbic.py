import asyncio
from pyrogram import Client, filters


from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     filters.command(["/help", "ميوزك"],"")  
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/61dd842dd42e87cef8091.jpg",
caption=f"""<b>- اضغـط الـزر بالاسفـل لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𝄞", callback_data="arbic"
                ),
                ],
            ]
        ),
    )
