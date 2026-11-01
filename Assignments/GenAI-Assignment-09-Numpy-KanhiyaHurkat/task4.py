import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Aggregate operations
row_sum = np.sum(data, axis=1)
column_sum = np.sum(data, axis=0)
min_value = np.min(data)
max_value = np.max(data)
mean_value = np.mean(data)

# Optional
row_wise_min = np.min(data, axis=1)
row_wise_max = np.max(data, axis=1)
column_wise_min = np.min(data, axis=0)
column_wise_max = np.max(data, axis=0)

# Display the results
print("Row-wise Sum:", row_sum)
print("Column-wise Sum:", column_sum)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Mean Value:", mean_value)
print("Row-wise Minimum:", row_wise_min)
print("Row-wise Maximum:", row_wise_max)
print("Column-wise Minimum:", column_wise_min)
print("Column-wise Maximum:", column_wise_max)