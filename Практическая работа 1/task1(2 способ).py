def calculator():
    '''
    Функция калькулятора
    '''
    print('Введите выражение:')
    expr = input()
    try:
        result = eval(expr)
    except:
        return 'Error'
    else:
        return 'Результат работы программы: {}'.format(result)

print(calculator())