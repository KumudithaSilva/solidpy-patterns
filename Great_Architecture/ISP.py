"""

Interface Separation Principal (ISP)

It states that class should not be forced to depend on interfaces they do not use.

"""

"""
This class violates the Interface Segregation Principle (ISP).

The Pizza class only needs methods that are relevant to pizza, but it depends on an interface that includes 
some irrelevant methods that it is still required to implement.

This breaks ISP because a class should not be forced to depend on methods or interfaces it does not use.
"""

from abc import ABC, abstractmethod
class IRestaurantMenu(ABC):
    @abstractmethod
    def pizza(self):
        pass

    @abstractmethod
    def sushi(self):
        pass

    @abstractmethod
    def burger(self):
        pass

    @abstractmethod
    def smoothie(self):
        pass

class Pizza(IRestaurantMenu):
    def pizza(self):
        print("Ordering pizza")


# ===============================================================================#

"""
Refactored Solution:

- It breaks the single IPizzaMenu interface into smaller, more specific interfaces.
- The Pizza class should only implement the IPizzaMenu interface, which defines the behavior it actually supports.
- This design adheres to the Interface Segregation Principle (ISP): it only requires a class to implement the methods that are relevant to its behavior.

- Make the base class `Number` abstract or generic, without assuming divisibility.
- Define subclasses `EvenNumber` and `OddNumber` that correctly implement the `divisible()` method based on their behavior.
- This design adheres to the Liskov Substitution Principle (LSP): it allows adding new subclasses without breaking the expected behavior.
"""

from abc import ABC, abstractmethod

class IPizzaMenu(ABC):
    @abstractmethod
    def pizza(self):
        pass

class ISushiMenu(ABC):
    @abstractmethod
    def sushi(self):
        pass

class IBurger(ABC):
    @abstractmethod
    def burger(self):
        pass

class ISmoothie(ABC):
    @abstractmethod
    def smoothie(self):
        pass

class Pizza_Order(IPizzaMenu):
    def pizza(self):
        print("Ordering pizza")


