#Константы программы

META_FILE = "db_meta.json"
TABLE_DATA_PATH = "src/primitive_db/data/"
TABLE_DATA_TYPE = ".json"


VALID_TYPES = {'int', 'str', 'bool'}
DEFAULT_COLUMNS = ['ID:int']

ERROR_FILE_NOT_FOUND = "Ошибка: Файл данных не найден."
ERROR_TABLE_NOT_FOUND = "Ошибка: Таблица или столбец {} не найден."
ERROR_VALIDATION = "Ошибка валидации: {}"
ERROR_UNEXPECTED = "Произошла непредвиденная ошибка: {}"

CONFIRM_PROMPT = 'Вы уверены, что хотите выполнить "{}"? [y/n]: '
CANCEL_MESSAGE = "Операция отменена"

CACHE_USED = "Используется кэшированный результат для ключа: {}"
CACHE_SAVED = "Результат кэширован для ключа: {}"

TIME_MESSAGE = "Операция {} выполнена за {:.3f} секунд"