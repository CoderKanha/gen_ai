import numpy as np

one_dimensional_array = np.arange(1, 11)
two_dimensional_array = np.arange(1, 10).reshape(3, 3)
dummy_list = [10, 20, 30, 40, 50]
dummy_array = np.array(dummy_list)

# Shape of the arrays
print("Shape of one-dimensional array:", one_dimensional_array.shape)
print("Shape of two-dimensional array:", two_dimensional_array.shape)
print("Shape of dummy array:", dummy_array.shape)

# Data type of the arrays
print("Data type of one-dimensional array:", one_dimensional_array.dtype)
print("Data type of two-dimensional array:", two_dimensional_array.dtype)
print("Data type of dummy array:", dummy_array.dtype)