from app.entities import DiningRoom
from app.views import ABCView


class MenuView(ABCView):
    def __init__(self, dining_room: DiningRoom) -> None:
        self.dining_room = dining_room

    def render(self) -> str:
        menu = ''
        for category, menu_items in self.dining_room.menu.items():
            menu += f'<b><u>{category}</u></b>\n'
            for item in menu_items:
                menu += f'<b>{item.title}</b>: <i>{item.price} руб</i>.\n'
        return menu
