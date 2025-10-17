import pygame
import random
from abc import ABC, abstractmethod


# ------------------------------
# Base abstract class for shapes
# ------------------------------
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, surface):
        pass


# ------------------------------
# Concrete Shapes
# ------------------------------

class Circle(Shape):
    def __init__(self, color, x, y, radius):
        super().__init__(x, y)
        self.color = color
        self.radius = radius

    # Draw circle on given surface
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


class Rectangle(Shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(x, y)
        self.color = color
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


# ------------------------------
# Factory Interface
# ------------------------------

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, context) -> Shape:
        pass

    @staticmethod
    def random_color():
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )


# ------------------------------
# Concrete Factories
# ------------------------------

class CircleFactory(ShapeFactory):
    def create_shape(self, context) -> Shape:
        random.randint(10, 50)
        color = ShapeFactory.random_color()
        radius = random.randint(10, 50)
        return Circle(color, context.x, context.y, radius=radius)


class RectangleFactory(ShapeFactory):
    def create_shape(self, context) -> Shape:
        width = random.randint(10, 100)
        height = random.randint(10, 100)
        color = ShapeFactory.random_color()
        return Rectangle(color, context.x, context.y, width=width, height=height)


# ShapeContext class to hold factory parameters
class ShapeContext:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Main function to set up and run the game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Random Shapes")
    clock = pygame.time.Clock()

    shapes = []  # List to store created shapes
    running = True

    # Main game loop
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Create a random shape on mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:

                shape_factory_list = [CircleFactory(), RectangleFactory()]
                x, y = pygame.mouse.get_pos()
                shape_type = random.choice(shape_factory_list)
                context = ShapeContext(x, y)
                shape = shape_type.create_shape(context)
                shapes.append(shape)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw all the shapes
        for shape in shapes:
            shape.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
