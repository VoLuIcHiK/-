
def func(file_name):
    '''Функция чтения и вывода текста в консоль'''
    try:
        f = open(file_name)
    except:
        print('Файла нет')
    else:
        print(f.readlines())
        f.close()

func('Задание №2')
func('Задание №1')