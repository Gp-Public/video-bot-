# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**


🛠 **[ 𝙋𝙍𝘼𝙑𝙄𝙉𝘾𝙔🕴️] [https://t.me/Gplove_Rp) **if you have any problem contact**

❔ **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 💃𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋💃 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎", callback_data="cbcmds"),
                    InlineKeyboardButton("⭕𝙒𝙉𝙀𝙍", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "💫 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇 𝙂𝙍𝙊𝙐𝙋", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "💫 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🐾𝙋𝙍𝘼𝙑𝙄𝙉𝘾𝙔🕴️", url="https://t.me/Gplove_Rp"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **turn on the video chat first before start to play video.**
5.) **all the command list you can see on » 📚 Commands button, find it on start home, tap the » Go Back button below.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 Here is the Commands list:

» /play - play music on voice chat
» /stream - enter the radio link
» /vplay - play video on video chat
» /vstream - for m3u8/live link
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /queue - show you the queue list (admin only)
» /pause - pause the stream (admin only)
» /resume - resume the stream (admin only)
» /skip - switch to next stream (admin only)
» /stop - stop the streaming (admin only)
» /userbotjoin - invite the userbot to join chat (admin only)
» /userbotleave - order userbot to leave from group (admin only)
» /reload - update the admin list (admin only)
» /rmw - clean raw files (sudo only)
» /rmd - clean downloaded files (sudo only)
» /leaveall - order userbot leave from all group (sudo only)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
