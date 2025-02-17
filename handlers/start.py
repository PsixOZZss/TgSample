from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject

router = Router()


@router.message(CommandStart(deep_link=True))
async def cmd_start(message: Message, command: CommandObject):
    args = command.args
    await message.answer(
        f"Привет! Это бот. Аргумент в ссылке: {args}. Напишите /help для справки."
    )


@router.message(CommandStart(deep_link=False))
async def cmd_start(message: Message):
    await message.answer("Привет! Это бот. Напишите /help для справки.")
