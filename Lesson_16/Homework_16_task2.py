from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculating the area of a figure"""
        pass

    @abstractmethod
    def parameter(self):
        """Calculating the parameter of a figure"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def parameter(self):
        return 2 * math.pi * self.__radius


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def parameter(self):
        return 4 * self.__side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height= height

    def area(self):
        return self.__width * self.__height

    def parameter(self):
        return 2 * (self.__width + self.__height)

Shapes = [
    Circle(6),
    Square(10),
    Rectangle(4, 7)
]

for shape in Shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"Area: {shape.area():.2f}")
    print(f"Parameter: {shape.parameter():.2f}")



