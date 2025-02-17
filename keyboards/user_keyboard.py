from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_menu_keyboard():
    kb = [[KeyboardButton(text="/start"), KeyboardButton(text="/help")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def get_inline_keyboard():
    # список кнопок
    button_list: list = [2, 1]

    # сами кнопки
    builder = InlineKeyboardBuilder()
    builder.button(text="Первая кнопка", callback_data=f"FirstAction")
    builder.button(text="Вторая кнопка", callback_data=f"SecondAction")
    builder.button(text="Назад", callback_data="MainMenu")

    # формируем расположение кнопок
    builder.adjust(*button_list)

    return builder.as_markup()
