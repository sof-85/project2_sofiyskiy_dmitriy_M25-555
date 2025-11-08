import prompt

def welcome():
   print('\n***')
   print('<command> exit - выйти из программы')  
   print('<command> help - справочная информация')
   command = prompt.string('Введите команду ')
   return command
   
#welcome()