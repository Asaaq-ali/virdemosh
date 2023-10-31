from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app as Client
from AnonXMusic import app


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""<b>- مرحبا عـزيـزي  </b>  \n
<b>- في قسم تشغيل الأغاني والفيديو في المكالمات</b>\n
<b>- استخدم الازرار لـ تصفـح اوامـر الميـوزك</b> """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت لـ مجموعتك ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [                   InlineKeyboardButton("طريقة التشغيل", callback_data="bcmds"),
                    InlineKeyboardButton("طريقة التفعيل", callback_data="bhowtouse"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>- عـزيـزي   !</b>
<b>- استخـدم الازرار بالاسفل لمعرفة طريقة التشغيل</b>
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("العودة", callback_data="arbic")
                ],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> اوامــر التشغيــل :</b>
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
» شغل/دينا شغلي (اسم الموسيقى/رابـط )
لـ تشغيل الموسيقى في المحادثة الصوتية 
» لايف ( بالرد على ملف/رابـط)
لـ تشغيل مقطع فيديو موجود في الدردشـه
» شغل/دينا شغلي (اسم الفيديو/رابـط)
لـ تشغيل مقطع فيديو 
» /vstream
لـ تشغيل بث مباشر
» القائمه
لـ عرض قائمة التشغيل
» فيديو
لـ تحميل مقطع فيديو
» بحث/اغنيه
لـ تحميل ملف صوتي 
» ابحث
لـ البحث عن روابط يوتيوب
» بنج
لـ عرض سرعة الاستجابة
» /uptime
لـ عرض وقت تشغيل البوت
» /alive
لـ عرض معلومات البوت 
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> اوامـر التحكم الخاصـه بـ الادمنيـة :</b>
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
» قف/قفي - ايقاف التشغيل موقتأ
» كمل/استمر - لاستكمال التشغيل
» تخطي/دينا طفيها - لتخطي تشغيل الحالي
» ايقاف/انهاء - لايقاف تشغيل الحالي
» دينا اسكتي/اسكتي - لكتم البوت في المحادثة
» دينا تكلمي/تكلمي - الغاء كتم الحساب المساعد
» ريلود - لتحديث قائمة الادمن للتحكم في البوت
» /المتصلين - لـ جلب قائمـة ب اسماء المتواجدين ع المكالمـه
» مين في الكول - لـ جلب قائمـة ب اسماء المتواجدين ع المكالمـه
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )
@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> طريقة تفعيل البوت في مجموعتك :</b>
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
<b>1- اضف البوت الى مجموعتك</b>
<b>2- ترقية البوت مشرف كامل الصلاحيه</b>
3- لـ تحديث قائمة الادمن ارسل `ريلود`
<b>- اضف الحساب المساعد الى مجموعتك (يوزر المساعد ع نبذة البوت)</b>
<b>4- تأكد من تشغيل المحادثة الصوتية<b>
<b>5- اذا واجهت خطأ قم بكتابة الام* `ريلود`</b>
™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="arbic")]]
        ),
    )
