import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from Zaid.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC
HOME_TEXT = "🥇 **ههݪاެ حبيب** \n\n **اެناެ بَۅت بَمميࢪ࣪اެتَ متَعدَدةَ ݪتشغِيݪ اެݪاغاެنِي فَي اެݪمَجمَۅعاتَ 🥇.** \n\n**اެضغط عݪى ࢪ࣪ࢪ الاۅاެمࢪ لݪاستخداެم 🤍.**"
HELP_TEXT = """
  **- تابع الازرار في الاسفل ↓** 

\u2022 يمديك تشوف كل اوامر البوت عن طريق زر اوامر البوت .
"""



USER_TEXT = """
🤍 ** - تابع الاوامر في الاسفل ↓ :** 

\u2022 -› .شغل - بالرد على ملف صوتي او اسم أغنية
\u2022 -› .تخطي - لتخطي اغنية في التشغيل
\u2022 -› .كافي - لايقاف تشغيل جميع الاغاني
\u2022 -› .اضبط - لضبط صوت حساب المساعد
\u2022 -› .الانتضار - لرؤية قائمة الانتضار التشغيل
\u2022 -› .ابحثلي - لبحث عن فيديو من اليوتيوب
\u2022 -› .بحث - لتحميل اغنية من اليوتيوب
\u2022 -› .كتم - لكتم صوت المساعد 
\u2022 -› .بنك - لإضهار بنك البوت
\u2022 -› .انضم - لدعوة حساب المساعد

. شكراً لقرائتك الاوامر - أتمنى لك يوماً تعيساً 🦴.
"""

SPAM_TEXT = """
🤍 **طريقة التشغيل ، تابع في الاسفل ↓** 

\u2022 1-› أولا ، أضفني الى مجموعتك
\u2022 2-› بعد ذالك قم برفعي كمشرف واعطائي صلاحيات مثل باقي البشر.
\u2022 3-› بعد ذالك اكتب .تحديث بيانات البوت
\u2022 3-› اضف سيدي ومولاي في مجموعتك او اكتب .انضم لدعوة المساعد
\u2022 4-› اذ لم تستطيع اضافة المساعد او واجهت مشاكل تحدث مع رئيس الوزراء  .
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("اެݪمِطَۅࢪ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("اެݪاۅاެمࢪ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("طࢪيقة اެݪتشغيݪ", callback_data="spam"),
            ],            

            [
                InlineKeyboardButton("اެݪتاެݪي", callback_data="home"),
                InlineKeyboardButton("مِسِحِ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("🥇 اެضفني اެݪى مجمۅعتَك 🥇", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("طࢪيقة اެݪتشغيݪ", callback_data="spam"),
            ],
            
            [
                InlineKeyboardButton("اެݪاۅاެمࢪ", callback_data="help"),
                InlineKeyboardButton("🦎 اެݪمطَۅࢪ", url=f"https://t.me/{UPDATES_CHANNEL}")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("اެݪاۅاެمࢪ", callback_data="help"),
                InlineKeyboardButton("مِسِحِ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("اެݪتاެݪي", callback_data="help"),
                InlineKeyboardButton("مِسِحِ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton("اެݪتاެݪي", callback_data="help"),
                InlineKeyboardButton("مِسِحِ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton("طࢪيقة اެݪتشغيݪ", callback_data="help"),
                InlineKeyboardButton("مِسِحِ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons = [
            [
                InlineKeyboardButton("🥇 اެضفني اެݪى مجمۅعتَك 🥇", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("طࢪيقة اެݪتشغيݪ", callback_data="spam"),
            ],
            
            [
                InlineKeyboardButton("اެݪاۅاެمࢪ", callback_data="help"),
                InlineKeyboardButton("🦎 اެݪمطَۅࢪ", url=f"https://t.me/{UPDATES_CHANNEL}")
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
