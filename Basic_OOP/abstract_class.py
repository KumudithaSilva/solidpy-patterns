from abc import ABC, abstractmethod
from typing import override


# Define an abstract class 'Employee'
class Employee(ABC):
    @abstractmethod
    def role(self):
        pass

    def description(self):
        print(f"{self.__class__.__name__} says: {self.role()}")


# Define a concrete class 'Manager' that inherited from the Employee class
class Manager(Employee):
    def role(self):
        return "Manager"

    def description(self):
        super().description()

# Define a concrete class 'Manager' that inherited from the Employee class
class CEO(Employee):
    def role(self):
        return "CEO"

    def description(self):
        print(f"Company CEO says: {self.role()}")


manger = Manager()
manger.description()

ceo = CEO()
ceo.description()
