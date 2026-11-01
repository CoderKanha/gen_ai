import numpy as np
array_one = np.array([10, 20, 30, 40])
array_two = np.array([1, 2, 3, 4])

# Mathametical operations
addition = array_one + array_two
subtraction = array_one - array_two
multiplication = array_one * array_two
division = array_one / array_two
square = array_one ** 2

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Square:", square)

# Optional: Use numpy functions for these operations
print("Addition (using np.add):", np.add(array_one, array_two))
print("Subtraction (using np.subtract):", np.subtract(array_one, array_two))
print("Multiplication (using np.multiply):", np.multiply(array_one, array_two))
print("Division (using np.divide):", np.divide(array_one, array_two))
print("Square (using np.square):", np.square(array_one))