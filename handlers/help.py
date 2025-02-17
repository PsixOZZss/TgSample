from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "/help")
async def cmd_help(message: Message):
    await message.answer("Список доступных команд:\n/start - начать\n/help - помощь")
