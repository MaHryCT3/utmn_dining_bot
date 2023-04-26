from dataclasses import dataclass
from datetime import datetime

from app.entities.api_entities import MenuItem


@dataclass
class DiningRoom:
    university: str
    name: str
    address: str
    menu: dict[str, list[MenuItem]]


@dataclass
class AllMenu:
    date: datetime
    dining_rooms: dict[str, DiningRoom]
