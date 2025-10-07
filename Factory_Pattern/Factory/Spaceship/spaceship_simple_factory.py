from abc import ABC, abstractmethod
from enum import Enum, auto
import random

# ======Simple Factory Pattern=====

# Simple Factory Pattern uses a single factory class to create all types of objects.
# Unique Feature: One centralized factory method.
# Not easily extensible: It must modify the factory when adding new types.
# Good for small-scale object creation when flexibility isn’t a priority.


class SpaceShipType(Enum):
    MILLENNIUMFALCON = auto()
    UNSCINFINITY = auto()
    USSENTERPRISE = auto()
    SERENITY = auto()


# Base abstract class for spaceship
class SpaceShip(ABC):
    def __init__(self, position, size, name, speed):
        self.x = position[0]
        self.y = position[1]

        self.size = size
        self.name = name
        self.speed = speed

    @abstractmethod
    def createShip(self):
        pass


class MillenniumFalcon(SpaceShip):
    def createShip(self):
        return f"Created {self.name} with speed of {self.speed}"


class UNSCInfinity(SpaceShip):
    def createShip(self):
        return f"Created {self.name} with speed of 2X{self.speed}"


class USSEnterprise(SpaceShip):
    def createShip(self):
        return f"Created {self.name} with speed of 3X{self.speed}"


class Serenity(SpaceShip):
    def createShip(self):
        return f"Created {self.name} with speed of 4X{self.speed}"


# A single factory class with a static method that returns concrete instances.
class SpaceShipFactory:
    @staticmethod
    def create_spaceship(spaceship):

        if spaceship == SpaceShipType.MILLENNIUMFALCON:
            return MillenniumFalcon((12, 10), 100, "Falcon", "200Km")

        elif spaceship == SpaceShipType.UNSCINFINITY:
            return UNSCInfinity((12, 10), 120, "UNSC", "400Km")

        elif spaceship == SpaceShipType.USSENTERPRISE:
            return USSEnterprise((12, 10), 100, "USS", "600Km")

        elif spaceship == SpaceShipType.SERENITY:
            return Serenity((12, 10), 100, "SERENITY", "800Km")

        else:
            raise ValueError("Invalid spaceship type")


# Main function to set up and run the game loop
def main():

    spaceship_factory = SpaceShipFactory()
    spaceships_list = []

    for _ in range(2):
        spaceship_type = random.choice(list(SpaceShipType))
        spaceships = spaceship_factory.create_spaceship(spaceship_type)
        spaceships_list.append(spaceships)

    for i in spaceships_list:
        print(i.createShip())


if __name__ == "__main__":
    print("======Simple Factory Pattern=====\n")
    main()
