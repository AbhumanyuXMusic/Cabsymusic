
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ง๐๐ฒ ๐ฌ ๐๐ฎ๐ฌ๐ข๐'๐ ๐งโโ๏ธ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ \n๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ \n๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐ค \nโญ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ [สแดแดแด๊ฑ แดแดษดแดส](https://t.me/candy_626)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โฐ๐ข๐๐ป๐ฒ๐ฟ๐ฌโฑ", url="https://t.me/candy_626")
                  ],[
                    InlineKeyboardButton(
                        "โฐ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐๐โฑ", url="https://t.me/AlishaSupport"
                    ),
                    InlineKeyboardButton(
                        "โฐ๐๐ฟ๐ผ๐๐ฝ๐ฉโฑ", url="https://t.me/Shayri_Music_Lovers"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐ๐๐๐๐ซ๐๐ญ๐ข๐จ๐ง๐ฅโฑ", url="https://t.me/Venomofficialfed" 
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Candy") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**๐๐๐ง๐๐ฒ ๐ฌ ๐๐ฎ๐ฌ๐ข๐'๐ ๐๐ฌ ๐๐ง๐ฅ๐ข๐ง๐ ๐งโโ๏ธ\n๐ ๐๐๐ง๐๐ฒ_๐๐ฉ ๐ฅ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐โค๏ธ", url="https://t.me/Shayri_Music_Lovers")
                ]
            ]
        )
   )
