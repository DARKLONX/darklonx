# COPYRIGHT (C) 2021 BY DARKLONX22 AND PROBOYX, ALAIN

"""
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
                 MADE BY DARKLONX AND PROBOY X
                   DISIGNED BY ALAIN_CHAMPION
                   CREDITS #TEAMDARKLONX 
                PLEASE DON'T REMOVE THIS LINES
"""

from telethon import events, Button, custom
import re, os
from DARKLONX import PHOTO, xbot, BOT, VERSION
from userbot import bot
@xbot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  DARKLONX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  DARKLONX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  DARKLONX += f"{BOT} VERSION : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  DARKLONX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  DARKLONX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  DARKLONX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  DARKLONX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/DARKLONXOP/DARKLONX-BOT")]]
  BUTTON += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="DARKLONX")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=DARKLONX,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"DARKLONX")))
async def callback_query_handler(event):
# inline by DARKLONX22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-DARKLONX", "https://github.com/DARKLONXOP/DARKLONX-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-DARKLONX", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/DARKLONX-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/DARKLONXBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/DARKLONX_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by DARKLONX22 and PROBOY22 🔥
  DARKLONX = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  DARKLONX += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  DARKLONX += f"{BOT} OS : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  DARKLONX += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  DARKLONX += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  DARKLONX += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  DARKLONX += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/DARKLONXOP/DARKLONX-BOT")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="DARKLONX")]]
  await event.edit(text=DARKLONX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await xbot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/DARKLONXOP/DARKLONX-BOT")]])
