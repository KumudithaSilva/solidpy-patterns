class Singleton:
    _instance = None

    # override the new method which is control how object are created
    def __new__(cls):

        if not cls._instance:
            # create a new singleton instance using the parent class's __new__
            cls._instance = super().__new__(cls)
        # return the singleton instance class or newly created one
        return cls._instance


s1 = Singleton()
