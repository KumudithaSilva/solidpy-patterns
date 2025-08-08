from abc import ABC, abstractmethod

# Define abstract class
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        print(f"{self.__class__.__name__} has the color {self.color}")


# Define a concrete classes that inherits from shape

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radios = radius

    def perimeter(self):
        return 2 * 3.145 * self.radios

    def area(self):
        return  3.145 * (self.radios ** 2)

# Interface contact method
def process_shape(obj : Shape):
    obj.description()

rectangle = Rectangle(20, 12, "Blue")
print(f"Rectangle area is: ", rectangle.area())

circle = Circle(7,"Green")
print(f"Circle area is: ", circle.area())

process_shape(rectangle)
process_shape(circle)
