# Для вспомогательных функций (например, работа с файлами)

import json


def load_metadata():
    from .constants import META_FILE, TABLE_DATA_PATH
    """Загружает метаданные из файла"""
    try:
        with open(TABLE_DATA_PATH + META_FILE, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_metadata(metadata):
    """Сохраняет метаданные в файл"""
    from .constants import META_FILE, TABLE_DATA_PATH
    with open(TABLE_DATA_PATH + META_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def load_table_data(table_name):
    """Загружает данные таблицы из файла"""
    from .constants import TABLE_DATA_PATH
    filename = f"{TABLE_DATA_PATH}{table_name}.json"
    try:
        with open(filename, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_table_data(table_name, data):
    """Сохраняет данные таблицы в файл"""
    from .constants import TABLE_DATA_PATH
    filename = f"{TABLE_DATA_PATH}{table_name}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

