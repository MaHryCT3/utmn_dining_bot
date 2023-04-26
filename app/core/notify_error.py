from aiogram import types


async def no_university_dinings(message: types.Message, error: Exception) -> None:
    await message.answer(f'Произошла ошибка! Попробуйте написать "Вузы" и повторите попытку. Текст ошибки: {error}')


async def addres_not_matched(message: types.Message, error: Exception) -> None:
    await message.answer(f'Произошла какая-то ошибка с адрессами. Текст ошибки: {error}')


async def unexpected_error(message: types.Message, error: Exception) -> None:
    await message.answer(f'Произошла непредвиденная ошибка. Текст ошибки: {error}')
