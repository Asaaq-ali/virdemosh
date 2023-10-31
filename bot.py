from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=21627756,
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1",
    bot_token="6496026062:AAGtP4jAMXb3Mel1ukEfkIdjzLjUjePZFZA",
    plugins=dict(root="MZombie")
    )

DEVS = ["ASAKIOb","lll_lll89"]

bot_id = bot.bot_token.split(":")[0]

async def start_bot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
