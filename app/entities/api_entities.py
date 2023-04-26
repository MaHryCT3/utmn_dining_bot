from datetime import datetime

from pydantic import BaseModel, Field, validator


class BaseResponse(BaseModel):
    status: int
    success: bool


class MenuItem(BaseModel):
    id: str
    title: str
    price: float


class BaseDiningRoom(BaseModel):
    title: str
    date: datetime
    menu: dict[str, list[MenuItem]]

    @validator('date', pre=True)
    def get_date_object(cls, value: str) -> datetime:
        return datetime.strptime(value, '%d.%m.%Y')


class DiningMenuResponse(BaseModel):
    total: int
    dining_rooms: list[BaseDiningRoom] = Field(..., alias='diningroom')


class DiningMenuJson(BaseResponse):
    response: DiningMenuResponse | None = None
