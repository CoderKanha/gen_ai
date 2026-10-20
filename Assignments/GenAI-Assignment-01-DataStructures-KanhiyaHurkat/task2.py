products = ["Laptop", "Screwdriver", "Clothes", "Camera", "Car", "Freeze"]

categories_set = {"Electronics", "Accessories", "Wearables", "Photography", "Automobiles", "Home Appliances"}

categories_set.add("Cosmetics")  # Adding a new category to the set
categories_set.add("Photography")  # Adding a duplicate category to the set

print(f"Categories Set: {categories_set}") # Avoding Duplicate in output

print({"Electronics" in categories_set})  # Checking if "Electronics" is in the set

print(len(categories_set))  # Getting the number of unique categories in the set