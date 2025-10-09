# 🌟 SOLID Principles of OOP

The SOLID principles are five design principles intended to make software designs more understandable, flexible, and maintainable.

---

## 📌 What is SOLID?

**SOLID** is a set of five design principles in object-oriented programming. These principles help create code that is easier to understand, maintain, and scale.


---

## 🚀 Why SOLID Matters?

✅ Easier to maintain  
✅ Highly scalable  
✅ Encourages reusable code  
✅ Supports clean architecture  
✅ Promotes OOP best practices

---

## 1️⃣ Single Responsibility Principle (SRP)  
> **A class should have one, and only one, reason to change.**  
📦 Each class should focus on a single task or functionality.

✅ *Example:*  
A `UserManager` class should only handle user-related logic — not file operations, logging, or payment handling.

---

## 2️⃣ Open/Closed Principle (OCP)  
> **Software should be open for extension, but closed for modification.**  
🚪 New features can be added by extending existing code, without changing the original implementation.

✅ *Example:*  
A new `PaypalPayment` class can be created and used without modifying the existing `PaymentProcessor` class.
---

## 3️⃣ Liskov Substitution Principle (LSP)  
> **Subtypes must be substitutable for their base types.**  
🔁 Objects of a derived class should behave the same as objects of the base class.

✅ *Example:*  
A `Square` class should behave correctly when used in place of a `Rectangle` without causing unexpected issues.

---

## 4️⃣ Interface Segregation Principle (ISP)  
> **No client should be forced to depend on methods it does not use.**  
✂️ Create smaller, more specific interfaces rather than one large interface.

✅ *Example:*  
Use separate interfaces like `IPrinter`, `IScanner`, and `IFax` instead of one big `IMachine` interface.

---

## 5️⃣ Dependency Inversion Principle (DIP)  
> **Depend on abstractions, not concretions.**  
🔌 High-level modules shouldn’t depend on low-level modules. Both should depend on abstractions (e.g., interfaces).

✅ *Example:*  
A `ReportService` depends on an `IPrinter` interface, not a concrete `HPPrinter` class.


