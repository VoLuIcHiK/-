
def func(text):
    '''Функция записи строки в файл'''
    f = open('Задание №2', 'a+')
    f.write(text)
    f.close()

func('Привет\n')
func('Как дела?\n')
