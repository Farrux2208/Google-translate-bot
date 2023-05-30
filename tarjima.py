from googletrans import Translator
from aiogram.dispatcher.filters import Text
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import lang_buttons


logging.basicConfig(level=logging.INFO)
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
tr = Translator()

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
	await message.reply("salom!!! \nso'z kiriting....")

@dp.message_handler()
async def echo(message: types.Message): 
	global msg
	msg = message.text
	markup = await lang_buttons()
	await message.answer("Tilni tanlang",reply_markup=markup)

@dp.callback_query_handler(Text(startswith='lang_'))
async def foo(call:types.CallbackQuery):
	index = call.data.index('_')
	lang = call.data[index+1:]
	

	tarjima = tr.translate(msg,dest=lang)
	await call.message.answer(tarjima.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)