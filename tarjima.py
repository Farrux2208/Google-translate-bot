from googletrans import Translator
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = "6102788608:AAH-XHcJtOKoNxjg00x-x9NgSug--N6oRO4"
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
	markup  = types.InlineKeyboardMarkup()
	knopka_1 = types.InlineKeyboardMarkup(text="uzbek",callback_data="uz")
	knopka_2 = types.InlineKeyboardMarkup(text="inglesh",callback_data="en")
	knopka_3 = types.InlineKeyboardMarkup(text="ruscha",callback_data="ru")
	knopka_4 = types.InlineKeyboardMarkup(text="tojikcha",callback_data="tg")
	knopka_5 = types.InlineKeyboardMarkup(text="qazoqcha",callback_data="kk")
	markup.add(knopka_1,knopka_2,knopka_3,knopka_4,knopka_5)
	await message.answer("Tilni tanlang",reply_markup=markup)

@dp.callback_query_handler(text="uz")
async def foo(call:types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="en")
async def foo(call:types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="ru")
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="tg")
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text="kk")
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)