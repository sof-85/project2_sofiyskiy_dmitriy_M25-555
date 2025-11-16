# Файл реализует логику работы с таблицей и данными
from utils import load_metadata, save_metadata

def create_table(metadata, table_name, columns):
    #from utils import load_metadata, save_metadata
    #print(metadata)
    #print(table_name)
    #print(columns)
    if (table_name not in metadata.keys()):
        '''Функция создает новую таблицу'''
        
        #if (columns[0] != "ID:int"):
        columns.insert(0,"ID:int")
        new_columns = columns
        print(new_columns)
        type_sym = ':'
        if type_sym in table_name:
            print("Ошибка в имени таблицы")
            return
        for ncol in range (0,len(new_columns)):
            if new_columns[ncol].count (type_sym) == 1:
                pass
            else:
                print(f'Ошибка:Не могу создать столбец {new_columns[ncol]} - неправильный синтаксис команды')
                return
            
              
        split_col = map(lambda col: tuple(col.split(':')),new_columns)
        #for scol in range (0,len(split_col)-1):
         #   if scol in ['int','bool','string']:
          #      pass
        print (split_col)
        col_dict=dict(split_col)
        print(col_dict)
        new_table = {table_name:col_dict}
        print (set(col_dict.values()))
        if (set(col_dict.values()).issubset({'int','bool','string'})):
            metadata.update(new_table)
            save_metadata("db_meta.json", metadata)
            print (f"Таблица {table_name} успешно создана со столбцами {col_dict}")
        else:
            print ("Ошибка. Проверьте правильность задания типов данных")
    else:
        print(f"Ошибка: Таблица {table_name} уже существует")     
  
    return metadata

def drop_table(metadata, table_name):
    '''Функция выполняет удаление таблицы по заданному имени'''
    if (table_name in metadata.keys()):
        metadata.pop(table_name,None)
        new_metadata = metadata
        save_metadata("db_meta.json", new_metadata)
        print(f"Таблица {table_name} успешно удалена")
    else:
        print(f"Ошибка: Таблица {table_name} не существует")     

def list_tables (metadata):
    '''Функция выводит список таблиц отсортированных по алфовиту'''
    print(sorted(metadata.keys()))
    for key in sorted(metadata.keys()):
        print (f'- {key}')



#current_data = save_metadata('db_meta.json')


#def check_data()
'''
data =  {"users": [{"id":1,"username": "Ann","is_active": True}]}
data1 =  {"users": [{"id":2,"username": "Jane","is_active": True}]}
save_metadata("db_meta",data)
save_metadata("db_meta",data1)

data = {'user':
                {"id":"int",
                 "name":"string",
                 "isactive":"bool"}
        }
metadata = load_metadata("db_meta.json")
print ('до ',metadata)
create_table(metadata,"user2",["name:string","isactive:bool"])


#drop_table(metadata,"user")
print ('после ',metadata)

metadata = load_metadata("db_meta.json")
create_table(metadata,"user0",["name:string","isactive:bool"])
create_table(metadata,"user1",["name:string","isactive:bool"])
list_tables(metadata)

metadata = load_metadata("db_meta.json")
create_table(metadata,"user3",["ID:int","name:string","name:string","isactive:bool","sdf:int"])
#drop_table(metadata,"user3")'''