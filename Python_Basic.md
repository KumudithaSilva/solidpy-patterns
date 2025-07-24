# 🐍 Python Basics

## Class and Objects

### 📘 Class
- A **class** is a blueprint for creating objects.
- It defines **attributes** (data) and **methods** (functions) that describe the object.

### 📦 Object
- An **object** is an instance of a class.
- It contains real data and can perform actions defined by the class.

---

### ✅ Example:

```python
# Define the greeting class
class Greeting:
    # Constructor for Greeting class
    def __init__(self, name):
        # Initialize 'name' with the provided value
        self.name = name
    # define the greeting method
    def say_hello(self):
        # Print a personalized greeting message
        print(f"Hello {self.name}")

# Creating an object of a Greeting class
# Initializing it with the name 'John'
greeting = Greeting('John')

# Call the 'say_hello' method on the 'greeting'
# Object to print the greeting message
my_greeting.say_hello()

