# Ported by LEGENDX
# Original By 
# @THE_B_LACK_HAT
# @danish_00
# Card Generator
##############################
from faker import Faker as dc
from LEGENDX.utils import admin_cmd as hehe
from LEGENDX import bot as cobra
@cobra.on(hehe("cc"))
async def _cobra(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    danish = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{danish}`")
