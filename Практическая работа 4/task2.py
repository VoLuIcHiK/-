
class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_name(self):
        '''
        Метод, проверяющий кооректность введенного имени
        '''
        if self.name != 'Николай':
            self.name = 'Я не {}, а Николай'.format(self.name)
        else:
            pass

if __name__ == '__main__':
    m1 = Nikola('Николай', 11)
    m2 = Nikola('Сережа', 14)
    m1.check_name()
    m2.check_name()
    print(m1.name)
    print(m2.name)
