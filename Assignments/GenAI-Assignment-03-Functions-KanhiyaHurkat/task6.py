# Function that processes a list of prices
def process_prices(prices):

    # Using map() and lambda to apply a 10% discount to every price
    discounted_prices = list(map(lambda price: price * 0.90, prices))

    # Using filter() and lambda to keep only discounted prices above 300
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))

    # Return both discounted and filtered list
    return discounted_prices, filtered_prices


# Testing function with given list
discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

# Print all prices after applying the 10% discount
print("Discounted prices:", discounted_prices)

# Print only discounted prices greater than 300
print("Filtered prices (above 300):", filtered_prices)