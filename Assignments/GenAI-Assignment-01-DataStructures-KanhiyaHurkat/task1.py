# List of six products
products = ["Laptop", "Photo Frame", "Pasta", "T-shirt", "Sofa", "Specs"]

# Tuple of one sample product with name, price and category
sample_products = ("Laptop", 47500, "Electronics")

# Printing second and last product from the list
print(f"Product: {products[1]}, {products[-1]}")

# Appending two new products and printing the new product list
products.append("Water Bottle")
products.append("Wallet")
print(f"Updated Products List: {products}")

# Converting sample_product into list, updating the price and changing back to tuple
sample_products = list(sample_products)
sample_products[1] = 50000
sample_products = tuple(sample_products)
print(type(sample_products))
