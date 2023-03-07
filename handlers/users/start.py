from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from insta import insta
from loader import dp, bot, baza



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        ism = message.from_user.first_name
        id = message.from_user.id
        user_name = message.from_user.username
        baza.user_qoshish(first_name=ism, user_name=user_name, tg_id=id)
    except Exception:
        pass
    await message.answer(f"Assalomu Alaykum!, {message.from_user.full_name}!")
    await message.answer(text='Havolani yuboring')
@dp.message_handler(Text(startswith='https://www.instagram.com/tv'))
async def bot_start(message: types.Message):
    natija = insta(message.text)
    await message.answer(text='⏳')
    await bot.send_video(chat_id=message.from_user.id, video=natija['video'], caption='Dasturchi💻: https://t.me/Pythonchi_UZB')
@dp.message_handler(Text(startswith='https://www.instagram.com/p'))
async def bot_start(message: types.Message):
    natija = insta(message.text)
    await message.answer(text='⏳')
    await bot.send_photo(chat_id=message.from_user.id, photo=natija['video'], caption='Dasturchi💻: https://t.me/Pythonchi_UZB')
@dp.message_handler(Text(startswith='https://instagram.com/stories/'))
async def bot_start(message: types.Message):
    natija = insta(message.text)
    await message.answer(text='⏳')
    await message.answer_video(video=natija['video'][0], caption='Dasturchi💻: https://t.me/Pythonchi_UZB')
@dp.message_handler(Text(startswith='https://www.instagram.com/reel/'))
async def bot_start(message: types.Message):
    natija = insta(message.text)
    await message.answer(text='⏳')
    await bot.send_video(chat_id=message.from_user.id, video=natija['video'], caption='Dasturchi💻: https://t.me/Pythonchi_UZB')

