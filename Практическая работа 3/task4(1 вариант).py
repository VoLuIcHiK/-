import os

def func(file_name, new_file_name):
    '''Функция копирования содержимого файла и удаления '''
    try:
        f_old = open(file_name)
    except:
        print('Сначала запустите task2')
    else:
        f_new = open(new_file_name, 'a+')
        text = f_old.readlines()
        f_new.writelines(text)
        os.remove(file_name)
        f_new.close()

func('Задание №2', 'Задание №4')