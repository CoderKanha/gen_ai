# Returns sum of all the prices
def calculate_total(prices):
    total_price = 0
    for price in prices:
        total_price += price
    return total_price

# Apply 5% tax
def apply_tax(amount):
    return amount + (amount * 0.05)