
import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonXMusic import app
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

iddof = []
@app.on_message(
    filters.command(["قفل الاذكار","تعطيل الاذكار"],"")
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = (6275847466)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\n الاذكار مقفلها من قبل**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر الاذكار بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")

@app.on_message(
    filters. command(["فتح الاذكار","تفعيل الاذكار"],"")
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (6218149232)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif message.from_user.id in haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 
    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention}\n الاذكار مقفلها من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل الاذكار بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 



@app.on_message(
    filters.command(["اذكار"],"")
    
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = [



"اااللهم يا من رويت الأرض مطرا أمطر قلوبنا فرحا 🍂 ",
"اا‏اللَّهُـمَّ لَڪَ الحَمْـدُ مِنْ قَـا؏ِ الفُـؤَادِ إلىٰ ؏َـرشِڪَ المُقـدَّس حَمْـدَاً يُوَافِي نِـ؏ـمَڪ 💙🌸",
"﴿وَاذْكُرِ اسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًا﴾🌿✨",
"﴿وَمَن يَتَّقِ اللهَ يُكَفِّرْ عَنْهُ سَيِّئَاتِهِ وَيُعْظِمْ لَهُ أَجْرًا﴾",
"«سُبْحَانَ اللهِ ، وَالحَمْدُ للهِ ، وَلَا إلَهَ إلَّا اللهُ ، وَاللهُ أكْبَرُ ، وَلَا حَوْلَ وَلَا قُوَّةَ إلَّا بِاللهِ»🍃",
"وذُنُوبًا شوَّهتْ طُهْرَ قُلوبِنا؛ اغفِرها يا ربّ واعفُ عنَّا ❤️",
"«اللَّهُمَّ اتِ نُفُوسَنَا تَقْوَاهَا ، وَزَكِّهَا أنْتَ خَيْرُ مَنْ زَكَّاهَا ، أنْتَ وَلِيُّهَا وَمَوْلَاهَا»🌹",
"۝‏﷽إن اللَّه وملائكته يُصلُّون على النبي ياأيُّها الذين امنوا صلُّوا عليه وسلِّموا تسليما۝",
"فُسِبًحً بًحًمًدٍ ربًکْ وٌکْنِ مًنِ الَسِاجّدٍيَنِ 🌿✨",
"اأقُمً الَصّلَاةّ لَدٍلَوٌکْ الَشُمًسِ إلَيَ غُسِقُ الَلَيَلَ🥀🌺",
"نِسِتٌغُفُرکْ ربًيَ حًيَتٌ تٌلَهّيَنِا الَدٍنِيَا عٌنِ ذِکْرکْ🥺😢",
"وٌمًنِ أعٌرض عٌنِ ذِکْريَ فُإنِ لَهّ مًعٌيَشُةّ ضنِکْا 😢",
"وٌقُرأنِ الَفُجّر إنِ قُرانِ الَفُجّر کْانِ مًشُهّوٌدٍا🎀🌲",
"اأّذّأّ أّلَدِنِيِّأّ نَِّستّګوِ أّصٌلَګوِ زِّوِروِ أّلَمَقِأّبِر💔",
"حًتٌيَ لَوٌ لَمًتٌتٌقُنِ الَخِفُظُ فُمًصّاحًبًتٌ لَلَقُرانِ تٌجّعٌلَکْ مًنِ اهّلَ الَلَهّ وٌخِاصّتٌهّ❤🌱",
"وٌإذِا رضيَتٌ وٌصّبًرتٌ فُهّوٌ إرتٌقُاء وٌنِعٌمًةّ✨??",
"«ربً اجّعٌلَنِيَ مًقُيَمً الَصّلَاةّ وٌمًنِ ذِريَتٌيَ ربًنِا وٌتٌقُبًلَ دٍعٌاء 🤲",
"ااعٌلَمً انِ رحًلَةّ صّبًرکْ لَهّا نِهّايَهّ عٌظُيَمًهّ مًحًمًلَهّ بًجّوٌائزٍ ربًانِيَهّ مًدٍهّشُهّ🌚☺️",
"اإيَاکْ وٌدٍعٌوٌةّ الَمًظُلَوٌمً فُ إنِهّا تٌصّعٌدٍ الَيَ الَلَهّ کْأنِهّا شُرارهّ مًنِ نِار 🔥🥺",
"االَلَهّمً انِقُذِ صّدٍوٌرنِا مًنِ هّيَمًنِهّ الَقُلَقُ وٌصّبً عٌلَيَهّا فُيَضا مًنِ الَطِمًأنِيَنِهّ✨🌺",
"يَابًنِيَ إنِ صّلَاح الَحًيَاةّ فُ أتٌجّاهّ الَقُبًلَهّ 🥀🌿",
"الَلَهّمً ردٍنِا إلَيَکْ ردٍا جّمًيَلَا💔🥺",

" ﴿وَكَفَىٰ بِاللَّهِ وَكِيلًا﴾.", 
"‏﴿فَرِحِينَ بِمَا آتَاهُمُ اللَّهُ مِنْ فَضْلِهِ﴾", 
" أَيْنَمَا تَكُونُوا يُدْرِككُّمُ الْمَوْتُ .", 
"‏﴿ رَبَّنَا إِنَّكَ تَعْلَمُ مَا نُخْفِي وَمَا نُعْلِنُ ﴾", 
" ‏﴿ لا تَخَف وَلا تَحزَن إِنّا مُنَجّوكَ ﴾ .", 
"‏اللهُم و إن ضاق صدري فلا غير لُطفك يشرحه", 
" أَفَلَا يَتُوبُونَ إِلَى اللَّهِ وَيَسْتَغْفِرُونَهُ.", 
"‏﴿ رَبَّنَا إِنَّكَ تَعْلَمُ مَا نُخْفِي وَمَا نُعْلِنُ ﴾", 
" وَقالَ رَبُّكُمُ ادعوني أَستجِب لَكُم", 
"قُلِ اللَّهُ يُنَجّيكُم مِنها وَمِن كُلِّ كَربٍ .", 
" وَاصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا .", 
"وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ .", 
]

    ik = random.choice(i)
    await message.reply_text(f"اذكار اليوم ❤️\n│ \n└ʙʏ: {ik}")
