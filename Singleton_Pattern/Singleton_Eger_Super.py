"""
Eager Loading Singleton using metaclass __new__

1. This version also creates the instance eagerly, but does it during the metaclass's __new__ method.
2. The instance is created inside the metaclass's __new__ method and runs before the class is fully created.
3. It is useful for data preloading and caching, connectivity pre-caching and frequent and fast access.
4. Python does not support eager instantiation, but using a metaclass, it can be achieved.
5. Eager loading can be achieved by called init method before call method.

"""
class SingletonMeta(type):
    # Dictionary stores single instance of the class
    _instance = {}

    # This method is called when a class is created (not an object)
    # override the call during creation of the subtypes
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        print("Initializing <super>")
        cls._instance[new_class] = super(SingletonMeta, new_class).__call__()
        return  new_class

    # This method is called when trying to create (call) an object of the class
    def __call__(cls, *args, **kwargs):
        # Instead of creating a new object, always return the same stored instance
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing <child>")

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)