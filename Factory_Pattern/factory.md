# 🏭💡 Factory Method Design Pattern


> Factory Method is a creational design pattern that abstracts out the creation logic of the specific class instances.

> It is a way to create objects without exposing the instantiation logic. 
 >- In Factory Pattern objects are created by calling factory method instead of calling a constructor.
 >
> 
 >- Creation logic is encapsulated, promoting abstraction and loose coupling.
 >
> 
 >- To create objects, it used a common interface.

>Defines an interface for creating objects,
> but lets subclasses decide which concrete product class to use.

> This is one of GoF patterns:



### Factory Method Design Pattern
<br>
<img src=../images/Factory_Method.png alt="img" width="500px" />

  
## 🎯 Key Points

### ✅ Factory Method Design Pattern

- Provides a way to delegate instantiation to subclasses.
- Promotes programming to an interface, not an implementation.
- Decouple object creation from object usage.

### 💻 Use Cases

- GUI frameworks (e.g., createButton() may return WindowsButton or MacButton).
- Document editors (different document parsers for XML, JSON, etc.). 
- Payment gateways (factory method chooses PayPal, Wire, etc.). 
- Connection providers (different DB connections: MySQL, PostgreSQL, etc.).

### 🧩 Benefits

- It allows subclass to choose the type of objects to create.
- It promotes loose-coupling.
- It promotes Single responsibility principal 
  - Can move creation code into one place.
- It promotes Open/Closed principal
  - can introduce new subtypes without breaking existing code.

### 📌 When to Use

- When a caller can't anticipate the type of objects it must create.
- When having many objects of a common type.

### ⚠️ When Not to Use

- When only need one object. 
- When object creation is simple and unlikely to change.

### 🛠️ Design Considerations

- Factory Method only when object creation logic varies.
- GoF Factory Method vs. Simple Factory - object creation is centralized in a single method (Simple Factory), 
while subclasses decide which class to instantiate (Factory Method, GoF).

