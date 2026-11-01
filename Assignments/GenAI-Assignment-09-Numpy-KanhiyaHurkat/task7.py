import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# Sales analysis
total_weekly_sales = np.sum(sales)
average_daily_sales = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
standard_deviation_sales = np.std(sales)
days_above_average = np.where(sales > average_daily_sales)[0]

# Display the results
print("Total Weekly Sales:", total_weekly_sales)
print("Average Daily Sales:", average_daily_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation of Sales:", standard_deviation_sales)
print("Days Above Average Sales:", days_above_average)