from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import asyncio

from config import BOT_TOKEN
from handlers import start, help, echo
from middlewares.logging_middleware import LoggingMiddleware


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация middleware
    dp.update.outer_middleware(LoggingMiddleware())

    # Регистрация обработчиков
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
