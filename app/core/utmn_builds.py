from dataclasses import dataclass

from app.core.exceptions import AddressNotMatched


@dataclass
class UniverityBuild:
    name: str
    address: str
    number: str


class UTMNBuilds:
    def __init__(self) -> None:
        self.universitys: list[UniverityBuild] = [
            UniverityBuild('ИФиЖ', 'республика', '9'),
            UniverityBuild('ИнЗем', 'осипенко', '2'),
            UniverityBuild('ФЭИ', 'ленина', '16'),
            UniverityBuild('ИМиКН', 'перекопская', '15'),
            UniverityBuild('ИнБио', 'пирогова', '3'),
            UniverityBuild('ИФК', 'пржевальского', '37'),
            UniverityBuild('ИГиП', 'ленина', '38'),
            UniverityBuild('СоцГУМ', 'ленина', '23'),
            UniverityBuild('ИПип', 'проезд 9 мая', '5'),
            UniverityBuild('X-BIO', 'володарского', '6'),
            UniverityBuild('ШПИ', '8 марта', '2'),
        ]

    def get_utmn_build_by_address(self, full_address: str) -> str:  # noqa: PLR0911
        full_address = full_address.lower()
        for univeristy_build in self.universitys:
            if self._address_includes_build(full_address, univeristy_build):
                return univeristy_build.name
        raise AddressNotMatched(f'Не найдено строения по адресу {full_address}')

    def _address_includes_build(self, full_address: str, build: UniverityBuild) -> bool:
        if build.address in full_address and build.number in full_address:
            return True
        return False
