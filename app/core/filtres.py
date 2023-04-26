from aiogram.filters import Filter
from aiogram.types import Message

from app.core import constants


class DiningRoomFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        for dining_room_name in constants.DINING_ROOM_NAMES:
            if dining_room_name.lower() in message.text.lower():
                return True
        return False


class UniversityNameFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        if message.text in constants.UNVERSITY_NAMES:
            return True
        return False
