"""
Meta Class - It is a class that define the behaviour and rules for creating other class.

Metaclass allows to customize the class creation process and modify
class attribute, methods, or the properties before the class actually created.

By default, all Python classes implicitly inherit from the type build-class,
which itself a Meta class.
"""

class SingletonMeta(type):
    # Dictionary stores single instance of the class
    # Each subclass of the SingletonMeta metaclass
    _instance = {}

    def __call__(cls, *args, **kwargs):
        # If single instance of the class already been created?
        if cls not in cls._instance:
            # If not, create the instance of the class that calling this
            # that is Singleton class
            instance = super().__call__()
            cls._instance[cls] = instance
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def some_implementation(self):
        pass

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

# Check if all instances refer to the same object
print(id(s1))
print(id(s2))
print(id(s3))

# Verify if they are all the same object
print(s1 is s2)
print(s1 is s3)
print(s2 is s3)
