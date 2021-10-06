import math


class Dots(object):


    def __init__(self, x, y):

        self.x = x
        self.y = y
# Если получать x и y из вне при инициализации, то тогда придется все внешние программы переделывать при измении класса. что плохо.
# Можно сделать так:
# def __init__(self):
#
#        self.x = float(input('Введите координату x: '))
#        self.y= float(input('Введите координату y: '))
        
    def show(self):

        return '({}; {})'.format(self.x, self.y)

    def distance (self, A):
        return math.sqrt(abs(self.x - A.x)**2 + abs(self.y-A.y)**2)
    
    
class Triangle(object):

    def __init__(self, ax, ay, bx, by, cx, cy):
# Тоже самое. При инициализации я должна знать какие данные что означают. А если я не могу посмотреть? Коммерческая тайна?
#     def __init__(self):
#
#        self.A = Dots()
#        self.B = Dots()
#        self.C = Dots()
        
        self.A = (ax, ay)
        self.B = (bx, by)
        self.C = (cx, cy)

    def area(self):
        s = abs((self.B[0] - self.A[0])*(self.C[1] - self.A[1]) - (self.C[0] - self.A[0]) * (self.B[1] - self.A[1]))/2
        return s

    def per(self):
 #  расчет расстояния следует вынести в один метод. Т.к. оно повторяется, и если изменится, то менять придется только в одном месте.
        ab = math.sqrt(abs(self.A[0] - self.B[0])**2 + abs(self.A[1] - self.B[1])**2)
        bc = math.sqrt(abs(self.B[0] - self.C[0])**2 + abs(self.B[1] - self.C[1])**2)
        ac = math.sqrt(abs(self.A[0] - self.C[0])**2 + abs(self.A[1] - self.C[1])**2)
        perimetr = ab + bc + ac
        return perimetr

    def show(self):

        return 'A = {} B = {} C = {}'.format(self.A, self.B, self.C)


class Rect(object):

    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        print('Точка 1')
        self.A = Dots()
        print('Точка 2')
        self.B = Dots()
        print('Точка 3')
        self.C = Dots()
        print('Точка 4')
        self.D = Dots()


    def area(self):
        ab =  self.A.distance(self.B)
        cd =  self.C.distance(self.D)
        s = ab*cd
        return s



while True:
    ans = input('С чем вы хотите работать?\n-точка\n-треугольник\nпрямоугольник\n--')

    if ans == 'точка':
        # Если это класс точка, то необходимо использовать методы класса точка для работы с полями этого класса. Когда будут трехмерные координаты, всю программу придется переписывать.
        # А если будет требование что читать не из консоли а из файла, то снова все эти условия менять и переписывать?
        # Если будет запрос данных в инициализации, то все упрощается
        #  dot = Dots()
        dot_x = float(input('Введите координату x: '))
        dot_y = float(input('Введите координату y: '))
        dot = Dots(dot_x, dot_y)
        
        print('Координаты точки:', dot.show())
    elif ans == 'треугольник':
        dot_a_x = float(input('Введите координату x вершины А: '))
        dot_a_y = float(input('Введите координату y вершины А: '))
        dot_b_x = float(input('Введите координату x вершины B: '))
        dot_b_y = float(input('Введите координату y вершины B: '))
        dot_c_x = float(input('Введите координату x вершины С: '))
        dot_c_y = float(input('Введите координату y вершины С: '))
        if ((dot_a_x != dot_b_x) or (dot_a_y != dot_b_y)) and ((dot_b_x != dot_c_x) or (dot_b_y != dot_c_y)) and ((dot_a_x != dot_c_x) or (dot_a_y != dot_c_y)):
            A = Dots(dot_a_x, dot_a_y)
            B = Dots(dot_b_x, dot_b_y)
            C = Dots(dot_c_x, dot_c_y)
            ABC = Triangle(A.x, A.y, B.x, B.y, C.x, C.y)
            print(ABC.show())
            print('Площадь треугольника равна:', ABC.area())
            print('Периметр треугольника равен:', ABC.per())
        else:
            print('Вы ввели прямую')
            continue
    elif ans == 'прямоугольник':
        ABCD = Rect()
        print(ABCD.area())

    q = input('Если хотите выйти введите q: ')
    if q == 'q':
        break
