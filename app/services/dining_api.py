from typing import Sequence

from app.core.today_menu import TodayMenu
from app.entities import AllMenu, DiningMenuJson, DiningMenuResponse, DiningRoom
from app.services import HTTPClient


class DiningAPI:
    def __init__(self):
        self._http_client = HTTPClient('https://nova.utmn.ru/api/v1')
        self._today_menu: TodayMenu = TodayMenu()

    async def get_all_university_with_dining_menu(self) -> Sequence[str]:
        await self._updates_menus()
        return self._today_menu.get_all_today_university()

    async def get_university_dining_rooms(self, university: str) -> Sequence[str]:
        await self._updates_menus()
        return self._today_menu.get_university_dinings(university)

    async def get_today_menu(self) -> AllMenu | None:
        await self._updates_menus()
        return self._today_menu.get_all_menu()

    async def get_dining_room(self, name: str) -> DiningRoom | None:
        await self._updates_menus()
        return self._today_menu.get_dining_room(name)

    async def get_all_dining_rooms(self) -> Sequence[str]:
        await self._updates_menus()
        return self._today_menu.get_all_dining_rooms()

    async def _get_menu(self) -> DiningMenuResponse:
        response = await self._http_client.request_get('/diningroom')
        menu = DiningMenuJson(**response.json())
        return menu.response

    async def _updates_menus(self) -> None:
        if self._today_menu.is_expire():
            self._today_menu.update(await self._get_menu())

    # We have 3 different situation
    # The first when menu is expire, it means day end
    #   Need set today menu to None
    # The second when menu now is None, it means bot only start work or dining menu on update
    #   Need check menu for current day and update if we have this
    # The third when it's all good
    #   Just return today menu
