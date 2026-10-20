# List of six products
products = ["Laptop", "Photo Frame", "Pasta", "T-shirt", "Sofa", "Specs"]

# Category set of the product listed above
categories_set = {"Electronics", "Home Decor", "Grosseries", "Clothing", "Furniture", "Accessories"}

# Adding a new and duplicate category to the set
categories_set.add("Cosmetics")
categories_set.add("Furniture")

# Displayed that duplicate category is ignored
print(f"Categories Set: {categories_set}")

# Checking if "Electronics" category is in the set
print("Electronics" in categories_set)

# Getting the number of unique categories in the set
print(len(categories_set))