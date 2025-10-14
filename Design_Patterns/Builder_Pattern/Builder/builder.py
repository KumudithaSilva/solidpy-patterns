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
        self.sandwich.add_ingredients("White Bread")

    def add_filling(self):
        self.sandwich.add_ingredients("Lettuce")
        self.sandwich.add_ingredients("Tomato")
        self.sandwich.add_ingredients("Cucumber")


class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredients("White Bread")


    def add_filling(self):
        self.sandwich.add_ingredients("Ham")
        self.sandwich.add_ingredients("Cheese")
        self.sandwich.add_ingredients("Mayonnaise")

# Define the director class
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()

# Client
veggie_builder = VeggieSandwichBuilder()
director = SandwichDirector(veggie_builder)
veggie_sandwich = director.build_sandwich()

ham_builder = HamSandwichBuilder()
director = SandwichDirector(ham_builder)
ham_sandwich = director.build_sandwich()

print("==VeggieSandwichBuilder==")
[print(veg) for veg in veggie_sandwich.ingredients]

print("\n==HamSandwichBuilder==")
[print(ham) for ham in ham_sandwich.ingredients]