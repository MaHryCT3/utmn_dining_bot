from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.core.exceptions import AddressNotMatched, UniversityNotHaveDinings
from app.core.notify_error import addres_not_matched, no_university_dinings, unexpected_error
from app.services.dining_api import DiningAPI


class MenuMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.dining_api = DiningAPI()

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        data['dining_api'] = self.dining_api
        try:
            return await handler(event, data)
        except UniversityNotHaveDinings as ex:
            return await no_university_dinings(event, ex)
        except AddressNotMatched as ex:
            return await addres_not_matched(event, ex)
        except Exception as ex:
            return await unexpected_error(event, ex)
