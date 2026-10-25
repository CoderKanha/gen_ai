# Function to calcualte the final price after discount
# If discount_percent value is not provide, 5% discount applied by default
# Returned the same price if discount_percent exceeds 60%
def apply_discount(price, discount_percent = 5):
    if discount_percent <= 60:
        discounted_amount = price * (discount_percent / 100)
        return price - discounted_amount
    else:
        print("Discount can't be exceeds more than 60%")
        return price

print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(1500, 60))
print(apply_discount(3000, 61))