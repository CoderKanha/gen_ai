import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# Statistical operations
mean_marks = np.mean(marks)
median_marks = np.median(marks)
variance_marks = np.var(marks)
standard_deviation_marks = np.std(marks)
min_marks = np.min(marks)
max_marks = np.max(marks)
range_marks = np.ptp(marks)

# Display the results
print("Mean Marks:", mean_marks)
print("Median Marks:", median_marks)
print("Variance Marks:", variance_marks)
print("Standard Deviation Marks:", standard_deviation_marks)
print("Minimum Marks:", min_marks)
print("Maximum Marks:", max_marks)
print("Range of Marks:", range_marks)