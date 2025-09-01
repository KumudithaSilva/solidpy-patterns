"""
Eager Loading - The Idea of eager loading is load the instance before need it.

It is useful for data preloading and caching, connectivity pre-caching and
frequent and fast access.

Python does not support eager instantiation, but using a metaclass, it can be achieved.

Eager loading can be achieved by called init method before call method
"""
class SingletonMeta(type):
    _instance = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instance[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass