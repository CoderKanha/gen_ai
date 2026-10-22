# Created required variables to shore the total revenue and list of order with no discount
total_revenue = 0
orders_with_no_discount = []

# Print the summary table to display values 
print("-----------------------------------------------------------------------")
print("Order Amount\t| Discount %\t| Discount Amount\t| Final Amount")
print("-----------------------------------------------------------------------")
for order_amount in [1200, 2500, 800, 1750, 3000]:
    discounted_amount = 0
    discount_percent = 0
    final_amount = 0
    if order_amount >= 2000:
        # Applying 15% discount if order_amount is more than 2000
        discount_percent = 15
        discounted_amount = order_amount * (discount_percent / 100)
    elif 1500 <= order_amount < 2000:
        # Applying 10% discount if order_amount is more than 1500 or less than 2000
        discount_percent = 10
        discounted_amount = order_amount * (discount_percent / 100)
    elif 1000 <= order_amount < 1500:
        # Applying 7% discount if order_amount is more than 1000 or less than 1500
        discount_percent = 7
        discounted_amount = order_amount * (discount_percent / 100)
    else:
        # Applying 0% discount if order_amount is less than 1000
        discount_percent = 0
        discounted_amount = 0
        orders_with_no_discount.append(order_amount)

    # Calculating the final and total revenue and printing the values
    final_amount = order_amount - discounted_amount
    total_revenue += final_amount
    print(f"{order_amount}\t\t| {discount_percent}\t\t| {discounted_amount:.2f}  \t\t| {final_amount:.2f}")

print(f"Total revenue: {total_revenue}")
print(f"There are {len(orders_with_no_discount)} order/s with 0% discount -> {orders_with_no_discount}")