import os

from aiogram import Bot, Dispatcher
from loguru import logger

from app.handlers import routers


async def start_polling() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(*routers)
    bot = Bot(os.getenv('TELEGRAM_TOKEN'), parse_mode='HTML')
    logger.info('Bot started')
    dp['123'] = 123
    await dp.start_polling(bot)
