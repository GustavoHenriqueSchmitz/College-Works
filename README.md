# College-Works
A set of challenges and projects I worked on while studying subjects at college.

## Programming Logic and Algorithms (Python Challenges)
### **1. Wholesale Discount System**
- **Goal:** Calculate discounts (0% to 11%) based on the total purchase value [cite: 26, 28-31].
- **Key Concepts:** Input handling, logical operators (`<`, `>=`), `if/elif/else` structures, and formatted output [cite: 34-37].

### **2. Açaí & Cupuaçu Shop Interface**
- **Goal:** Create a console ordering menu for specific flavors and sizes with input validation [cite: 54, 61-64].
- **Key Concepts:** Nested conditions, accumulators for total order price, and control flow using `while`, `break`, and `continue`[cite: 65, 66, 69].

### **3. Photocopy Service Calculator**
- **Goal:** Calculate costs for different printing services (Digitization, Color, B&W) with volume-based discounts and extra binding services [cite: 89, 93-104].
- **Key Concepts:** Modular programming with specific functions (`escolha_servico`, `num_pagina`, `servico_extra`) and error handling via `try/except`[cite: 109, 113, 117, 122].

### **4. Book Management Software**
- **Goal:** Develop a CRUD system to Register, Consult (by All, ID, or Author), and Remove books [cite: 142, 145-151].
- **Key Concepts:** Data structures (lists of dictionaries), global ID management, and menu-driven architecture[cite: 155, 172, 180].

## Object-Oriented Programming (Java Challenge)

### Java Coin Piggy Bank

#### **Project Overview**
* **Goal:** Develop a system to emulate a "Piggy Bank" that manages coins from different countries (Real, Dollar, Euro).
* **Key Concepts:** Practical application of **Inheritance** and **Polymorphism** using an abstract base class (`Moeda`) and concrete implementations.

#### **Functional Requirements**
* **Menu System:** Create an interactive console menu with the following options:
    1.  **Add Coins:** Support multiple currencies and values.
    2.  **Remove Coins:** Ability to remove specific coin instances.
    3.  **List Coins:** Display all coins currently inside the piggy bank.
    4.  **Calculate Total:** Convert the value of all foreign coins to Real (BRL) and display the total sum.

#### **Technical Architecture (UML)**
* **Class Structure:**
    * `Cofrinho`: Manages a collection (e.g., `ArrayList`) of coins with methods to add, remove, list, and calculate total.
    * `Moeda` (Abstract): Defines the contract for `info()` and `converter()`.
    * **Subclasses:** `Dolar`, `Euro`, `Real` inherit from `Moeda` and implement specific conversion logic.
