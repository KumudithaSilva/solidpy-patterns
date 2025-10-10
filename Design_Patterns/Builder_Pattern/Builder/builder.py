from abc import ABC, abstractmethod

# Define product class
class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print("Sandwich with following ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")


# Define abstract builder class
class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass

    def get_result(self):
        return self.sandwich


# Define Concrete builders
class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        pass

    def add_filling(self):
        pass


class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        pass

    def add_filling(self):
        pass

# Define the director class
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()