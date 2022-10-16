import random


class Hero:

    def __init__(self):
        self.name = None
        self.age = None
        self.class_ap = None
        self.params = None
        self.characteristics = []
        self.abilities = []

    def generate_name(self):
        '''Метод генерации имени'''
        names = ['Таод', 'Купалинг', 'Гумба', 'Могучий Пу', 'Варкрафт', 'Имлерих', 'Сахелантроп',
                 'Эхо Шамбер', 'Викарий Амелиа', 'Гик', 'Лудоман', 'Виртуальщик', 'Геймоголик']
        self.name = random.choice(names)

    def generate_age(self):
        '''Метод генерации возраста'''
        self.age = random.randint(10, 100)

    def generate_class_ap(self):
        '''Метод генерации класса апа'''
        class_ap = ['Воин', 'Маг', 'Охотник', 'Друид', 'Священник']
        self.class_ap = random.choice(class_ap)

    def generate_params(self):
        '''Метод генерации параметров'''
        params = {
            'Здоровье': random.randint(100, 1000),
            'Сила': random.randint(1, 10),
            'Скорость': random.randint(1, 10),
            'Выносливость': random.randint(1, 10),
            'Магия': random.randint(1, 10),
            'Удача': random.randint(1, 10),
            'Интеллект': random.randint(1, 10)
        }
        self.params = params

    def generate_characteristics(self):
        '''Метод генерации характеристик'''
        characteristics = ['Дружелюбность', 'Жестокость', 'Ловкость', 'Гордость',
                           'Преданность', 'Мудрость', 'Честность', 'Милосердие', 'Жадность', 'Алчность']
        self.characteristics = random.choices(characteristics, k=3)

    def generate_abilities(self):
        '''Метод генерации навыков'''
        abilities = ['Наука', 'Медицина', 'Огнестельное оружие', 'Холодное орежие',
                     'Рукопашный бой', 'Хитрость', 'Собирательство', 'Дипломатия',
                     'Друг зверей', 'Следопыт']
        self.abilities = random.choices(abilities, k=3)

    def output(self):
        '''Метод вывода инф. о созданном персонаже'''
        print('Информация о персонаже: ')
        print('Имя: ', h1.name)
        print('Возраст: ', h1.age)
        print('Класс апа: ', h1.class_ap)
        print('Характеристики: ', h1.characteristics)
        print('Параметры: ', h1.params)
        print('Навыки: ', h1.abilities)


h1 = Hero()
h1.generate_name()
h1.generate_age()
h1.generate_class_ap()
h1.generate_characteristics()
h1.generate_params()
h1.generate_abilities()
h1.output()