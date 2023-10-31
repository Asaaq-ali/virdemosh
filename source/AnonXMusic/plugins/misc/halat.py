import asyncio

import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app, Telegram
from random import  choice, randint


@app.on_message(filters.command(["استوري","حالات","فيديو"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,100)
    url = f"https://t.me/hs6a7/{rl}"
    await client.send_audio(message.chat.id,url,caption="<b> تـم اختيـار الأستوري لـك ¦ 🌹</b>\n ✧ [<a href=https://t.me/Mlze1bot> 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂</a>]",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot")
                ],
            ]
        )
    )

@app.on_message(filters.command(["اقتباسات", "اقتباس"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,200)
    url = f"https://t.me/akttbas6/{rl}"
    await client.send_photo(message.chat.id,url,caption="<b> تـم اختيـار الأقتباس لـك ¦ 🌹</b>\n ✧ [<a href=https://t.me/Mlze1bot> 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂</a>]",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot")
                ],
            ]
        )
     )


