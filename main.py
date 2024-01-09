from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, InputFile, WebAppInfo
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
API_TOKEN = '6751725166:AAFBWZA2H-ibCXC0gDffZm1Y-kppL0xKk1s'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url = 'https://fikfap.com/')))
    await message.answer('hello', reply_markup=markup)
if __name__ == '__main__':
    storage = MemoryStorage()
    # Подключаем MemoryStorage к боту
    dp.storage = storage
    executor.start_polling(dp, skip_updates=True)
