import re
import difflib

def input_words():
    '''
    Функция ввода данных с клиаватуры, где
        text - строка для хранения введенного предложения,
        correct - массив для хранения "правильных" слов,
        check - массив для хранения слов, которые необхожимо проверить
    '''
    print('Введите "правильные" слова: ')
    text = input()
    correct = re.sub(r'[^\w\s]', '', text).split(' ')
    print('Введите предложение, которое необходимо проверить: ')
    text = input()
    check = re.sub(r'[^\w\s]', '', text).split(' ')
    return correct, check

def get_worng_words(correct, check):
    '''
    Функция определения и вывода слов, в которых содержатся ошибки, где
        correct - массив "правильных" слов,
        check - массив слов, которые необхожимо проверить
        result - массив слов, где указаны ошибки
    '''
    result = []
    for i in range(len(check)):
        for j in range(len(correct)):
            str = ''
            mark = difflib.SequenceMatcher(None, correct[j], check[i])
            if 0.6 < mark.ratio() < 1.0:
                for k in range(len(check[i])):
                    if check[i][k] != correct[j][k]:
                        str += '_' + check[i][k] + '_'
                    else:
                        str += check[i][k]
                result.append(str)
                break
    return result

def output(result):
    '''Функция вывода результата на экран, где
        result - массив слов, где указаны ошибки'''
    print('Результат работы программы: {}'.format(result))

correct, check = input_words()
result = get_worng_words(correct, check)
output(result)
