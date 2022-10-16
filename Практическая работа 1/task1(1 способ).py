import math

class Calculator:

    def __init__(self):
        pass
    #сложение
    def add(self, n1, n2):
        return 'Результат работы программы: {}'.format(n1 + n2)

    #вычитание
    def sub(self, n1, n2):
        return 'Результат работы программы: {}'.format(n1 - n2)

    #умножение
    def mult(self, n1, n2):
        return 'Результат работы программы: {}'.format(n1 * n2)

    #деление
    def div(self, n1, n2):
        try:
            result = n1 / n2
        except ZeroDivisionError:
            return 'Error'
        else:
            return 'Результат работы программы: {}'.format(result)

    #возведение в степень
    def pow(self, n1, n2):
        return 'Результат работы программы: {}'.format(n1 ** n2)

    #получение остатка от деления
    def rem_of_div(self, n1, n2):
        try:
            result = n1 % n2
        except ZeroDivisionError:
            return 'Error'
        else:
            return 'Результат работы программы: {}'.format(result)

    #извлечение корня
    def get_root(self, n1):
        return 'Результат работы программы: {}'.format(math.sqrt(n1))




