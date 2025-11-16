META_FILE = "db_meta.json"


def welcome():
   import prompt
   #print('\n***')
   #print('<command> exit - выйти из программы')  
   #print('<command> help - справочная информация')
   command = prompt.string('>>>Введите команду ')
   return command
   
def print_help():
    """Prints the help message for the current mode."""
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")
#welcome()

def print_help():
    """Prints the help message for the current mode."""
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n") 

def run():
    import shlex, core, utils
    print_help()
    user_input = ''
    while(user_input != "exit"):
       user_input = welcome()
       args = shlex.split(user_input)
       print (args)
       match args[0].lower():
            case 'create_table':
                print(len(args))
                if len(args) < 2:
                    print ("Ошибка синтаксиса команды")
                else:
                    table_name = args[1]
                    print(table_name)
                    columns = args[2:]
                    print(columns)
                    metadata = utils.load_metadata(META_FILE)
                    core.create_table(metadata, table_name, columns)
            
            case 'drop_table':
                if len(args) != 2:
                    print(f'Функция удаления должна содержать только имя таблицы')
                else:
                    metadata = utils.load_metadata(META_FILE)
                    table_name = args[1]
                    core.drop_table(metadata, table_name)
            case 'list_tables':
                metadata = utils.load_metadata(META_FILE)
                core.list_tables(metadata)
            case 'exit':
                user_input = 'exit'
            case 'help':
                print_help()
              
            case _:
                print(f'Такой функции {args[0]} нет. Попробуйте снова.')

#run()