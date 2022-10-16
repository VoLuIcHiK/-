import random

class Statistics:

    def __init__(self):
        self.name = None
        self.industries = None


    @staticmethod
    def check_republics(buf, republics):
        for i in range(len(republics)):
            if buf == republics[i].name:
                return False
        return True

    def create_republics(self, num):
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
        industries = {'Сельское хозяйство': 0, 'Легкая промышленность': 0, 'Тяжелая промышленность группы А': 0,
                      'Тяжелая промышленность группы Б': 0, 'Военно промышленный комплекс': 0, 'Наука': 0,
                      'Химическая промышленность': 0}
        for i in range(len(republics)):
            dict = {k: random.randint(-1, 1) for (k, _) in industries.items()}
            republics[i].industries = dict
        return republics

    def find_most_industries(self, republics):
        industries = {'Сельское хозяйство': 0, 'Легкая промышленность': 0, 'Тяжелая промышленность группы А': 0,
                      'Тяжелая промышленность группы Б': 0, 'Военно промышленный комплекс': 0, 'Наука': 0,
                      'Химическая промышленность': 0}
        for i in range(len(republics)):
            for k in republics[i].industries:
                industries[k] += republics[i].industries[k]
        print(industries)
        most_developed = max(industries, key=industries.get)
        least_developed = min(industries, key=industries.get)
        print('Самая развитая отрасль: ', most_developed)
        print('Самая отстающая отрасль: ', least_developed)
        return most_developed, least_developed

    @staticmethod
    def output(republics):
        for i in range(len(republics)):
            print('Название республики: ', republics[i].name)
            print(republics[i].industries)
            print('_______________')

st = Statistics()
republics = st.create_republics(4)
m, l = st.find_most_industries(republics)


