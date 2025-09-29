"""
Eager Loading Singleton using metaclass __init__

1. This version creates the instance eagerly when the class is defined (not when an object is created)
2. The instance is created inside the metaclass's __init__ method and runs after the class is created.
3. It is useful for data preloading and caching, connectivity pre-caching and frequent and fast access.
4. Python does not support eager instantiation, but using a metaclass, it can be achieved.
5. Eager loading can be achieved by called init method before call method.

"""
class SingletonMeta(type):
    # Dictionary stores single instance of the class
    _instance = {}

    # Called when the class is defined (not instantiated)
    # override the call during creation of the subtypes
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        # Create and store a single instance of the class right away
        # eager loading the class instance
        cls._instance[cls] = super().__call__()
        print("Initializing <super>")

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