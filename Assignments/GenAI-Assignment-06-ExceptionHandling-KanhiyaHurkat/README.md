# Python Exception Handling Practice

A set of five small Python programs that demonstrate exception handling: `try`, `except`, `else`, `finally`, and raising custom errors with `raise`.

## Project Structure

```
.
├── task1.py   # Safe Division Utility
├── task2.py   # Bill Calculator with Error Handling
├── task3.py   # Custom Exception: Age Validator
├── task4.py   # File Reader with Exception Handling
└── task5.py   # Mini Program: Safe Shopping Cart
```

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies

## Running a Task

Run any task from the project folder:

```bash
python task1.py
```

---

## Task 1: Safe Division Utility (`task1.py`)

Takes a numerator and denominator from the user and divides them safely.

| Block | Behavior |
|-------|----------|
| `try` | Reads both inputs as floats and divides them |
| `except ValueError` | Handles input that is not a number |
| `except ZeroDivisionError` | Handles a denominator of `0` |
| `else` | Prints the result if no error occurred |
| `finally` | Always prints `Operation Complete` |

**Example runs**

```
Enter the numerator: 10
Enter the denominator: 4
Result: 2.5
Operation Complete
```

```
Enter the numerator: 10
Enter the denominator: 0
Error: Denominator cannot be zero.
Operation Complete
```

---

## Task 2: Bill Calculator with Error Handling (`task2.py`)

Iterates through the list `[120, 350, 'abc', 500, -200, 800]` and adds only valid (positive, numeric) prices to the total. Invalid items are skipped and processing continues.

- **`TypeError`**: caught when a value is not a number (e.g. `'abc'`)
- **`ValueError("Negative price not allowed")`**: raised manually for negative prices and caught by `except ValueError`
- The running total is printed after each valid price

**Output**

```
Added 120 | Running total: 120
Added 350 | Running total: 470
Skipped 'abc': not a number
Added 500 | Running total: 970
Skipped -200: Negative price not allowed
Added 800 | Running total: 1770

Final total: 1770
```

---

## Task 3: Custom Exception: Age Validator (`task3.py`)

Defines `check_age(age)`, which raises `ValueError("Age must be between 1 and 120")` when the age is outside the range. The main code reads the age from the user, validates it, and prints the error message if validation fails.

**Example runs**

```
Enter your age: 25
Valid age: 25
```

```
Enter your age: 150
Age must be between 1 and 120
```

> **Note:** If the user enters non-numeric text, `int()` raises its own `ValueError`, so Python's default message is printed instead of the custom one.

---

## Task 4: File Reader with Exception Handling (`task4.py`)

Asks for a filename, then tries to open it and print its first 3 lines.

| Block | Behavior |
|-------|----------|
| `try` | Opens the file and reads all lines |
| `except FileNotFoundError` | Prints a "file not found" message |
| `except PermissionError` | Prints a "permission denied" message |
| `else` | Prints the first 3 lines of the file |
| `finally` | Always prints `File operation attempted.` |

**Example run (missing file)**

```
Enter the filename: missing.txt
Error: File 'missing.txt' not found.
File operation attempted.
```

---

## Task 5: Mini Program: Safe Shopping Cart (`task5.py`)

Keeps asking the user for prices and stores them in a `cart` list until the user enters `q`.

- Each entry is converted to a `float`
- **Invalid input** (e.g. `abc`) prints a "valid number" message and the loop continues
- **Negative prices** raise `ValueError("Negative price not allowed")`, and the price is not added
- When the user quits, the program prints the total items and the total bill

**Example run**

```
Enter price (or 'q' to quit): 100
Added 100.0
Enter price (or 'q' to quit): abc
Error: Please enter a valid number.
Enter price (or 'q' to quit): -50
Error: Negative price not allowed
Enter price (or 'q' to quit): 250.5
Added 250.5
Enter price (or 'q' to quit): q

Total items: 2
Total bill: 350.5
```

---

## Concepts Covered

- `try` / `except` / `else` / `finally`
- Handling multiple exception types
- Raising exceptions with `raise`
- `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, `PermissionError`
- Input validation inside loops