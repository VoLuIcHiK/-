import random

class Statistics:
    '''Класс 'Стистика' для генерирования республик и их характеристик,
    а также для поиска самых развитых, наименеее развитых и сбалансированно развитых отраслей республик, где
    republics - массив республик (объектов класса Statistics),
    most_developed - переменная для хранения наиболее развитой области,
    least_developed - переменная для хранения наименее развитой области,
    balanced_developed - переменная для хранения сбалансированно развитых областей,
    '''

    def __init__(self):
        self.name = None
        self.industries = None


    @staticmethod
    def check_republics(buf, republics):
        '''Метод для проверки на повтор сгенерированного названия республики, где
        buf - новая сгенерированная республика,
        republics - массив с уже созданными республиками
        '''
        for i in range(len(republics)):
            if buf == republics[i].name:
                return False
        return True

    def create_republics(self, num):
        '''Метод генерация республик
        '''
        names = ['Белорусская ССР', 'Узбекская ССР', 'Казахская ССР', 'Грузинская ССР', 'Азербайджанская ССР',
                 'Литовская ССР', 'Молдавская ССР', 'Латвийская ССР', 'Киргизская ССР', 'Таджикская ССР',
                 'Армянская ССР', 'Туркменская ССР', 'Эстонская ССР']
        republics = list()
        for i in range(num):
            res = False
            while res != True:
                buf = random.choice(names)
                res = self.check_republics(buf, republics)
                if res == True:
                    obj = Statistics()
                    obj.name = buf
                    republics.append(obj)
        republics = self.assign_values(republics)
        self.output(republics)
        return republics

    @staticmethod
    def assign_values(republics):
        '''Метод генерации отраслец для каждой республики'''
        industries = {'Сельское хозяйство': 0, 'Легкая промышленность': 0, 'Тяжелая промышленность группы А': 0,
                      'Тяжелая промышленность группы Б': 0, 'Военно промышленный комплекс': 0, 'Наука': 0,
                      'Химическая промышленность': 0}
        for i in range(len(republics)):
            dict = {k: random.randint(-1, 1) for (k, _) in industries.items()}
            republics[i].industries = dict
        return republics

    def find_most_industries(self, republics):
        '''Метод поиска самых развитых, наименеее развитых и сбалансированно развитых отраслей республик'''
        industries = {'Сельское хозяйство': 0, 'Легкая промышленность': 0, 'Тяжелая промышленность группы А': 0,
                      'Тяжелая промышленность группы Б': 0, 'Военно промышленный комплекс': 0, 'Наука': 0,
                      'Химическая промышленность': 0}
        for i in range(len(republics)):
            for k in republics[i].industries:
                industries[k] += republics[i].industries[k]
        most_developed = max(industries, key=industries.get)
        least_developed = min(industries, key=industries.get)
        balanced_developed = [k for k in industries if industries[k] == 0]
        print('Самая развитая отрасль: ', most_developed)
        print('Самая отстающая отрасль: ', least_developed)
        print('Самые сбалансированн-ая/-ые отрасл-ь/-и: ', balanced_developed)
        self.find_most_republics(republics, most_developed, least_developed, balanced_developed)
        self.statistics(republics)
        return most_developed, least_developed, balanced_developed

    @staticmethod
    def find_most_republics(republics, most_developed, least_developed, balanced_developed):
        '''Метод поиска республик сильно развитых, отстающих в развитии или сбалансированно развитых в отраслях'''
        count = 0
        for i in range(len(republics)):
            if republics[i].industries[most_developed] == 1:
                count += 1
        print('Кол-во развитых республик в отрасли \'{0}\' равно {1}'.format(most_developed, count))
        count = 0
        for i in range(len(republics)):
            if republics[i].industries[least_developed] == -1:
                count += 1
        print('Кол-во отстающих республик в отрасли \'{0}\' равно {1}'.format(least_developed, count))
        count = 0
        for i in range(len(republics)):
            for j in range(len(balanced_developed)):
                if republics[i].industries[balanced_developed[j]] == 0:
                    count += 1

        print('Кол-во сбалансированных республик в отрасл-и/-ях {0} равно {1}'.format(balanced_developed, count))

    @staticmethod
    def statistics(republics):
        '''Метод создания статистики по всем отраслям'''
        print('Стистика по отраслям: ')
        keys = ['Сельское хозяйство', 'Легкая промышленность', 'Тяжелая промышленность группы А',
                'Тяжелая промышленность группы Б', 'Военно промышленный комплекс', 'Наука',
                'Химическая промышленность']
        for k in keys:
            count = 0
            for i in range(len(republics)):
                if republics[i].industries[k] == -1 or republics[i].industries[k] == 1:
                    count += 1
            print('{0}: {1}'.format(k, count))

    @staticmethod
    def output(republics):
        for i in range(len(republics)):
            print('Название республики: ', republics[i].name)
            print(republics[i].industries)
            print('_______________')

st = Statistics()
republics = st.create_republics(4)
m, l, b = st.find_most_industries(republics)


