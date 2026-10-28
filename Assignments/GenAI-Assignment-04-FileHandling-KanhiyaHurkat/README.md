# Python File Handling Practice

A collection of seven small Python scripts that demonstrate core file-handling concepts: writing, reading, appending, processing data, handling user input, validating file paths, and generating reports.

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Task Descriptions](#task-descriptions)
- [Generated Files](#generated-files)
- [Concepts Covered](#concepts-covered)
- [Notes](#notes)

## Requirements

- Python 3.6 or higher (uses f-strings)
- No third-party packages required (only the standard library, including `os`)

## Project Structure

```
.
├── task1.py   # Write sales data to files
├── task2.py   # Read file content in different ways
├── task3.py   # Append data and count lines
├── task4.py   # Sales statistics from a file
├── task5.py   # Build a product list from user input
├── task6.py   # Read a file by name given by the user
├── task7.py   # Discount report generator
└── README.md
```

## How to Run

Run each script from the same folder so the generated files are created and found in the right place:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
python task6.py
python task7.py
```

> **Important:** Tasks 2, 3 and 4 depend on `sales_data.txt`, which is created by Task 1. Run `task1.py` first.

## Task Descriptions

### Task 1: Writing Data to a File

Writes a list of dummy sales figures (`[1200, 450, 980, 1500, 3000]`) to `sales_data.txt`, one value per line, and then reads the file back and prints it.

**Optional part:** writes the same figures to `new_sales_data.txt`, separated by commas, and prints the result.

| Mode | Purpose |
|------|---------|
| `'w'` | Create/overwrite the file and write data |
| `'r'` | Read the file back |

**Output files:** `sales_data.txt`, `new_sales_data.txt`

---

### Task 2: Reading Data from a File

Reads `sales_data.txt` using three different methods:

1. `read()`: prints the complete file content as a single string
2. `readline()`: prints only the first line
3. `readlines()`: loads every line into a list of integers (newlines stripped and values converted with `int()`)

**Requires:** `sales_data.txt` (from Task 1)

---

### Task 3: Appending Data to a File

Appends three new sales values (`[5000, 2500, 1700]`) to the existing `sales_data.txt` using append mode (`'a+'`), then prints the updated content.

**Optional part:** counts and prints the total number of lines in the file using `len(readlines())`.

**Requires:** `sales_data.txt` (from Task 1)

---

### Task 4: Sales Data Analysis

Reads all sales figures from `sales_data.txt` into a list and calculates:

- Total sales
- Highest sale
- Lowest sale
- Average sale

**Requires:** `sales_data.txt` (from Task 1)

**Sample output** (after Task 1 only):

```
Sales data: [1200, 450, 980, 1500, 3000]
Total Sales: 7130
Highest Sales: 3000
Lowest Sales: 450
Average Sales: 1426.0
```

---

### Task 5: Product List from User Input

Prompts the user to enter the name and price of **3 products** and saves them to `products.txt` with a header row (`Product Name | Price`). The file is then read back and displayed.

- The price must be an integer; otherwise an error message is shown and the user is asked to re-enter the product.
- After each valid entry, the script tells the user how many more products are needed.

**Output file:** `products.txt`

**Sample session:**

```
Enter product name: Laptop
Enter product price: 55000
Add 2 more product
Enter product name: Mouse
Enter product price: abc
Product price should be integer
Enter product name: Mouse
Enter product price: 500
Add 1 more product
...
```

---

### Task 6: Read a File by Name

Asks the user for a file name, then looks for that file in the **same folder as the script** (using `os.path.dirname(os.path.abspath(__file__))` and `os.path.join`).

- If the file exists, its content is printed.
- If not, the message `File not found. Please check the filename.` is displayed.

**Example:** entering `sales_data.txt` prints the sales data written by Task 1.

---

### Task 7: Discount Report Generator

Uses a dictionary of products and their prices:

| Product | Price |
|---------|-------|
| Mouses | 500.00 |
| Keyboard | 800.00 |
| Monitor | 7000.00 |
| Pendrive | 400.00 |
| Cameras | 5000.00 |

The user enters a discount percentage (integer). The script then:

1. Rejects any value above the **maximum allowed discount of 30%**
2. Calculates the discounted price for every product
3. Appends a formatted report to `discount_report.txt` with the original price and discounted price of each item
4. **Optional:** adds the total number of items and the average discounted price

Non-integer input is caught and reported with `Value must be integer`.

**Output file:** `discount_report.txt` (opened in append mode, so repeated runs add new reports to the end of the file)

## Generated Files

| File | Created by | Description |
|------|-----------|-------------|
| `sales_data.txt` | Task 1 (extended by Task 3) | Sales figures, one per line |
| `new_sales_data.txt` | Task 1 | Sales figures, comma-separated |
| `products.txt` | Task 5 | Product names and prices |
| `discount_report.txt` | Task 7 | Discounted price report |

## Concepts Covered

- Opening files with the `with` statement (context manager)
- File modes: `'w'`, `'r'`, `'a'`, `'a+'`
- Reading with `read()`, `readline()` and `readlines()`
- Writing with `write()` and formatted f-strings
- Cleaning data with `strip()` and converting types with `int()`
- Aggregations with `sum()`, `max()`, `min()` and `len()`
- User input with `input()` and validation using `try`/`except`
- Working with paths using the `os` module (`os.path.exists`, `os.path.join`, `os.path.abspath`)
- Iterating over dictionaries with `.items()`

## Notes

- The `with` statement closes files automatically, so the explicit `file.close()` calls in the scripts are redundant (though harmless).
- Task 1 uses `'w'` mode, so re-running it resets `sales_data.txt` to its original five values, undoing any data appended by Task 3.
- Task 3 appends to `sales_data.txt` each time it runs, so running it multiple times adds duplicate entries.
- Task 7 uses a bare `except:`, so any error (not just invalid input) triggers the "Value must be integer" message. Catching `ValueError` specifically would be more precise.
- Task 7 does not reject negative discount percentages; only the upper limit is enforced.