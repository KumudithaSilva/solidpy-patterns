from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle1 = Rectangle("red", 4, 5)
print(rectangle1.area())
print(rectangle1.perimeter())

circle1 = Circle("blue", 3)
print(circle1.area())
print(circle1.perimeter())
