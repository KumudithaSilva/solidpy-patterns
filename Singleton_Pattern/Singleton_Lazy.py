class Singleton:
    # class-level variable to hold the single class variable
    _instance = None

    # override the new method which control how object are created
    def __init__(self):
        # This will not allow to initialize the constructor
        raise RuntimeError("Call Instance Instead")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            # Create new instance of the class
            cls._instance = cls.__new__(cls)
        return cls._instance


s1 = Singleton.get_instance()
