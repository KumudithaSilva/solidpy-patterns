from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class FirstClass(MyInterface):
    def my_method(self):
        print("This method implemented in FirstClass")

class SecondClass(MyInterface):
    def my_method(self):
        print("This method implemented in SecondClass")


my_first = FirstClass()
my_first.my_method()

my_second = SecondClass()
my_second.my_method()