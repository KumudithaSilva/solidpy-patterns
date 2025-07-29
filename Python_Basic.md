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
```
```
+---------------------------------+
|          Greeting               |
+---------------------------------+
| - name: str                     |
+---------------------------------+
| << create >>+Greeting(name:str) |
| + say_hello():void              |
+---------------------------------+
```

## Object-Oriented Programming (OOP)

### 💊 Encapsulation
- It is a concept of bundling data (attributes) and methods (functions) that operate on that data within a single unit.
- In gerneral a well design class already achieves encapsulation.

### ✅ Example:

```python
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):
        return f"{self.name} (born {self.birth_year})"

class Book:
    def __init__(self, title, pub_year, author: Author):
        self.title = title
        self.publication_year = pub_year
        self.author = author

    def get_book_info(self):
        return f" {self.title} by {self.author.get_author_info()}, published in {self.publication_year}"

```

```
+-------------------------------------------------------------------+
|          Book                                                     |
+-------------------------------------------------------------------+
| - title: str                                                      | 
| - publication_year: int                                           |
| - author: Author                                                  |
+-------------------------------------------------------------------+
| << create >>+Book(title:str, publication_year:int, author:Author) |
| + get_book_info():str                                             |
+-------------------------------------------------------------------+
              |
              | 1
              |
              |-----------------------------+
                                            |
                                            | *
+-----------------------------------------------+
|          Author                               |
+-----------------------------------------------+
| - name: str                                   |
| - birth_year: int                             |
+-----------------------------------------------+
| << create >>+Author(name:str, birth_year:int) |
| + get_author_info():str                       |
+-----------------------------------------------+


```


### 🌲 Inheritance
- It is a mechanism where a class (child/subclass) can inherit attributes and methods from another class (parent/superclass).
- It allows to generalize

### ✅ Example:

```python
# Base Class
class Animal:
    def __init__(self, name,):
        self.name = name

    def speak(self):
        print (f"{self.name} make a sound.")

# Derived Class
class Dog(Animal):
    def speak(self):
        print (f"{self.name} barks.")

# Derived Class
class Cat(Animal):
    def speak(self):
        print (f"{self.name} meows.")

```
```
+--------------------------------+
|          Animal                |
+--------------------------------+
| -name:str                      |
+--------------------------------+
| << create >>+Animal(name:str)  |
| +speak(): void()               |
+--------------------------------+
      ^                  ^           
      |                  |
      |                  |   
      |                  |
      +----------        +--------------
                |                       |
                |                       |
+-----------------------------+  +----------------------------+
|             Dog            |   |             Cat            |
+----------------------------+   +----------------------------+   
+----------------------------+   +----------------------------+
| << create >>+Dog(name:str) |   | << create >>+Cat(name:str) |
| << override >>+speak()void |   | << override >>+speak()void |
+----------------------------+   +----------------------------+
```

### 🧩 Interfaces
- It is like a promise: it defines methods that a class must implement, but does not provide the method’s code.
- Interfaces help ensure that different classes provide the same functionality, making code more flexible and consistent.
- In Python, interfaces are often created using abstract base classes (`abc` module).

### ✅ Example:


```python
# imports needed for abstract classes
from abc import ABC, abstractmethod

# interface contact. Children will have to implement
# all of the abstract methods. In an interface methods
# have no implementation and add pass

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle.")

class Square(Drawable):
    def draw(self):
        print("Drawing a square.")
```

```

+--------------------------------+
|          <<interface>>         |
|            Drawable            |
+--------------------------------+
| + draw(): void                 |
+--------------------------------+
      ^                  ^           
      |                  |
      |                  |   
      |                  |
      +----------        +--------------
                |                       |
                |                       |
+----------------------------+   +----------------------------+
|             Circle         |   |             Square         |
+----------------------------+   +----------------------------+   
+----------------------------+   +----------------------------+
| << create >>+Circle        |   | << create >>+Square        |
| + draw(): void             |   | + draw(): void             |
+----------------------------+   +----------------------------+

```

### 🎭 Abstract 
- An abstract class is a class that cannot be used on its own and is meant to be inherited by other classes.
- In many cases, an abstract class is used to define shared functionality beyond just method signatures that can be inherited and extended by its subclasses.

### ✅ Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    # Concrete method shared by all sub class
    def start_engine(self):
        print("Engine started.")

    #Abstract method — must be implemented by all subclasses
    @abstractmethod
    def drive(self):
        pass
    
    # Default behavior — can be overridden
    def fuel_type(self):
        print("Uses gasoline.") 

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")
    # Inherits fuel_type() from Vehicle (no need to override)

class Truck(Vehicle):
    def drive(self):
        print("Truck is hauling.")

    # Overrides the default method
    def fuel_type(self):
        print("Uses diesel.")
    

car = Car()
truck = Truck()

car.start_engine()   # Inherited from Vehicle
car.drive()          # Must be implemented in subclass

truck.start_engine()
truck.drive()
```
```
+--------------------------------+
|          <<abstract>>           |
|            Vehicle             |
+--------------------------------+
| + start_engine(): void          |
| + fuel_type(): void             |
| + drive(): void <<abstract>>    |
+--------------------------------+
      ^                        ^
      |                        |
+--------------------+   +--------------------+
|        Car         |   |       Truck        |
+--------------------+   +--------------------+
| + drive(): void    |   | + drive(): void    |
|                    |   | + fuel_type(): void|  
+--------------------+   +--------------------+
```