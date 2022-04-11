from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Music import app
from Music.config import MUST_JOIN


def subcribe(func):
    async def wrapper(_, message: Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        if not MUST_JOIN:  # Not compulsory
            return
        try:
            try:
                await app.get_chat_member(MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                if MUST_JOIN.isalpha():
                    link = "https://t.me/" + MUST_JOIN
                else:
                    chat_info = await app.get_chat(MUST_JOIN)
                    chat_info.invite_link
                try:
                    await message.reply(
                        f"**Hallo {rpk}. ᴍᴀ'ᴀꜰ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ʙᴇʀɢᴀʙᴜɴɢ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴏᴜᴘ ᴋᴀᴍɪ ꜱɪʟᴀʜᴋᴀɴ ᴊᴏɪɴ ᴅᴜʟᴜ ᴋᴀᴋ ᴀɢᴀʀ ʙɪꜱᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ɪɴɪ, ᴋᴀᴍɪ ᴍᴇʟᴀᴋᴜᴋᴀɴ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜɪɴᴅᴀʀɪ ʙᴇʀʟᴇʙɪʜᴀɴɴʏᴀ ᴘᴇᴍᴀᴋᴀɪᴀɴ ʙᴏᴛ ᴅᴀɴ ꜱᴇᴋᴀʟɪɢᴜꜱ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀʀᴀʜᴋᴀɴ ᴋᴀᴋᴀᴋ ʙᴀɢᴀɪᴍᴀɴᴀ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ ɪɴɪ, ᴋᴀᴋᴀᴋ ᴄᴜᴋᴜᴘ ʙᴀᴄᴀ ꜱᴀᴊᴀ ᴛᴜᴛᴏʀɪᴀʟ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴀᴛᴀᴜ ɢʀᴏᴜᴘ ᴋᴀᴍɪ. ꜱɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ.**",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Join Channel Bot", url=link)]]
                        ),
                    )
                    await message.stop_propagation()
                except ChatWriteForbidden:
                    pass
        except ChatAdminRequired:
            await message.reply(
                f"Saya bukan admin di chat MUST_JOIN chat : {MUST_JOIN} !"
            )
        return await func(_, message)

    return wrapper
