def parse_where_clause(where_str):
    """Функция выполняет парсинг строки условия WHERE в словарь"""
    where = {}
    parts = where_str.split(' and ')
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()


            # Удаление кавычек
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            elif value.isdigit():
                value = int(value)
            elif value.lower() in ['true', 'false']:
                value = value.lower() == 'true'

            where[key] = value
   
    return where


def parse_set_clause(set_str):
    """Функция выполняет парсинг значений SET в словарь"""
    set_values = {}
    parts = set_str.split(',')
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()

            # Удаляем кавычки
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            elif value.isdigit():
                value = int(value)
            elif value.lower() in ['true', 'false']:
                value = value.lower() == 'true'

            set_values[key] = value
    return set_values


def parse_values(values_str):
    """Функция выполняет парсинг строки значений VALUES в список значений"""
    
    vals = []
    # Удаляем скобки
    if values_str.startswith('(') and values_str.endswith(')'):
        values_str = values_str[1:-1]

    parts = values_str.split(',')
    for part in parts:
        value = part.strip()

        # Удаляем кавычки
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        elif value.isdigit():
            value = int(value)
        elif value.lower() in ['true', 'false']:
            value = value.lower() == 'true'

        vals.append(value)
    return vals
