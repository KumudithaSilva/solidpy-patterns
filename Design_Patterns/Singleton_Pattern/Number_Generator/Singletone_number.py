class Number_Generator:
    _instance = None
    _init_number = 0

    # override the new method which is control how object are created
    def __new__(cls):

        if not cls._instance:
            # create a new singleton instance using the parent class's __new__
            cls._instance = super(Number_Generator, cls).__new__(cls)
            # return the singleton instance class or newly created one
        return cls._instance

    def generate_next_number(self):
        self._init_number += 1

    def get_next_number(self):
        return self._init_number


if __name__ == "__main__":
    # Testing the singleton behavior and number generator
    number_gen_1 = Number_Generator()
    number_gen_2 = Number_Generator()

    print(f"number_gen_1: {id(number_gen_1)}")
    print(f"number_gen_2: {id(number_gen_2)}\n")

    number_gen_1.generate_next_number()
    print(f"number generator 1: {number_gen_1.get_next_number()}")

    number_gen_2.generate_next_number()
    print(f"number generator 2: {number_gen_2.get_next_number()}")

    number_gen_1.generate_next_number()
    print(f"number generator 1: {number_gen_1.get_next_number()}")
