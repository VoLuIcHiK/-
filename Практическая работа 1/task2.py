import random


def input_words():
    '''
    Функция ввода данных с клиаватуры, где
        nouns - массив для хранения существительных,
        verbs - массив для хранения глаголов
        num - кол-во фраз, которые необходимо сгенерировать
    '''
    nouns = []
    verbs = []
    noun = input('Введите существительные: ')
    while noun != 'стоп':
        nouns.append(noun)
        noun = input()
    verb = input('Введите глаголы: ')
    while verb != "стоп":
        verbs.append(verb)
        verb = input()
    num = int(input('Введите кол-во фраз, которые необходимо сгенерировать: '))
    return nouns, verbs, num

def SGS(nouns, verbs, num):
    '''Функция создание фразы типа СГС'''
    result = list()
    for i in range(num):
        phrase = random.choice(nouns) + ' ' + random.choice(verbs) + ' ' + random.choice(nouns)
        result.append(phrase)
    return result

def GSS(nouns, verbs, num):
    '''Функция создание фразы типа ГСС'''
    result = list()
    for i in range(num):
        phrase = random.choice(verbs) + ' ' + random.choice(nouns) + ' ' + random.choice(nouns)
        result.append(phrase)
    return result

def SSG(nouns, verbs, num):
    '''Функция создание фразы типа СГС'''
    result = list()
    for i in range(num):
        phrase = random.choice(nouns) + ' ' + random.choice(nouns) + ' ' + random.choice(verbs)
        result.append(phrase)
    return result

def generate_phrases(nouns, verbs, num):
    '''
     Функция генерирования фраз, где
        nouns - массив существительных,
        verbs - массив глаголов
        num - кол-во фраз, которые необходимо сгенерировать
    '''
    for i in range(num):
        print(SGS(nouns, verbs, num)[i])
        print(GSS(nouns, verbs, num)[i])
        print(SSG(nouns, verbs, num)[i])

nouns, verbs, num = input_words()
generate_phrases(nouns, verbs, num)


