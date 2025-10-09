"""

Liskov Substitution Principal (LSP)

An Object of a super class should be able to be replaced with
object of a subclass without affecting the correctness of the program.

"""

"""
This class violates the Liskov Substitution Principal (LSP) Principle.

The Non_primernumber class should behave like its superclass, 
but instead, it contradicts the superclass’s behavior.

This breaks the LSP because the subclass does not follow the expected behavior of the superclass.
"""

class Number:
    def divisible(self):
        print("This number is divisible by 2 with no remainder.")

class Non_primernumber(Number):
    def divisible(self):
        print("This number is not divisible by 2 with no remainder.")

# ===============================================================================#

"""
Refactored Solution:

- Make the base class `Number` abstract or generic, without assuming divisibility.
- Define subclasses `EvenNumber` and `OddNumber` that correctly implement the `divisible()` method based on their behavior.
- This design adheres to the Liskov Substitution Principle (LSP): it allows adding new subclasses without breaking the expected behavior.
"""


class Number:
    def divisible(self):
        pass

class EvenNumber(Number):
    def divisible(self):
        print("This number is divisible by 2 with no remainder.")

class OddNumber(Number):
    def divisible(self):
        print("This number is NOT divisible by 2 with no remainder.")

class Two(EvenNumber):
    pass
