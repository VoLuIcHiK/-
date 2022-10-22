import random

def func():
    '''Функция генерации 0 или 1 и последующее деление числа 10 на них'''
    try:
        res = 10 / random.randint(0, 1)
    except:
        print('Деление на 0')
    else:
        return res

