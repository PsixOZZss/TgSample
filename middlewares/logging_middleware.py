from aiogram import BaseMiddleware
from aiogram.types import Update


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data):
        print(f"Получено событие: {event}")
        return await handler(event, data)
