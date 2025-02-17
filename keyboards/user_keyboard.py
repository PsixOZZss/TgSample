from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_menu_keyboard():
    kb = [[KeyboardButton(text="/start"), KeyboardButton(text="/help")]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
