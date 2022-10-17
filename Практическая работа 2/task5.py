import random

def data_base():
    '''Функция создания базы данных сотрудников'''
    workers = create_workers()
    slots = []
    for i in range(1, len(workers) + 1):
        slot = 'Сотрудник №' + str(i)
        slots.append(slot)
    db = dict(zip(slots, workers))
    print(db)

def create_workers():
    '''Функция генерации инф. о сотрудниках'''
    names = ['Иванов И.И', 'Лазарев С.С.', 'Летучая Е.В', 'Высокий А.В.']
    pos = ['Директор', 'повар', 'младший аналитик', 'учитель']
    secret = ['Да', 'Нет']
    workers = list()
    for i in range(len(names)):
        info = [random.randint(20, 50), random.choice(pos), random.randint(1, 100), random.choice(secret)]
        worker_info = dict(zip(['возраст', 'должность', '№ рабочего места', 'Наличие доступа к тайне'], info))
        worker = {names[i]: worker_info}
        workers.append(worker)
    return workers

data_base()