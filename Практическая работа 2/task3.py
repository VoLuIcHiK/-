
def sun_num(number):
    '''Функция вычисления суммы цифр, где
    number - число, сумму цифр которого необходимо найти,
    sum - перемнная для хранения суммы цифр числа'''
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum

print('Введите число: ')
number = int(input())
print('Результат работы программы: ', sun_num(number))