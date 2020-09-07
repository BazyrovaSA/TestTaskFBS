import math


class Triangle:
    def __init__(self, a, b, c):
        # Функция вычисления длин сторон треугольника по координатам вершин
        def side_len(dot1, dot2):
            return math.sqrt((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2)
        self.a = a
        self.b = b
        self.c = c
        # Вычисление длин сторон по соседним координатам
        self.ab = (side_len(self.a, self.b))
        self.bc = (side_len(self.b, self.c))
        self.ca = (side_len(self.c, self.a))

    # Метод вычисления площади треугольника по формуле Герона
    def area(self):
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.ab)
                         * (semi_perimeter - self.bc)
                         * (semi_perimeter - self.ca))

    # Метод вычисления периметра треугольника
    def perimeter(self):
        return self.ab + self.bc + self.ca

    # Метод определения существования треугольника
    def existence(self):
        if self.ab + self.bc <= self.ca or self.ab + self.ca <= self.bc or self.bc + self.ca <= self.ab:
            return False
        else:
            return True


triangle1 = Triangle((0.5, 0.1), (0.5, 0.2), (0.05, 0.3))
print(triangle1.area())
print(triangle1.perimeter())
print(triangle1.existence())

