# Для вспомогательных функций (например, работа с файлами)

from constants import TABLE_DATA_PATH, TABLE_DATA_TYPE


def load_metadata(filepath):
    '''Функция читает метаданные из файла формата JSON'''
    import json
    data = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as db:
            current_data = json.load(db)
            if (current_data is None):
                return data
            else:
                return current_data
    except FileNotFoundError:
        return data
    except json.JSONDecodeError:
        return data
    
    
def save_metadata(filepath, data):
    '''Функция сохраняет метаданные в файл формата JSON'''
    import json
 
    try:
        with open(filepath, 'w', encoding='utf-8') as db:
          res = json.dump(data, db, indent=4, ensure_ascii=False)
          return res

    except FileNotFoundError:
        raise ValueError("База данных отсутствует")

    except json.JSONDecodeError:
        raise ValueError("База данных повреждена")
    
def load_table_data(table_name):
    '''Функция читает данные таблиц из каталога data из файла формата JSON'''
    import json
    from pathlib import Path
    data = []
    table_name = Path(TABLE_DATA_PATH + table_name + TABLE_DATA_TYPE)
    print(table_name) 
    
    try:
        with open(table_name, 'r', encoding='utf-8') as td:
            current_data = json.load(td)
            print(current_data)
            if (current_data is None):
                return data
            else:
                return current_data
    except FileNotFoundError:
        print ("Файл не найден")
        return data
    except json.JSONDecodeError:
        print("формат некорректен")
        return data
    
    
def save_table_data(table_name, data):
    '''Функция сохраняет метаданные в файл формата JSON'''
    import json
    from pathlib import Path
    table_name = Path(TABLE_DATA_PATH + table_name + TABLE_DATA_TYPE)
    
    try:
        with open(table_name, 'w', encoding='utf-8') as td:
          json.dump(data, td, indent=4, ensure_ascii=False)
        
    except FileNotFoundError:
        raise ValueError("База данных отсутствует")
    except json.JSONDecodeError:
        raise ValueError("База данных повреждена")

