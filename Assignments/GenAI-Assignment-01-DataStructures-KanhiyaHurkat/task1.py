products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Camera"]

sample_products = ("Laptop", 47500, "Electronics")

print(f"Product: {products[1]}, {products[-1]}")

products.append("Speaker")
products.append("Monitor")

print(f"Updated Products List: {products}")

sample_products = list(sample_products)
sample_products[1] = 50000
sample_products = tuple(sample_products)
