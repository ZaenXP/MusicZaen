from pyrogram import filters
from pyrogram.types import Message

from config import Music, MUSIC_BOT_NAME, adminlist
from strings import get_command
from Music import app
from Music.core.call import Music
from Music.misc import db
from Music.utils.database import get_authuser_names
from Music.utils.decorators import language
from Music.utils.decorators.admins import AdminActual
from Music.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "Failed to reload admincache. Make sure Bot is admin in your chat."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"Please Wait.. Restarting {MUSIC_BOT_NAME} for your chat.."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Music.stop_stream(message.chat.id)
    except:
        pass
    return await mystic.edit_text(
        "Successfully restarted. Try playing now.."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return
