# Для вспомогательных функций (например, работа с файлами)

def load_metadata(filepath):
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
    import json
 #   current_data = load_metadata(filepath)
 #   current_data.update(data)
    #print(data)   
    try:
        with open(filepath, 'w', encoding='utf-8') as db:
          json.dump(data, db, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        raise ValueError("База данных отсутствует")
    except json.JSONDecodeError:
        raise ValueError("База данных повреждена")

#data = { 'user':1,"name":"Alice","age":28 }
#save_metadata("db_meta.json",data)
#data_r = load_metadata("db_meta.json")
#print(data_r)

'''

data = {'user':
                {"id":"int",
                 "name":"string",
                 "isactive":"bool"}
 ,'user1':
                {"id":"int",
                 "name":"string",
                 "isactive":"bool"}
        }

db=save_metadata("db_meta.json", data)
#db=save_metadata("db_meta.json", data2)
db = load_metadata("db_meta.json")
print(db)
'''
