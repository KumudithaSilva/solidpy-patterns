from abc import ABC, abstractmethod
import random

# ======Classic Factory Pattern=====

# Classic Factory Method Pattern uses inheritance and polymorphism.
# Unique Feature: Each product type has its own factory class.
# Easily extensible: It can add new types by adding new factories.
# Better for large systems where object creation varies frequently.

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


# Concrete spaceships
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


# Factory Interface
class SpaceShipFactory(ABC):
    @abstractmethod
    def create_spaceship(self) -> SpaceShip:
        pass


# Concrete Factories
class MillenniumFactory(SpaceShipFactory):
    def create_spaceship(self) -> SpaceShip:
        return MillenniumFalcon((12, 10), 100, "Falcon", "200Km")


class UNSCInfinityFactory(SpaceShipFactory):
    def create_spaceship(self) -> SpaceShip:
        return UNSCInfinity((12, 10), 120, "UNSC", "400Km")


class USSEnterpriseFactory(SpaceShipFactory):
    def create_spaceship(self) -> SpaceShip:
        return USSEnterprise((12, 10), 100, "USS", "600Km")


class SerenityFactory(SpaceShipFactory):
    def create_spaceship(self) -> SpaceShip:
        return Serenity((12, 10), 100, "SERENITY", "800Km")


# Main function to set up and run the game loop
def main():

    spaceship_factory_list = [
        MillenniumFactory(),
        UNSCInfinityFactory(),
        USSEnterpriseFactory(),
        SerenityFactory(),
    ]

    for _ in range(2):
        spaceship_factory = random.choice(spaceship_factory_list)
        spaceship = spaceship_factory.create_spaceship()
        print(spaceship.createShip())


if __name__ == "__main__":
    main()
