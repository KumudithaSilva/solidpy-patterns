import math


class Circle:
    def __init__(self, radius):
        # Initialize the radius property
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle
        return math.pi * (self.radius * self.radius)

    def circumference(self):
        # Calculate and return the circumference of the circle
        return 2 * math.pi * self.radius

    def diameter(self):
        # Calculate and return the diameter of the circle
        return 2 * self.radius


circle1 = Circle(3)
print(circle1.area())
print(circle1.circumference())
print(circle1.diameter())

circle2 = Circle(5)
print(circle2.area())
print(circle2.circumference())
print(circle2.diameter())
