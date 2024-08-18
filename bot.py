from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from config import bot_token
from main import main

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

answ = dict()

hello_text = """Hello, I'm a bot that will help you find out the weather in any city in the world. Just write the name of the city and I will tell you what the weather is like there :)"""

@dp.message_handler(commands = ["start", "help"])
async def start(message : types.Message):
    await message.answer(hello_text)

@dp.message_handler()
async def handle_message(message: Message):
    city = message.text
    
    result = main(city)
    await message.reply(result)

executor.start_polling(dp, skip_updates=True)