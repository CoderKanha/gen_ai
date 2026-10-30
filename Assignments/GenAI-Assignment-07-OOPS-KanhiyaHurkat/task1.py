class Product:
    # Class constructor method
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Get info related to the product
    def get_info(self):
        print(f"This is a {self.name}. It's price is {self.price} and it comes under {self.category} category.")

    # Apply discount and display discounted amount of the product
    def apply_discount(self, percent):
        print(f'Discounted price for {self.name}: {self.price - (self.price * percent / 100)}')

# Creating object 1 and calling functions
obj1 = Product('Laptop', 500000, 'Electronics')
obj1.get_info()
obj1.apply_discount(20)

# Creating object 2 and calling functions
obj2 = Product('Sofa', 10000, 'Furniture')
obj2.get_info()
obj2.apply_discount(10)

