# Apply discount on the given price
def apply_discount(price, percent):
    return price - (price * percent/100)

# Add flat 50 rupees discount 
def flat_discount(price):
    return price - 50