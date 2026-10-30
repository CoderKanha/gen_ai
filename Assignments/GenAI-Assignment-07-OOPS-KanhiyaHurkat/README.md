# Python OOP Practice

A set of seven Python programs that build up object-oriented programming concepts step by step, using a `Product` class as the running example: classes and objects, encapsulation, inheritance, polymorphism, abstraction, magic methods, and a small inventory system.

## Project Structure

```
.
├── task1_1.py   # Classes and objects
├── task2_1.py   # Encapsulation (getter and setter)
├── task3_1.py   # Inheritance
├── task4_1.py   # Polymorphism
├── task5_1.py   # Abstraction (abstract base class)
├── task6.py     # Magic methods and operator overloading
└── task7.py     # Mini project: Store and Inventory system
```

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## Running a Task

Run any task from the project folder:

```bash
python task1_1.py
```

---

## Task 1: Classes and Objects (`task1_1.py`)

Defines a `Product` class with `name`, `price`, and `category` attributes.

| Method | Description |
|--------|-------------|
| `get_info()` | Prints the product's name, price, and category |
| `apply_discount(percent)` | Prints the price after applying the percentage discount |

Two objects are created (a Laptop and a Sofa) and both methods are called on each.

**Output**

```
This is a Laptop. It's price is 500000 and it comes under Electronics category.
Discounted price for Laptop: 400000.0
This is a Sofa. It's price is 10000 and it comes under Furniture category.
Discounted price for Sofa: 9000.0
```

---

## Task 2: Encapsulation (`task2_1.py`)

Extends `Product` with accessor methods instead of reading the price directly.

| Method | Description |
|--------|-------------|
| `get_price()` | Returns the current price |
| `set_price(price)` | Updates the price only if the new price is greater than 0 |

The Laptop's `set_price(-10000)` call is ignored because the value is not positive, while the Sofa's `set_price(4000)` is accepted.

**Output**

```
This is a Laptop. It's price is 500000 and it comes under Electronics category.
This is a Sofa. It's price is 4000 and it comes under Furniture category.
```

---

## Task 3: Inheritance (`task3_1.py`)

Adds an `ElectronicProduct` class that inherits from `Product`.

- Calls `super().__init__()` to reuse the parent constructor
- Adds a new `warranty_years` attribute
- Overrides `get_info()` to include the warranty
- Inherits `apply_discount()` unchanged

**Output**

```
This is a Laptop and it has 3 years of warranty.
Discounted price for Laptop: 450000.0
```

---

## Task 4: Polymorphism (`task4_1.py`)

Creates two subclasses of `Product`, `Laptop` and `Mobile`, each with its own version of `get_info()`. A list containing both types is looped over, and the same `get_info()` call produces different output depending on the object type.

**Output**

```
This is HP laptop with 21 inch screen. Its price is $5000 and 3 years warranty.
This is Motorola mobile with 9 inch screen. Its price is $300 and 1 years warranty.
This is Dell laptop with 21 inch screen. Its price is $6500 and 4 years warranty.
This is Asus mobile with 9 inch screen. Its price is $250 and 2 years warranty.
```

---

## Task 5: Abstraction (`task5_1.py`)

Uses Python's `abc` module to define an abstract base class.

- `Payment` is an abstract class with the abstract method `process_payment(amount)`
- `CreditCardPayment` and `UPIPayment` are subclasses that must implement it
- `Payment` itself cannot be instantiated

**Output**

```
Payment of ₹1000 processed using Credit Card.
Payment of ₹500 processed using UPI.
```

---

## Task 6: Magic Methods and Operator Overloading (`task6.py`)

A `Product` class that customizes built-in behavior.

| Magic method | Description |
|--------------|-------------|
| `__str__` | Returns a readable string, used by `print()` |
| `__add__` | Overloads `+` so adding two products returns the sum of their prices |

**Output**

```
Product(Laptop, 50000, Electronics)
Product(Mobile, 20000, Electronics)
Total combined price: 70000
```

---

## Task 7: Mini Project: Store and Inventory System (`task7.py`)

Combines several classes to model a simple store.

| Class | Responsibility |
|-------|----------------|
| `Product` | Holds a name and price, with `__str__` and `__add__` |
| `Inventory` | Stores products with `add_product()`, `remove_product(name)`, `get_total_value()`, and `show_all_products()` |
| `Store` | Owns an `Inventory`, takes product details from the user with `add_new_product()`, and prints a summary with `show_summary()` |

`add_new_product()` keeps asking until a valid integer price is entered. The test code adds three products, displays them, shows the summary, and then uses `+` to print the combined price of the first two products.

**Example run**

```
Enter product name: Rice
Enter product price: 50
Rice added successfully.
Enter product name: Milk
Enter product price: 30
Milk added successfully.
Enter product name: Bread
Enter product price: 25
Bread added successfully.
Product name is Rice and it's price is 50.
Product name is Milk and it's price is 30.
Product name is Bread and it's price is 25.
There are total 3 items in inventory and total value is 105

Combined price of Rice and Milk: ₹80.00
```

If a non-numeric price is entered, the program prints `Product price should be valid number` and asks again.

---

## Notes

- In Tasks 2 to 4, the constructor parameter is named `__price`, but the value is stored in the public attribute `self.price`, so it is not truly private. For real encapsulation, store it as `self.__price` (or `self._price`) and access it only through `get_price()` and `set_price()`.
- In Task 7, `remove_product()` is defined but not called by the test code.

## Concepts Covered

- Classes, objects, and constructors (`__init__`)
- Encapsulation with getters and setters
- Inheritance and `super()`
- Method overriding and polymorphism
- Abstract base classes (`ABC`, `@abstractmethod`)
- Magic methods (`__str__`, `__add__`) and operator overloading
- Composition (a `Store` has an `Inventory`, which holds `Product` objects)