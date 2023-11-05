from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=21627756,
    api_hash="fe77fbf0cae9f7f5ece37659e2466cf1",
    bot_token="6445765629:AAGYzIlQDSfpBcqlklDJ_WU_tNrZif_Pcrs",
    plugins=dict(root="MZombie")
    )

DEVS = ["lll_lll89"]

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
