# List of original prices
prices = [100, 250, 400, 1200, 50]

# Lambda function to calculate price after adding 18% GST
gst = lambda price: price + (0.18 * price)

# Using map() to apply the GST lambda function to every price
prices_with_gst = list(map(gst, prices))

# Print the original list of prices
print("Original prices:", prices)

# Print the list of prices after adding GST
print("Prices after GST:", prices_with_gst)