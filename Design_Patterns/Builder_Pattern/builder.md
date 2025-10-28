# 🏗️ Builder Design Pattern


> Builder is a creational design pattern that encapsulate reusable logic of complex object.
>   
> Complex object means - Objects that are made up with many distinct parts.

> It separates the construction of a complex objects from its representation and same constructor can
> create different representations.

> Builder does not allow objects to create itself to user, it abstracts the creational process.

> Builder is an object able to construct other objects.



### Builder Design Pattern
<br>
<img src= /assets/images/Class_Diagram.png alt="img" width="700px" />

  
## 🎯 Key Points

### ✅ Builder Design Pattern

- Separates object construction from its representation.
- The same construction process can create different objects.
- Constructs complex objects step-by-step.

### 💻 Use Cases

- Document Parsers: Build documents in PDF, HTML, or Markdown formats.
- Meal Builders: Construct meals with different food items (e.g., in a fast-food ordering system).

### 🧩 Benefits

- Separation of Concerns: Construction logic is kept separate from the object’s representation.
- Better Code Readability: Especially useful for objects with many optional parameters.
- Promotes SOLID Principles:
  - Single Responsibility Principle (SRP): Construction logic is in one place. 
  - Open/Closed Principle (OCP): Add new builders without modifying existing ones.
- Improves Testability: Builders can easily produce test objects with specific configurations.

### 📌 When to Use

- An object has a large number of fields or optional parameters.
- You need to create different representations of a complex object.
- Object construction involves many steps or conditional logic.
- Reuse the same building process to create different configurations.

### ⚠️ When Not to Use

- Object creation is simple and has no complex logic. 
- Only one type of object needs to be created.

### 🛠️ Design Considerations

- Use Director if construction logic is reusable across different builders.
- A distinct concrete builder must be created for each type of objects.

