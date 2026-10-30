# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: ₹{self.price}"

    # Operator overloading
    def __add__(self, other):
        return self.price + other.price
    
# Inventory class
class Inventory:
    def __init__(self):
        self.products = []

    # Add product
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully.")

    # Remove product by name
    def remove_product(self, product_name):
        self.products = [
            product for product in self.products
            if product.name != product_name
        ]
        print(f"Product '{product_name}' removed if it existed.")

    # Calculate total value
    def get_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price
        return total_value
    
    # Display all products
    def show_all_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                print(f"Product name is {product.name} and it's price is {product.price}.")

# Store class
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        product_added = False
        while not product_added:
            product_name = input("Enter product name: ")
            try:
                product_price = int(input("Enter product price: "))
                product = Product(name=product_name, price=product_price)
                self.inventory.add_product(product)
                product_added = True

            except:
                print("Product price should be valid number")


    def show_summary(self):
        print(f"There are total {len(self.inventory.products)} items in inventory and total value is {self.inventory.get_total_value()}")

# Test the system
store = Store("Super Market")

# Adding 3 products
store.add_new_product()
store.add_new_product()
store.add_new_product()

# Display all products
store.inventory.show_all_products()

# Show summary
store.show_summary()

# Operator overloading: combine prices of two products
if len(store.inventory.products) >= 2:
    product1 = store.inventory.products[0]
    product2 = store.inventory.products[1]

    total_price = product1 + product2

    print(f"\nCombined price of {product1.name} and {product2.name}: ₹{total_price:.2f}")
