
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205


if __name__ == '__main__':
    f = KgToPounds(10)
    print('Кол-во кг: ', f.kg)
    print('{0} кг = {1} фунт.'.format(f.kg, f.to_pounds()))
    f.kg = 112.5
    print('Кол-во кг: ', f.kg)
    print('{0} кг = {1} фунт.'.format(f.kg, f.to_pounds()))


