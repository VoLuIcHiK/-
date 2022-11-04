
class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        '''
        Метод, проверяющий введенные значения сторон будущего треугольника
        '''
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float)):
            if self.a > 0 and self.b > 0 and self.c > 0:
                if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                    print('Ура, можно построить треугольник!')
                else:
                    print('Жаль, но из этого треугольник не сделать.')
            else:
                print('С отрицательными числами ничего не выйдет!')
        else:
            print('Нужно вводить только числа!')


if __name__ == '__main__':
    tr1 = TriangleChecker(3, 4, 5)
    tr2 = TriangleChecker(-3, 4, 5)
    tr3 = TriangleChecker('3', 4, 5)
    tr4 = TriangleChecker(1, 1, 10)
    tr1.is_triangle()
    tr2.is_triangle()
    tr3.is_triangle()
    tr4.is_triangle()

