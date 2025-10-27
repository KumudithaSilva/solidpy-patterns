# 🔌💡 Adapter Design Pattern


> The Adapter is a structural design pattern that allows objects 
> with incompatible interfaces to work together by converting one class’s 
> interface into another that the client expects.

> It can take two different elements into account
> 
 >- Adapter can convert source data to another formate that client expects.
 >
 > <p align="center"><img src="/assets/images/Adapter_data.png" alt="img" width="250px"/> </p>
> 
 >- Adapter can collaborate with different incompatible interfaces.
 >
 > <p align="center"><img src="/assets/images/Adapter_interface.png" alt="img" width="250px"/> </p>



> This is one of GoF patterns:



### Adapter Design Pattern
<br>
<img src= /assets/images/Adapter_Method.png alt="img" width="500px" />

  
## 🎯 Key Points

### ✅ Adapter Design Pattern

- Adaptee - It is the service that want to use
- ITarget - It is our own service
- Adapter - It is the wrapper which allow the seamless conversion

### 💻 Use Cases

- Integrating legacy code with new systems without modifying existing code.
- Making third-party libraries compatible with app’s interfaces.
- Converting different data formats or APIs into a common structure.
- Bridging between different interface contracts, e.g., old and new versions of a service.

### 🧩 Benefits

- It can separate data conversion
- Adapter introduced without breaking existing code or changing client classes.
- Separates data conversion and compatibility logic from business logic.
- Promotes reusability by allowing existing classes to be reused with new interfaces.
- Makes the system more flexible and extensible for future integrations.


### 📌 When to Use

- Use it if the class that want to use incompatible 
- Reuse existing functionality but the API or interface doesn’t match the new design.


### ⚠️ When Not to Use

- System is time-sensitive add adapter will over-head it then don't use it.
- Overusing adapters can make the system complex or hard to trace.


### 🛠️ Design Considerations

- Keep adapters lightweight and focused only on interface translation.
- Ensure the adapter doesn’t change the expected behavior of the adapted class.

