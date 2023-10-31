from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=23308690,
    api_hash="0a64b7fb353afea42c8847bd5ae5c744",
    bot_token="6923150925:AAFZ_6cSBZp2iehivEPE816D-5WPvEyyipI",
    plugins=dict(root="MZombie")
    )

DEVS = ["ASAKIOb","lll_lll89"]

bot_id = bot.bot_token.split(":")[0]

async def start_vgtrebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "ASAKIOb"
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
