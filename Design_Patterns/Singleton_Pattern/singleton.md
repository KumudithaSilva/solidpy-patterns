# 🔁💡 Singleton Design Pattern


> Singleton is a creational design pattern that ensures a class has only one
> instance and provides a global point of access to that instance.
> 
> The Singleton pattern does not specify how the instance should be utilized, 
> allowing flexibility and creativity in its implementation.

> This is one of GoF patterns:
> 
> It's important for some classes to have exactly one instance although there can be many 
> requests to access it, they should all refer to the same shared instance.


### Singleton Design Pattern
<br>
<img src= /assets/images/Singleton.jpg alt="img" width="500px" />

  
## 🎯 Key Points

### ✅ Singleton Design Pattern

- Guarantees a single instance throughout the application.
- Provides a global access point to that instance.
- Useful when exactly one object is needed to coordinate actions across a system.

### 💻 Use Cases

- Logging 
- Caching
- Configuration settings
- Database connections
- Thread pools

### 🧩 Benefits

- Controlled access to the sole instance
- Reduces memory footprint
- Can be extended to support lazy initialization

### 📌 When to Use

- When a single point of control or coordination is needed
- When a global state is needed across components

### ⚠️ When Not to Use

- When it introduces hidden dependencies, making the code harder to maintain.
- When it becomes just a global access point for everything.

### 🛠️ Design Considerations

- Thread Safety - to avoid creating multiple instances.
- Lazy vs. Eager Initialization - Create the instance only when needed (lazy) or at startup (eager)

