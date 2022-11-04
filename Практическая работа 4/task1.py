
class Soda:
    '''
    Класс, определяющий тип газировки
    '''

    def __init__(self, ingred=None):
        self.ingred = ingred

    def show_my_drink(self):
        '''
        Метод, выводящий на экран тип напитка
        '''
        if self.ingred is not None:
            print('Газировка и {}'.format(self.ingred))
        else:
            print('Обычная газировка')


if __name__ == '__main__':
    soda1 = Soda('Барбарис')
    soda2 = Soda()
    soda1.show_my_drink()
    soda2.show_my_drink()