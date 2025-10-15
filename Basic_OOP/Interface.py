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


class ThirdClass:
    def some_method(self):
        print("This class not implementing the MyInterface")


def process_my_interface(obj: MyInterface):
    obj.my_method()
    print("This object implemented MyInterface")


my_first = FirstClass()
# my_first.my_method()

my_second = SecondClass()
# my_second.my_method()

my_third = ThirdClass()
my_third.some_method()

process_my_interface(my_first)
process_my_interface(my_second)
