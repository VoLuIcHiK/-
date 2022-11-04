
class RealString:

    def __init__(self, str):
        self.str = str

    @staticmethod
    def compare_obj(obj1, obj2):
        '''
        Метод, сравнивающий строки двух объектов, где
        obj1 - объект №1;
        obj2 - объект №2.
        '''
        if len(obj1.str) > len(obj2.str):
            print('Строка \'{0}\' длиннее строки \'{1}\''.format(obj1.str, obj2.str))
        else:
            print('Строка \'{1}\' длиннее строки \'{0}\''.format(obj1.str, obj2.str))

    def compare_str(self, str):
        '''
        Метод, сравнивающий значение поля str объекта класса RealString и введенную строку, где
        str - введенная строка
        '''
        if len(self.str) > len(str):
            print('Строка \'{0}\' длиннее строки \'{1}\''.format(self.str, str))
        else:
            print('Строка \'{1}\' длиннее строки \'{0}\''.format(self.str, str))

if __name__ == '__main__':
    obj1 = RealString('Ура, выходные!')
    obj2 = RealString('Привет!')
    RealString.compare_obj(obj1, obj2)
    str = 'Кофе - лучший друг студента!'
    obj1.compare_str(str)