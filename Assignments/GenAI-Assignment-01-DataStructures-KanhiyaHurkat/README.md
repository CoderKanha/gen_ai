# Python Product Catalog – Data Structures

## Overview

This project demonstrates the use of fundamental Python data structures through a product catalog example. It consists of four Python scripts that cover lists, tuples, sets, and dictionaries, along with operations such as adding, updating, removing, searching, grouping, and analyzing product data.

## Project Structure

```text
.
├── task1.py    # List and Tuple Operations
├── task2.py    # Set Operations
├── task3.py    # Dictionary Operations
├── task4.py    # Product Catalog and Category Analysis
└── README.md  # Project Documentation
```

## Requirements

- Python 3.x
- No external libraries are required.

## Tasks and Concepts

### Task 1: List and Tuple Operations (`task1.py`)

This script demonstrates basic operations on Python lists and tuples.

**Operations performed:**
- Creates a list containing six products: Laptop, Photo Frame, Pasta, T-shirt, Sofa, and Specs.
- Creates a tuple containing a product name, price, and category.
- Accesses products using positive and negative indexing.
- Adds new products to the list using `append()`.
- Converts a tuple into a list to update the product price.
- Converts the modified list back into a tuple.
- Displays the type of the resulting tuple.

**Key concepts:** Lists, tuples, indexing, `append()`, type conversion, and mutability.

### Task 2: Set Operations (`task2.py`)

This script demonstrates how Python sets store unique values.

**Operations performed:**
- Creates a set of product categories.
- Adds a new category, Cosmetics.
- Attempts to add Furniture again to demonstrate that duplicate values are ignored.
- Checks whether Electronics exists in the set.
- Counts the number of unique categories using `len()`.

**Key concepts:** Sets, uniqueness, `add()`, membership operators, and `len()`.

**Note:** Sets are unordered collections, so their printed element order may vary.

### Task 3: Dictionary Operations (`task3.py`)

This script manages product prices using a dictionary, where product names are keys and prices are values.

**Operations performed:**
- Creates a dictionary containing product names and their prices.
- Adds a new product, Monitor, with its price.
- Updates the price of Laptop.
- Checks for Specs and removes it from the dictionary when found.
- Calculates the total price of the remaining products.
- Calculates the average price.
- Identifies the products with the minimum and maximum prices.

**Key concepts:** Dictionaries, key-value pairs, adding and updating entries, `get()`, `pop()`, loops, aggregation, `min()`, and `max()`.

**Note:** The average is calculated using the total of the remaining product prices divided by the number of remaining dictionary entries.

### Task 4: Product Catalog and Category Analysis (`task4.py`)

This script combines multiple data structures to build and analyze a product catalog.

**Operations performed:**
- Creates a list of ten products.
- Creates a set of product categories.
- Stores product prices in a dictionary.
- Maps each product to its corresponding category using another dictionary.
- Builds a catalog as a list of tuples containing the product name, price, and category.
- Groups products by category using a dictionary.
- Identifies the category containing the largest number of products.
- Prints the products belonging to that category.

**Key concepts:** Lists, sets, dictionaries, tuples, dictionary lookups, loops, conditional statements, data grouping, and counting.

**Expected category analysis:** Furniture contains the largest number of products, with three items: Sofa, Cupboard, and Chair.

## How to Run

1. Install Python 3.x if it is not already installed.
2. Download or clone the project repository.
3. Open a terminal or command prompt in the project folder.
4. Run each script separately using Python.

### Execution Commands

```bash
python task1.py
python task2.py
python task3.py
python task4.py
```

On systems where Python 3 is invoked using `python3`, use `python3` instead of `python`.

## Expected Results

Each script prints its results to the terminal.

| Script | Expected output |
|---|---|
| `task1.py` | Selected products, updated product list, and tuple type |
| `task2.py` | Category set, Electronics membership result, and unique category count |
| `task3.py` | Product removal confirmation, average price, and minimum- and maximum-priced product names |
| `task4.py` | Product catalog, products grouped by category, and the products in the largest category |

The exact output of the set operation may vary because sets do not guarantee element order.

## Learning Outcomes

After completing these tasks, you should understand how to:

- Create and manipulate Python lists and tuples.
- Understand the difference between mutable lists and immutable tuples.
- Use sets to maintain unique values.
- Store and manage data using dictionaries.
- Add, update, and remove dictionary entries.
- Iterate over collections and perform calculations.
- Combine multiple data structures to represent a product catalog.
- Group records by category and identify the category with the highest number of products.

## Conclusion

This project provides practical examples of Python's built-in data structures using a common product catalog scenario. Each script introduces specific operations, while the final script combines these concepts to organize, group, and analyze product information.

The project is suitable for beginners learning Python fundamentals and practicing data manipulation without external libraries.