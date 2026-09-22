import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.prod([self.a, self.b])


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


try:
    a = float(input("Введите 1-ю сторону прямоугольника: "))
    b = float(input("Введите 2-ю сторону прямоугольника: "))
    r = float(input("Введите радиус круга: "))
except ValueError:
    print("Введите число")
else:
    circle = Circle(r)
    print(circle.area())

    rectangle = Rectangle(a, b)
    print(rectangle.area())
