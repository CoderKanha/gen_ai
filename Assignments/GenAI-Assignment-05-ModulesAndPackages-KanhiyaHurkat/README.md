# Python Utilities & Shop Package Demo

A small Python project demonstrating modules, imports, and packages. It includes math and string utility modules, a `shop_package` package for billing and discounts, and a `main.py` script that exercises everything.

## Project Structure

```
.
├── main.py
├── math_utils.py
├── string_utils.py
└── shop_package/
    ├── billing.py
    └── discount.py
```

> **Note:** `main.py` imports from `shop_package`, so `billing.py` and `discount.py` must be placed inside a `shop_package/` folder (add an empty `__init__.py` file there if your Python setup requires it).

## Modules

### `math_utils.py`

| Function | Description |
|----------|-------------|
| `add(a, b)` | Returns the sum of two numbers |
| `subtract(a, b)` | Returns the difference of two numbers |
| `square(n)` | Returns the square of a number |

### `string_utils.py`

| Function | Description |
|----------|-------------|
| `capitalize_words(text)` | Capitalizes each word in the string |
| `reverse_string(text)` | Returns the reversed string |
| `word_count(text)` | Returns the total number of words in the string |

### `shop_package/billing.py`

| Function | Description |
|----------|-------------|
| `calculate_total(prices)` | Returns the sum of all prices in a list |
| `apply_tax(amount)` | Adds 5% tax to the given amount |

### `shop_package/discount.py`

| Function | Description |
|----------|-------------|
| `apply_discount(price, percent)` | Applies a percentage discount to the price |
| `flat_discount(price)` | Subtracts a flat 50 rupees from the price |

## Usage

Run the demo script from the project root:

```bash
python main.py
```

### What `main.py` does

1. **Task 1** – Tests the `math_utils` functions (`add`, `subtract`, `square`)
2. **Task 2** – Tests the `string_utils` functions (`capitalize_words`, `reverse_string`, `word_count`)
3. **Task 3** – Creates the `shop_package` package with the billing and discount modules
4. **Task 4** – Imports the package and tests its functions

### Example Output

```
Addition of 4 & 5: 9
Subtraction of 4 & 5: -1
Square of 4: 16
Capitalize word - learning gen_ai: Learning Gen_Ai
Reverse word - learning gen_ai: ia_neg gninrael
Count characters in word - learning gen_ai: 2
Apply 10% discount: 90.0
Apply flat discount: 50
Calculate total price: 600
Apply tax on purchase amount: 630.0
```

## Import Examples

```python
# Importing a whole module
import math_utils
math_utils.add(4, 5)

# Importing a specific function
from string_utils import word_count
word_count("hello world")

# Importing from a package
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax
```

## Requirements

- Python 3.6+ (uses f-strings)
- No external dependencies