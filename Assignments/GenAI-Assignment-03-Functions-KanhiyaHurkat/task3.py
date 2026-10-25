# Lambda function to calculate the price after adding 18% GST
gst = lambda price: price + (0.18 * price)

# Calculate the price of an item worth 100 after adding GST
print("Price after GST:", gst(100))


# Lambda function to calculate the final price after adding GST and applying a discount
# The discount is applied after adding GST
final_price = lambda price, discount: gst(price) - (gst(price) * discount / 100)

# Calculate the final price after 18% GST and a 10% discount
print("Final price after GST and discount:", final_price(100, 10))