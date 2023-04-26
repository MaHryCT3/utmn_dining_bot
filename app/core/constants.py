from datetime import timedelta, timezone

UNVERSITY_NAMES = ['ИФиЖ', 'ИнЗем', 'ФЭИ', 'ИМиКН', 'ИнБио', 'ИФК', 'ИГиП', 'СоцГУМ', 'ИПип', 'X-BIO', 'ШПИ']

DINING_ROOM_NAMES = ['Столовая', 'Кафе', 'Буфет', 'Кофейня']


menu_start = (9, 30)


_offset = timedelta(hours=5)
TZ = timezone(offset=_offset, name='Тюмень')
