"""
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@DARKLONX22)))))))))))))))))))))))))))
           MADE BY @DARKLONX22 dont kang this plugin
         CREDITS = @DARKLONX22 @PROBOYX @alain_champion
     Special thanks @alain_champion for this modified version
            if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime, CMD_HELP
from . import legend
from DARKLONX import BOT, PHOTO, VERSION
from userbot.utils import admin_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARKLONX BOY"

global kanger #kanger aaya bhaago bc
        
#make by DARKLONX X bht mehnat lag gayi yrr but banhi gaya 😅           
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   global PHOTO
   if PHOTO:
     tag = borg.uid
     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "💟 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 💟\n\n"
     ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 1.21\n\n"
     ALIVE_MESSAGE += f"🔶 𝙻𝙴𝙶𝙴𝙽𝙳 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔶 :   {VERSION}\n\n"
     ALIVE_MESSAGE += f"🔷 𝚄𝙿𝚃𝙸𝙼𝙴 🔷 : {uptm}\n\n"
     ALIVE_MESSAGE += f"💠 𝙼𝚈 𝙱𝙾𝚂𝚂 💠: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "🔰 𝙶𝚁𝙾𝚄𝙿 🔰 : [SUPPORT](https://t.me/DARKLONX_USERBOT_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"💠 [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2FDARKLONX-ROBOT) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/legendxop/legend-bot)  💠\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   elif PHOTO == None:
     PHOTO = "https://telegra.ph/file/0ed5f920e8a5e9a7b0029.jpg"
     tag = borg.uid
     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "💟 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 💟\n\n"
     ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 1.20\n\n"
     ALIVE_MESSAGE += f"🔶 𝙻𝙴𝙶𝙴𝙽𝙳 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔶 :   {VERSION}\n\n"
     ALIVE_MESSAGE += f"🔷 𝚄𝙿𝚃𝙸𝙼𝙴 🔷 : {uptm}\n\n"
     ALIVE_MESSAGE += f"💠 𝙼𝚈 𝙱𝙾𝚂𝚂 💠: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "🔰 𝙶𝚁𝙾𝚄𝙿 🔰 : [SUPPORT](https://t.me/DARKLONX_USERBOT_SUPPORT)\n\n"
     ALIVE_MESSAGE += f"💠 [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FDARKLONXOP%2FDARKLONX-ROBOT) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/legendxop/legend-bot)  💠\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   else:
     await awake.edit("please add right value on ALIVE_PHOTTO var")

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
