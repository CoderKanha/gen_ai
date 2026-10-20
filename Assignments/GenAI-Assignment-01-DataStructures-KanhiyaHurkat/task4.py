# List of the products
products = ["Laptop", "Photo Frame", "Pasta", "T-Shirt", "Sofa", "Specs", "Television", "Sugar", "Cupboard", "Chair"]

# Product category set
categories_set = {"Electronics", "Home Decor", "Grosseries", "Clothing", "Furniture", "Accessories", "Electronics", "Grosseries", "Furniture", "Furniture"}

# Product dictionary with there price
price_dict = { "Laptop": 100000, "Photo Frame": 5000, "Pasta": 900, "T-Shirt": 1500, "Sofa": 15000, "Specs": 2500, "Television": 25000, "Sugar": 100, "Cupboard": 6500, "Chair": 2300 }

# Mapping product with the categories
categories_dict = {
    "Laptop": "Electronics",
    "Photo Frame": "Home Decor",
    "Pasta": "Groceries",
    "T-Shirt": "Clothing",
    "Sofa": "Furniture",
    "Specs": "Accessories",
    "Television": "Electronics",
    "Sugar": "Groceries",
    "Cupboard": "Furniture",
    "Chair": "Furniture",
}

# Creating list of tuple with product name, price and category
catelog = []
for product in products:
    catelog.append(tuple((product, price_dict[product], categories_dict[product])))

print(f"Catelog of the product list: {catelog}")

# Dictionary with product category with the list of product in that category
category_to_products = {}
for item in catelog:
    category = item[2]
    product = item[0]
    if (category_to_products.get(category)):
        category_to_products[category].append(product)
    else:
        category_to_products[category] = [product]

print(f"List of product for each category: {category_to_products}")

# Printing the list of product which has maximum count according to category
max_count = 0
max_category = ""

for category in category_to_products:
    count = len(category_to_products[category])

    if count > max_count:
        max_count = count
        max_category = category

print("Products:", category_to_products[max_category])