# List of product prices
prices = [100, 250, 400, 1200, 50, 2000, 850]

# Using filter() with a lambda function to select prices greater than 500
expensive_prices = list(filter(lambda price: price > 500, prices))

# Using filter() with a lambda function to select prices less than or equal to 500
affordable_prices = list(filter(lambda price: price <= 500, prices))

# Print the original list of prices greater than 500
print("Prices greater than 500:", expensive_prices)

# Print the list of prices less than or equal to 500
print("Prices less than or equal to 500:", affordable_prices)