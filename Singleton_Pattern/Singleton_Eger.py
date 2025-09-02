"""
Eager Loading - The Idea of eager loading is load the instance before need it.

It is useful for data preloading and caching, connectivity pre-caching and
frequent and fast access.

Python does not support eager instantiation, but using a metaclass, it can be achieved.

Eager loading can be achieved by called init method before call method
"""
class SingletonMeta(type):
    # Dictionary stores single instance of the class
    _instance = {}

    # This method is called when a class is created (not an object)
    # override the call during creation of the subtypes
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        # Create and store a single instance of the class right away
        # eager loading the class instance
        cls._instance[cls] = super().__call__()

    # This method is called when trying to create (call) an object of the class
    def __call__(cls, *args, **kwargs):
        # Instead of creating a new object, always return the same stored instance
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing Singleton instance")

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)