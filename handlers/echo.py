from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message()
async def echo_handler(message: Message):
    await message.answer(f"Вы написали: {message.text}")
