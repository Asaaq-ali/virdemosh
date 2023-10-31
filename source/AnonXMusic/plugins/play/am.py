import asyncio
from pyrogram import Client, filters
from config import BANNED_USERS

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
  filters.command(
      [
         "فلم", 
         "أفلام",    
       ],""
  )
    & filters.group
    & ~BANNED_USERS
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/94c43633525702295679d.mp4",
        caption=f"""✧<b> اهلين فيك في قسم أفلام دينا</b> \n\n <b>  لمشاهدة الأفلام أضغط على الزر تحت </b> \n\n•<b>  Developer -› [ASAAQ]\n• Channel -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]</b> """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مشاهدة الأفلام", callback_data="film " + str(message.from_user.id)),
                ],[

                    InlineKeyboardButton(
                        "تحديثات دينا 🥢", url=f"https://t.me/Mlze1bot"),

                ],
            ]
        ),
)
