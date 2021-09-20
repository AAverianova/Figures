import math


class Dots(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def show(self):

        return '({}; {})'.format(self.x, self.y)


class Triangle(object):

    def __init__(self, ax, ay, bx, by, cx, cy):

        self.A = (ax, ay)
        self.B = (bx, by)
        self.C = (cx, cy)

    def area(self):
        s = abs((self.B[0] - self.A[0])*(self.C[1] - self.A[1]) - (self.C[0] - self.A[0]) * (self.B[1] - self.A[1]))/2
        return s

    def per(self):
        ab = math.sqrt(abs(self.A[0] - self.B[0])**2 + abs(self.A[1] - self.B[1])**2)
        bc = math.sqrt(abs(self.B[0] - self.C[0])**2 + abs(self.B[1] - self.C[1])**2)
        ac = math.sqrt(abs(self.A[0] - self.C[0])**2 + abs(self.A[1] - self.C[1])**2)
        perimetr = ab + bc + ac
        return perimetr

    def show(self):

        return 'A = {} B = {} C = {}'.format(self.A, self.B, self.C)


class Rect(object):

    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.A = (ax, ay)
        self.B = (bx, by)
        self.C = (cx, cy)
        self.D = (dx, dy)

    def area(self):
        ax = self.A[0]
        ay = self.A[1]
        bx = self.B[0]
        by = self.B[1]
        cx = self.C[0]
        cy = self.C[1]
        dx = self.D[0]
        dy = self.D[1]

        s = abs(ax * by + bx * cy + cx * dy + dx * ay - bx * ay - cx * by - dx * cy - ax * dy)/2
        return s


while True:
    ans = input('С чем вы хотите работать?\n-точка\n-треугольник\nпрямоугольник\n--')

    if ans == 'точка':
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
        dax = float(input('Введите координату x вершины А: '))
        day = float(input('Введите координату y вершины А: '))
        dbx = float(input('Введите координату x вершины B: '))
        dby = float(input('Введите координату y вершины B: '))
        dcx = float(input('Введите координату x вершины C: '))
        dcy = float(input('Введите координату y вершины C: '))
        ddx = float(input('Введите координату x вершины D: '))
        ddy = float(input('Введите координату y вершины D: '))
        A = Dots(dax, day)
        B = Dots(dbx, dby)
        C = Dots(dcx, dcy)
        D = Dots(ddx, ddy)
        ABCD = Rect(A.x, A.y, B.x, B.y, C.x, C.y, D.x, D.y)
        print(ABCD.area())

    q = input('Если хотите выйти введите q: ')
    if q == 'q':
        break
