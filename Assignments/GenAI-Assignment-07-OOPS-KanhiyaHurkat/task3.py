class Product:
    # Class constructor method
    def __init__(self, name, __price, category):
        self.name = name
        self.price = __price
        self.category = category

    # Get price value
    def get_price(self):
        return self.price

    # Set new price if price is greater than 0
    def set_price(self, price):
        if price > 0:
           self.price = price 

    # Get info related to the product
    def get_info(self):
        print(f"This is a {self.name}. It's price is {self.get_price()} and it comes under {self.category} category.")

    # Apply discount and display discounted amount of the product
    def apply_discount(self, percent):
        print(f'Discounted price for {self.name}: {self.get_price() - (self.get_price() * percent / 100)}')

class ElectronicProduct(Product):
    def __init__(self, name, __price, category, warranty_years):
            super().__init__(name, __price, category)
            self.warranty_years = warranty_years

    def get_info(self):
        print(f"This is a {self.name} and it has {self.warranty_years} years of warranty.")


# Creating object 1 and calling functions
obj1 = ElectronicProduct('Laptop', 500000, 'Electronics', 3)
obj1.get_info()
obj1.apply_discount(10)

