import asyncio

from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from AnonXMusic import app
from config import BANNED_USERS


@app.on_message(
  filters.command(
      [
         "انمي", 
         "مسلسل",    
       ],""
  )
    & filters.group
    & ~BANNED_USERS
)
async def anmi(client: Client, message: Message):
    await message.reply_text(f"""✧<b> اهلين فيك في قسم أنـــمي دينا</b>\n\n 𝑺𝒐𝒖𝒓𝒄𝒆 -› [ 𝒅𝒊𝒏𝒂 ] """,
        reply_markup=InlineKeyboardMarkup(
              [

        [InlineKeyboardButton("انمي 📼", callback_data="anmie2 " + str(message.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="asaaq1 " + str(message.from_user.id))],
  
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

       ]
    ), 
     disable_web_page_preview=True
) 
@app.on_callback_query(filters.regex("^anmie (\\d+)$"))
async def anmie(c: Client, m: CallbackQuery):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(" اكس هنتر ", callback_data="hxsoha " + str(m.from_user.id))],
        
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.reply_text("◍ اهلا بيك في قايمة الانمي\n√", reply_markup=keyboard)


# anime
@app.on_callback_query(filters.regex("^anmie2 (\\d+)$"))
async def anmie2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("أنمي هنتر القناص", callback_data="hxsoha " + str(m.from_user.id))], 
        
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قايمة الانمي\n√", reply_markup=keyboard)


########################################################################################
#########################################################################################
##############   hinter x hinter  #########
@app.on_callback_query(filters.regex("^hxsoha (\\d+)$"))
async def hxsoha(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الجزء الاول 1⃣", callback_data="hxsoha1 " + str(m.from_user.id))],
        [InlineKeyboardButton("الجزء التاني 2⃣", callback_data="hxsoha2 " + str(m.from_user.id))],
        
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ أهلا بيك في قايمة اجزاء هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha1 (\\d+)$"))
async def hxsoha1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ الحلقه 1", callback_data="Xsoha1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 2", callback_data="Xsoha2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 3", callback_data="Xsoha3 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 4", callback_data="Xsoha4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 5", callback_data="Xsoha5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 6", callback_data="Xsoha6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 7", callback_data="Xsoha7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 8", callback_data="Xsoha8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 9", callback_data="Xsoha9 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 10", callback_data="Xsoha10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 11", callback_data="Xsoha11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 12", callback_data="Xsoha12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 13", callback_data="Xsoha13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 14", callback_data="Xsoha14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 15", callback_data="Xsoha15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 16", callback_data="Xsoha16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 17", callback_data="Xsoha17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 18", callback_data="Xsoha18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 19", callback_data="Xsoha19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 20", callback_data="Xsoha20 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="hxsoha2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="hxsoha " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],
    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الاولي من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha2 (\\d+)$"))
async def hxsoha2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 21", callback_data="Xsoha21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 22", callback_data="Xsoha22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 23", callback_data="Xsoha23 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 24", callback_data="Xsoha24 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 25", callback_data="Xsoha25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 26", callback_data="Xsoha26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 27", callback_data="Xsoha27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 28", callback_data="Xsoha28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 29", callback_data="Xsoha29 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 30", callback_data="Xsoha30 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 31", callback_data="Xsoha31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 32", callback_data="Xsoha32 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 33", callback_data="Xsoha33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 34", callback_data="Xsoha34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 35", callback_data="Xsoha35 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 36", callback_data="Xsoha36 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 37", callback_data="Xsoha37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 38", callback_data="Xsoha38 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 39", callback_data="Xsoha39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 40", callback_data="Xsoha40 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="hxsoha " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة التانيه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha3 (\\d+)$"))
async def hxsoha3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 41", callback_data="Xsoha41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 42", callback_data="Xsoha42 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 43", callback_data="Xsoha43 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 44", callback_data="Xsoha44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 45", callback_data="Xsoha45 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 46", callback_data="Xsoha46 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 47", callback_data="Xsoha47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 48", callback_data="Xsoha48 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 49", callback_data="Xsoha49 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 50", callback_data="Xsoha50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 51", callback_data="Xsoha51 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 52", callback_data="Xsoha52 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 53", callback_data="Xsoha53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 54", callback_data="Xsoha54 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 55", callback_data="Xsoha55 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 56", callback_data="Xsoha56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 57", callback_data="Xsoha57 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 58", callback_data="Xsoha58 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 59", callback_data="Xsoha59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 60", callback_data="Xsoha60 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hxsoha4 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة التالته من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha4 (\\d+)$"))
async def hxsoha4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 61", callback_data="Xsoha61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 62", callback_data="Xsoha62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 63", callback_data="Xsoha63 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 64", callback_data="Xsoha64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 65", callback_data="Xsoha65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 66", callback_data="Xsoha66 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 67", callback_data="Xsoha67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 68", callback_data="Xsoha68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 69", callback_data="Xsoha69 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 70", callback_data="Xsoha70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 71", callback_data="Xsoha71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 72", callback_data="Xsoha72 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 73", callback_data="Xsoha73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 74", callback_data="Xsoha74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 75", callback_data="Xsoha75 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 76", callback_data="Xsoha76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 77", callback_data="Xsoha77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 78", callback_data="Xsoha78 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 79", callback_data="Xsoha79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 80", callback_data="Xsoha80 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hxsoha5 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الرابعه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha5 (\\d+)$"))
async def hxsoha5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 81", callback_data="Xsoha81 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 82", callback_data="Xsoha82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 83", callback_data="Xsoha83 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 84", callback_data="Xsoha84 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 85", callback_data="Xsoha85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 86", callback_data="Xsoha86 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 87", callback_data="Xsoha87 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 88", callback_data="Xsoha88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 89", callback_data="Xsoha89 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 90", callback_data="Xsoha90 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 91", callback_data="Xsoha91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 92", callback_data="Xsoha92 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 93", callback_data="Xsoha93 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 94", callback_data="Xsoha94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 95", callback_data="Xsoha95 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 96", callback_data="Xsoha96 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 97", callback_data="Xsoha97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 98", callback_data="Xsoha98 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 99", callback_data="Xsoha99 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 100", callback_data="Xsoha100 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hxsoha6 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة الخامسه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha6 (\\d+)$"))
async def hxsoha6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 101", callback_data="Xsoha101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 102", callback_data="Xsoha102 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 103", callback_data="Xsoha103 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 104", callback_data="Xsoha104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 105", callback_data="Xsoha105 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 106", callback_data="Xsoha106 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 107", callback_data="Xsoha107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 108", callback_data="Xsoha108 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 109", callback_data="Xsoha109 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 110", callback_data="Xsoha110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ 111 الحلقه ", callback_data="Xsoha111 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 112", callback_data="Xsoha112 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 113", callback_data="Xsoha113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 114", callback_data="Xsoha114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 115", callback_data="Xsoha115 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 116", callback_data="Xsoha116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 117", callback_data="Xsoha117 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 118", callback_data="Xsoha118 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 119", callback_data="Xsoha119 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 120", callback_data="Xsoha120 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("➡️ التالي", callback_data="hxsoha7 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة السادسه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^hxsoha7 (\\d+)$"))
async def hxsoha7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقه 121", callback_data="Xsoha121 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 122", callback_data="Xsoha122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 123", callback_data="Xsoha123 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 124", callback_data="Xsoha124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 125", callback_data="Xsoha125 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 126", callback_data="Xsoha126 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 127", callback_data="Xsoha127 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 128", callback_data="Xsoha128 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 129", callback_data="Xsoha129 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 130", callback_data="Xsoha130 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 131", callback_data="Xsoha131 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 132", callback_data="Xsoha132 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 133", callback_data="Xsoha133 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 134", callback_data="Xsoha134 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 135", callback_data="Xsoha135 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 136", callback_data="Xsoha136 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 137", callback_data="Xsoha137 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 138", callback_data="Xsoha138 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 139", callback_data="Xsoha139 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 140", callback_data="Xsoha140 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 141", callback_data="Xsoha141 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 142", callback_data="Xsoha142 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 143", callback_data="Xsoha143 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 144", callback_data="Xsoha144 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 145", callback_data="Xsoha145 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 146", callback_data="Xsoha146 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقه 147", callback_data="Xsoha147 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقه 148", callback_data="Xsoha148 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="hxsoha6 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="anmie2 " + str(m.from_user.id))],
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂]", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في القايمة السابعه من #القناص هنتر اكس هنتر\n√", reply_markup=keyboard)


########################################################################################################################
########################################################################################################################
#######################################################################################################################

@app.on_callback_query(filters.regex("^Xsoha1 (\\d+)$"))
async def Xsoha1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/2", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha2 (\\d+)$"))
async def Xsoha2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/3", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha3 (\\d+)$"))
async def Xsoha3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/4", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha4 (\\d+)$"))
async def Xsoha4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/5", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha5 (\\d+)$"))
async def Xsoha5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/6", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha6 (\\d+)$"))
async def Xsoha6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/7", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha7 (\\d+)$"))
async def Xsoha7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/8", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha8 (\\d+)$"))
async def Xsoha8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/9", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha9 (\\d+)$"))
async def Xsoha9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/10", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha10 (\\d+)$"))
async def Xsoha10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/11", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha11 (\\d+)$"))
async def Xsoha11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/12", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha12 (\\d+)$"))
async def Xsoha12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/13", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha13 (\\d+)$"))
async def Xsoha13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/14", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha14 (\\d+)$"))
async def Xsoha14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/15", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha15 (\\d+)$"))
async def Xsoha15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/16", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha16 (\\d+)$"))
async def Xsoha16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/17", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha17 (\\d+)$"))
async def Xsoha17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/18", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha18 (\\d+)$"))
async def Xsoha18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/19", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha19 (\\d+)$"))
async def Xsoha19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/20", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha20 (\\d+)$"))
async def Xsoha20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/21", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha21 (\\d+)$"))
async def Xsoha21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/22", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha22 (\\d+)$"))
async def Xsoha22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/23", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha23 (\\d+)$"))
async def Xsoha23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/24", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha24 (\\d+)$"))
async def Xsoha24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/25", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha25 (\\d+)$"))
async def Xsoha25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/26", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha26 (\\d+)$"))
async def Xsoha26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/27", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha27 (\\d+)$"))
async def Xsoha27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/29", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha28 (\\d+)$"))
async def Xsoha28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/30", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha29 (\\d+)$"))
async def Xsoha29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/31", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha30 (\\d+)$"))
async def Xsoha30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/32", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha31 (\\d+)$"))
async def Xsoha31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/33", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha32 (\\d+)$"))
async def Xsoha32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/34", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha33 (\\d+)$"))
async def Xsoha33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/35", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha34 (\\d+)$"))
async def Xsoha34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/36", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha35 (\\d+)$"))
async def Xsoha35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/37", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha36 (\\d+)$"))
async def Xsoha36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/38", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha37 (\\d+)$"))
async def Xsoha37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/39", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha38 (\\d+)$"))
async def Xsoha38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/40", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha39 (\\d+)$"))
async def Xsoha39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))], 
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/41", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsoha40 (\\d+)$"))
async def Xsoha40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤??", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="hxsoha1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_audio("https://t.me/anmihuntr/42", reply_markup=keyboard)
