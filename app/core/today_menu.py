from collections import defaultdict
from datetime import datetime, timedelta
from typing import Sequence

from app.core import UTMNBuilds, constants
from app.core.exceptions import UniversityNotHaveDinings
from app.entities import AllMenu, DiningMenuResponse, DiningRoom


class TodayMenu:
    def __init__(self) -> None:
        self._university_dinings = defaultdict(list)
        self._today_menu: AllMenu | None = None
        # - timdelta(days=1) mean menu on start is expire
        self._last_update: datetime = datetime.now() - timedelta(days=1)

        self._utmn_builds = UTMNBuilds()

    def update(self, new_menu: DiningMenuResponse) -> None:
        self._university_dinings.clear()
        self._today_menu = self._convert_menu(new_menu)
        self._last_update = datetime.now(tz=constants.TZ)

    def get_all_today_university(self) -> list[str]:
        return self._university_dinings

    def get_all_menu(self) -> AllMenu | None:
        return self._today_menu

    def get_dining_room(self, name: str) -> DiningRoom:
        return self._today_menu.dining_rooms.get(name)

    def get_all_dining_rooms(self) -> Sequence[str]:
        return self._today_menu.dining_rooms.keys()

    def get_university_dinings(self, university: str) -> list[str]:
        dining_rooms = self._university_dinings.get(university)
        if not dining_rooms:
            raise UniversityNotHaveDinings(f'Нету меню для {university}')
        return dining_rooms

    def is_expire(self) -> None:
        if self._today_menu is None:
            return True

        now = datetime.now(tz=constants.TZ)
        if self._last_update.day != now.day:
            self._today_menu = None
            return True
        return False

    def _convert_menu(self, menu: DiningMenuResponse) -> AllMenu:
        new_dining_rooms = {}
        for room in menu.dining_rooms:
            name, address = self._get_name_and_address(room.title)
            university = self._utmn_builds.get_utmn_build_by_address(address)
            self._university_dinings[university].append(name)
            new_dining_rooms[name] = DiningRoom(
                name=name,
                university=university,
                address=address,
                menu=room.menu,
            )
        return AllMenu(date=menu.dining_rooms[0].date, dining_rooms=new_dining_rooms)

    @staticmethod
    def _get_name_and_address(dining_room_title: str) -> tuple[str, str]:
        reversed_title = dining_room_title[::-1]
        open_bracket = reversed_title.find('(')

        name = reversed_title[: open_bracket + 1 : -1]
        address = reversed_title[open_bracket - 1 : 0 : -1]
        return name, address
