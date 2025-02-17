from aiogram.filters import BaseFilter
from aiogram.types import Message

class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        # Здесь можно проверить, является ли пользователь администратором
        return message.from_user.id in [123456789]  # Список ID админов