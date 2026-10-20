# Dictionary of product list with there price
price_dict = {
    "Laptop": 100000,
    "Photo Frame": 5000,
    "Pasta": 900,
    "T-Shirt": 1500,
    "Sofa": 15000,
    "Specs": 2500
}

# Adding a new product with its price to the dictionary
price_dict["Monitor"] = 20000

# Updating the price of an existing product in the dictionary
price_dict["Laptop"] = 60000

if (price_dict.get("Specs")):
    price_dict.pop("Specs")
    print("Item removed from the dictionary")
else:
    print("Item not found in the dictionary")
    raise KeyError("Product is not available in the dictionary")

# Summing up all the price of the product
total_price = 0
for key, value in price_dict.items():
    total_price += value

# Printing the average price of all the products
print(total_price / len(price_dict.keys()))

# Printing product name with min and max value
print(min(price_dict, key=price_dict.get))
print(max(price_dict, key=price_dict.get))