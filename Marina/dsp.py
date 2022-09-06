from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from cfg import TOKEN

bot = Bot(token=TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)
