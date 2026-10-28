# Task 1 - Testing math_utils function
import math_utils
from math_utils import square

print(f"Addition of 4 & 5: {math_utils.add(4, 5)}")
print(f"Subtraction of 4 & 5: {math_utils.subtract(4, 5)}")
print(f"Square of 4: {square(4)}")


# Task 2 - Testing string_utils funtion
import string_utils
from string_utils import word_count

word = "learning gen_ai"
print(f"Capitalize word - {word}: {string_utils.capitalize_words(word)}")
print(f"Reverse word - {word}: {string_utils.reverse_string(word)}")
print(f"Count characters in word - {word}: {word_count(word)}")

# Task 3 - Created the shop package with billing and discount files

# Task 4 - Importing package
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print(f"Apply 10% discount: {disc.apply_discount(100, 10)}")
print(f"Apply flat discount: {disc.flat_discount(100)}")
print(f"Calculate total price: {calculate_total([100, 200, 300])}")
print(f"Apply tax on purchase amount: {apply_tax(600)}")