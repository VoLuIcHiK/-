import shutil
import os

def func(file_name, new_file_name):
    '''Функция копирования содержимого файла и удаления с помощью shutil.copy()'''
    try:
        shutil.copy(file_name, new_file_name)
    except:
        print('Сначала запустите task2')
    else:
        os.remove(file_name)
        f = open(new_file_name)
        print(f.readlines())
        f.close()

func('Задание №2', 'Задание №4')