import random


def check_repeats(buf, set):
    '''Функция для проверки на повтор товаров'''
    for i in range(len(set)):
        if buf == set[i]:
            return False
    return True

def create_mas(num, gods):
    '''Создание массива с товарами'''
    mas = []
    for i in range(num):
        buf = random.choice(gods)
        res = check_repeats(buf, mas)
        if res == True:
            mas.append(buf)
    return mas

def find_diff_set(set_1, set_2):
    '''Поиск уникальных элементов в обоих множествах'''
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set

def func():
    '''Основной алгоритм программы'''
    gods = ['шоколад', 'хлеб', 'молоко', 'масло', 'сыр', 'колбаса', 'сметана',
            'конфеты', 'джем', 'сгущенка', 'сок', 'макароны', 'творог', 'йогурт', 'печенье', 'вафли', 'мука']
    rnd_num1 = random.randint(1, 10)
    rnd_num2 = random.randint(1, 10)
    set_1 = set(create_mas(rnd_num1, gods))
    set_2 = set(create_mas(rnd_num2, gods))
    diff_set = find_diff_set(set_1, set_2)
    print('Множества №1: ', set_1)
    print('Множество №2: ', set_2)
    print('Уникальные значения двух множеств: ', diff_set)


func()