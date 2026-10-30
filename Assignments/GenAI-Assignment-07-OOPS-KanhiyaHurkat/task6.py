class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic method to return a readable string
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator overloading for +
    def __add__(self, other):
        return self.price + other.price


# Create two product objects
product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Mobile", 20000, "Electronics")

# Test __str__ method
print(product1)
print(product2)

# Test operator overloading
total = product1 + product2
print("Total combined price:", total)