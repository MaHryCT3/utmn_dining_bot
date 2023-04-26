from aiogram import F, Router, filters, types

from app.core import DiningRoomFilter, UniversityNameFilter
from app.core.middlewares import MenuMiddleware
from app.handlers._keyboard import create_dining_room_keyboard, create_university_build_keyboard
from app.services.dining_api import DiningAPI
from app.views import MenuView

router = Router(name='Menu')
router.message.middleware(MenuMiddleware())


@router.message(filters.CommandStart())
async def start(message: types.Message, dining_api: DiningAPI) -> None:
    await message.answer('Привет! Это бот, который выводит актуальное меню столовой и все. 😌')
    await _send_universities(message, dining_api)


@router.message(F.text.in_(['Вузы', '/start']))
async def universitys_menu(message: types.Message, dining_api: DiningAPI) -> None:
    await _send_universities(message, dining_api)


@router.message(UniversityNameFilter())
async def university_dining_rooms(message: types.Message, dining_api: DiningAPI) -> None:
    dinings = await dining_api.get_university_dining_rooms(message.text)
    if len(dinings) == 1:
        await _send_dining_room_menu(message, dinings[0], dining_api)
    else:
        keyboard = create_dining_room_keyboard(dinings)
        await message.answer('Выбери столовую:', reply_markup=keyboard)


@router.message(DiningRoomFilter())
async def dining_menu(message: types.Message, dining_api: DiningAPI) -> None:
    await _send_dining_room_menu(message, message.text, dining_api)


@router.message(filters.Text(contains='test'))
async def today_dining_menu(message: types.Message, dining_api: DiningAPI) -> None:
    menu = await dining_api.get_today_menu()
    await message.answer(str(menu.dining_rooms.keys()))


async def _send_universities(message: types.Message, dining_api: DiningAPI) -> None:
    keyboard = await _get_university_keyboard(dining_api)
    await message.answer('Вузы:', reply_markup=keyboard)


async def _send_dining_room_menu(message: types.Message, dining_room: str, dining_api: DiningAPI) -> None:
    menu = await dining_api.get_dining_room(dining_room)
    keyboard = await _get_university_keyboard(dining_api)
    await message.answer(MenuView(menu).render(), reply_markup=keyboard)


async def _get_university_keyboard(dining_api: DiningAPI) -> types.ReplyKeyboardMarkup:
    university = await dining_api.get_all_university_with_dining_menu()
    return create_university_build_keyboard(university)
