from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_university_build_keyboard(university: list[str]) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for univer in university:
        builder.button(text=univer)
    builder.adjust(_find_greater_delimeter(len(university)))
    return builder.as_markup(resize_keyboard=True)


def create_dining_room_keyboard(rooms: list[str]) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for room in rooms:
        builder.button(text=room)
    builder.button(text='Вузы')
    builder.adjust(len(rooms), 1)
    return builder.as_markup(resize_keyboard=True)


def _find_greater_delimeter(number: int) -> int:
    if number % 4 == 0:
        return 4
    if number % 3 == 0:
        return 3
    if number % 2 == 0:
        return 2
    return 2
