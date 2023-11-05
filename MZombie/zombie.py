#'‹ ٰ💸 ⇣ سورس القيصر ⇣ 💸 › .'#
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import random
from bot import DEVS

API_ID = int("21627756")
API_HASH = "fe77fbf0cae9f7f5ece37659e2466cf1"
Bots = []
off =None
ch = "Mlze1bot"
@Client.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.username in DEVS:
     return await message.reply_text("الصانع معطل")
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
   message.continue_propagation()
   

@Client.on_message(filters.command(["《صنع جلسه》"], ""))
async def aliehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("اضغط لاستخراج الجلسه", url=f"https://t.me/Mlze1bot"),
                InlineKeyboardButton("𝗔𝗦𝗔𝗔𝗤 𖠁", url=f"https://t.me/ASAKIOb"),
            ],
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/c37de0fdccdad7e391714.jpg",
        caption="",
        reply_markup=keyboard,
    )
    
@Client.on_message(filters.command(["《السورس》"], ""))
async def alivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝙶𝚁𝙾𝚄𝙿️", url=f"https://t.me/Mlze1bot"),
                InlineKeyboardButton("𝗔𝗦𝗔𝗔𝗤 𖠁", url=f"https://t.me/ASAKIOb"),
            ],
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/7799fb8eadb3d501be153.jpg",
        caption="",
        reply_markup=keyboard,
    )
    
@Client.on_message(filters.command(["《مطور السورس》"], ""))
async def caesar(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝗔𝗦𝗔𝗔𝗤 𖠁", url=f"https://t.me/ASAKIOb"),
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴️", url=f"https://t.me/Mlze1bot"),
            ],
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/c6fcc8d4d4a02dfc62983.jpg",
        caption="",
        reply_markup=keyboard,
    )    
    
@Client.on_message(filters.command(["《تفعيل المجاني》", "《تعطيل المجاني》"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS:
    return
  global off
  if message.text == "《تفعيل المجاني》":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح .")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح .")
@Client.on_message(filters.command("《صنع بوت》", "") & filters.private)
async def makedzombie(client, message):
  if not message.from_user.username in DEVS:
    for x in Bots:
        if x[1] == message.from_user.id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل . ")
  try:
    ask = await client.ask(message.chat.id, "ارسل توكن البوت", timeout=300)
  except:
      return
  TOKEN = ask.text
  try:
    ask = await client.ask(message.chat.id, "ارسل كود الجلسه", timeout=300)
  except:
      return
  SESSION = ask.text
  Dev = message.from_user.id
  if message.from_user.username in DEVS:
    try:
       ask = await client.ask(message.chat.id, "ارسل ايدي المطور", timeout=300)
    except:
      return
    try:
      Dev = int(ask.text)
    except:
      return await message.reply_text("قم بارسال الايدي بشكل صحيح")#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
  bot = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True, plugins=dict(root="source"))
  user = Client(":ahmed:", api_id=API_ID, api_hash=API_HASH, session_string=str(SESSION))
  #try:
  await bot.start()
  username = await bot.get_me()
  username = username.username
    #await bot.stop()
  await user.start()
    #await user.stop()
  #except Exception as e:
    #print(e)
    #return await message.reply_text("تاكد من التوكن أو الجلسة")
  id = message.from_user.username
  for x in Bots:
        if x[0] == id:
          return await message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
  os.system(f"cp -a source users/{id}")
  env = open(f"users/{id}/.env", "w+", encoding="utf-8")
  x = f'BOT_TOKEN = {TOKEN}\nSTRING_SESSION = {SESSION}\nOWNER_ID = {Dev}'
  env.write(x)
  env.close()
  os.system(f"cd users/{id} && screen -d -m -S {id} python3 -m AnonXMusic")
  oo = [id, Dev]
  Bots.append(oo)
  await message.reply_text("تم تنصيب بوتك بنجاح\n《قناه السورس》»  @UI_XB ❤❤️‍🔥")

@Client.on_message(filters.command("《حذف بوت》", "") & filters.private)
async def deletbotzombie(client, message):
   if not message.from_user.username in DEVS:
     for x in Bots:
         bot = x[0]
         if x[1] == message.from_user.id:       
           os.system(f"sudo rm -fr users/{bot}")
           os.system(f"screen -XS {bot} quit")
           Bots.remove(x)
           return await message.reply_text("تم حذف بوتك من الصانع .")
     return await message.reply_text("لم تقم بصنع بوتات")
   try:
      bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
   except:
      return
   bot = bot.text.replace("@", "")
   for x in Bots:
       if x[0] == bot:
          Bots.remove(x)
   os.system(f"sudo rm -fr users/{bot}")
   os.system(f"screen -XS {bot} quit")
   await message.reply_text("تم حذف البوت بنجاح")


@Client.on_message(filters.command("《البوتات المصنوعه》", ""))
async def botzombie(client, message):
  if not message.from_user.username in DEVS:
   return
  o = 0
  text = "قايمه البوتات\n"
  for x in Bots:
      o += 1
      text += f"{o}- @{x[0]}\n"
  if o == 0:
    return await message.reply_text("لا يوجد بوتات مصنوعه")
  await message.reply_text(text)
