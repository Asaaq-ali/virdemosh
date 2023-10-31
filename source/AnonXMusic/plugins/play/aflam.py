###  zx حقوق سورس سهى تخمط اخمط عينك واطلعك من التلي مثل الجرذ

import asyncio

from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from AnonXMusic import app
from config import BANNED_USERS

#########################################################################################
#########################################################################################
#########################         #  𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂  𖥀 #             ##########################
################################### https://t.me/Mlze1bot ######################################################
#########################################################################################
@app.on_message(
  filters.command(
      [
         "الافلام", 
         "مسلسلات",    
       ],""
  )
    & filters.group
    & ~BANNED_USERS
)
async def aflamAR(client: Client, message: Message):
    await message.reply_text(f"""✧<b> اهلين فيك في قسم افلام دينا</b>\n\n 𝑺𝒐𝒖𝒓𝒄𝒆 -› [ 𝒅𝒊𝒏𝒂 ] """,
        reply_markup=InlineKeyboardMarkup(
              [

        [InlineKeyboardButton("افلام 📼", callback_data="film " + str(message.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="asaaq1 " + str(message.from_user.id))],
  
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

       ]
    ), 
     disable_web_page_preview=True
) 
                            
# Replay Edit
@app.on_callback_query(filters.regex("^aflamAR2 (\\d+)$"))
async def aflamAR2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 📼", callback_data="xfilum " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="asaaq1 " + str(m.from_user.id))],
  
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام والمسلسلات \n√", reply_markup=keyboard)

######رد الافلام#######
@app.on_callback_query(filters.regex("^xfilum (\\d+)$"))
async def film(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوري 🇰🇷", callback_data="zasaq9 " + str(m.from_user.id))],
        [InlineKeyboardButton("صيني 🇨🇳", callback_data="action " + str(m.from_user.id))],
   
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام \n√", reply_markup=keyboard)
######رد المسلسلات #####
@app.on_callback_query(filters.regex("^asaaq1 (\\d+)$"))
async def asaaq1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوري 🇰🇷", callback_data="xasaaq " + str(m.from_user.id))],
        [InlineKeyboardButton("صيني 🇨🇳", callback_data="xasaaq " + str(m.from_user.id))],
   
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة المسلسلات \n√", reply_markup=keyboard)

#############################################################################قائمة المسلسلات#######الكوريه#####
@app.on_callback_query(filters.regex("^xasaaq (\\d+)$"))
async def xasaaq(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ حب عبر حياتين", callback_data="Xasa1 " + str(m.from_user.id))] +
    
        [InlineKeyboardButton("عوده للمسلسلات ⏺", callback_data="asaaq1 " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة المسلسلات الكوريه \n√", reply_markup=keyboard)

#########مسلسل الاول #####
@app.on_callback_query(filters.regex("^Xasa1 (\\d+)$"))
async def Xasa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯  الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="xasaaq " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم المسلسل  :حب عبر حياتين
    🌎 الدولة : كوريا
    🗄 تصنيف : اكشن, رومنسي
    📜 قصة المسلسل :
بعد أن أصبحت ياو ليانغ ليانغ ‘شابين ضائعين’ فقدت حبها وفقدت وظيفتها فتحت بطريق الخطأ فجوة زمنية وفتحت الباب الغامض لكون موازٍ.
    """, reply_markup=keyboard)

######الحلقات المسلسل الاول ######
@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🐉", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الحلقة 1", callback_data="Xasaq1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحلقة 2 ", callback_data="Xasaaq2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحلقة 3", callback_data="Xasaaq3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحلقة 4", callback_data="Xasaaq4 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحلقة 5 ", callback_data="Xasaaq5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحلقة 6 ", callback_data="Xasaaq6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحلقة 7 ", callback_data="Xasaaq7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحلقة 8 ", callback_data="Xasaaq8 " + str(m.from_user.id))],

        [InlineKeyboardButton("الرئيسية ", callback_data="xasaaq " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("اهلا بك في قائمة مسلسل  حب عبر حياتيين ", reply_markup=keyboard)
#####حلقات المسلسل حب عبر حياتين #######
#الحلقة ١#
@app.on_callback_query(filters.regex("^Xasaq1 (\\d+)$"))
async def Xasaq1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_video(
        video=f"https://t.me/serii_film/78",
        caption=f"""الحلقة 1 من مسلسل حب حياتين""", reply_markup=keyboard)



#الحلقة 2#
@app.on_callback_query(filters.regex("^Xasaaq2 (\\d+)$"))
async def Xasaaq2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_video(
        video=f"https://t.me/serii_film/79",
        caption=f"""الحلقة 2 من مسلسل حب حياتين""", reply_markup=keyboard)



#الحلقة 3#
@app.on_callback_query(filters.regex("^Xasaaq3 (\\d+)$"))
async def Xasaaq3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_video(
        video=f"https://t.me/serii_film/80",
        caption=f"""الحلقة 3 من مسلسل حب حياتين""", reply_markup=keyboard)


##الحلقه 4###
@app.on_callback_query(filters.regex("^Xasaaq4 (\\d+)$"))
async def Xasaaq4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_video(
        video=f"https://t.me/serii_film/81",
        caption=f"""الحلقة 4 من مسلسل حب حياتين""", reply_markup=keyboard)


##الحلقه 5###
@app.on_callback_query(filters.regex("^Xasaaq5 (\\d+)$"))
async def Xasaaq5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton("الحلقات ", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton(" ⌞ 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ⌝ ", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.delete()
    await m.message.reply_video(
        video=f"https://t.me/serii_film/82",
        caption=f"""الحلقة 5 من مسلسل حب حياتين""", reply_markup=keyboard)



##الحلقه 6##
@app.on_callback_query(filters.regex("^Xasaaq6 (\\d+)$"))
async def Xasaaq6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/serii_film/83")
###الحلقه 7###
@app.on_callback_query(filters.regex("^Xasaaq7 (\\d+)$"))
async def Xasaaq7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/serii_film/84")
##الحلثة 8##
@app.on_callback_query(filters.regex("^Xasaaq8 (\\d+)$"))
async def Xasaaq8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/serii_film/85")
##النهايه####



#########################################################################################
#########################         # Aflam Comedy #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^zasaq9 (\\d+)$"))
async def zasaq9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ النبيل", callback_data="Xco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المرشحة الصادقة ", callback_data="Xco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المحتالون ", callback_data="Xco3 " + str(m.from_user.id))] +
     
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="asaaq1 " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة الافلام الكوريه \n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco1 (\\d+)$"))
async def Xco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="zasaq9 " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم  :  النبيل
    🌎 الدولة : كوريا
    🗄 تصنيف : اكشن
    📜 قصة الفيلم:
يسافر ملاكم نصف كوري-فلبيني إلى كوريا على أمل إيجاد والده،
ليجد نفسه مطارداً من قبل مجموعات مختلفة من الأشخاص
يسعون جميعهم خلفه دون أن يعرف سبب استهدافهم له.
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco2 (\\d+)$"))
async def Xco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="zasaq9 " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : المرشحة الصادقة 
        📖 انتاج سنة  : 2020
        🌎 الدولة : كوريا
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
تدور الأحداث عن عضوة مجلس وطني يجري الكذب في عروقها مجرى الدم لكن بعد حادثة غير متوقعة تجد نفسها مجبرة على قول الحقيقة أثناء شروعها في حملة إعادة انتخابها.

        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco3 (\\d+)$"))
async def Xco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="zasaq9 " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : المحتالون
         انتاج سنة : 2017
        🌎 الدولة : كوريا
        🗄 تصنيف : أكشن، اثاره، تشويق
        📜 قصة الفيلم:
يتحدث فيلم “The Swindlers” “عن جي سونغ” (هيون بن) هو محتال ذكي الذي يشكل خطة و يخدع فقط زملائه المحتالين ليمسك بـ جانغ دو تشيل و يقوم أولا بتجنيد المدعي العام هيو سو (يو جي تاي) ثم بقية المحتالين (باي سونغ وو)، وشون جا (نانا)، والرئيس كيم (أن سي-ها) ليلقون بـالطعم لـ سيونغ-غان (بارك سونغ-وونغ) اليد اليمنى لجانغ دو تشيل
        """, reply_markup=keyboard)



#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/2")


@app.on_callback_query(filters.regex("^XXco3 (\\d+)$"))
async def XXco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/6")


@app.on_callback_query(filters.regex("^XXco5 (\\d+)$"))
async def XXco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/7")

#####
@app.on_callback_query(filters.regex("^action (\\d+)$"))
async def action(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("النهاية ", callback_data="Xact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مصاصي الدماء ", callback_data="Xact2 " + str(m.from_user.id))],
   
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الاكشن الصينيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact1 (\\d+)$"))
async def Xact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : النهاية 
📖 انتاج سنة : 2019
🌎 الدولة : الصين
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور قصة الجزء الرابع حيث في العام 1964، بعد وفاة زوجته، يسافر إيب مان إلى سان فرانسيسكو لتخفيف التوترات بين أساتذة الكونغ فو المحليين وطالبه النجم، بروس لي، خلال البحث عن مستقبل أفضل لابنه.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact2 (\\d+)$"))
async def Xact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : مصاصي الدماء
📖 انتاج سنة : 2017
🌎 الدولة : الصين
🗄 تصنيف : اكشن , اثارة , رعب
📜 قصة الفيلم:
ينضم تيم تشيونج إلى منظمة إبادة مصاصي الدماء و هي منظمة سرية تهدف للقضاء عليهم و يديرها عمه تشاو، يقوم تيم لاحقاً بالحفاظ على حياة مصاصة الدماء سومار و يحاول حمايتها من قائدها الشرير الذي قام بدفنها و هي حية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^XXact1 (\\d+)$"))
async def XXact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/4")

@app.on_callback_query(filters.regex("^XXact3 (\\d+)$"))
async def XXact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/9")

##########################################قف هنا#####
