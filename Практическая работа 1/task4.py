import time

def timer(hours, minutes, seconds):
    '''Функция, отвечающая за вывод таймера, где
        hours - оставшееся кол-во часов,
        minutes - оставшееся кол-во минут,
        seconds - оставшееся кол-во секунд'''
    for i in range(hours * 3600 + minutes * 60 + seconds):
        print('{0}:{1}:{2}'.format(hours, minutes, seconds))
        time.sleep(1)
        seconds -= 1
        if seconds < 0:
            seconds = 59
            minutes -= 1
        elif minutes < 0:
            minutes = 59
            hours -= 1
        elif hours == 0 and minutes == 0 and seconds == 1:
            print('{0}:{1}:{2}'.format(hours, minutes, seconds))
            time.sleep(1)
            seconds -= 1
            print('ВРЕМЯ ВЫШЛО!')
            break

def get_time():
    '''Функция ввода времени с клавиатуры'''
    print('Введите время в формате ЧЧ:ММ:СС')
    str = input()
    time = str.split(':')
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    if hours > 23 or minutes > 60 or seconds > 60:
        return 'Введите корректное время'
    else:
        return hours, minutes, seconds

hours, minutes, seconds = get_time()
timer(hours, minutes, seconds)