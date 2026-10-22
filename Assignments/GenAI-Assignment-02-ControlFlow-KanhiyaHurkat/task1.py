try:
    # Reading user input value as an order amount
    order_amount = int(input("Enter order amount: "))
    discounted_amount = 0
    taxed_amount = 0
    sub_total = 0

    # Applying discount rule based on the rules
    if order_amount >= 2000:
        discounted_amount = order_amount * 0.15
    elif 1500 <= order_amount < 2000:
        discounted_amount = order_amount * 0.10
    elif 1000 <= order_amount < 1500:
        discounted_amount = order_amount * 0.07
    else:
        discounted_amount = 0

    sub_total = order_amount - discounted_amount

    # Added additional 5% tax on the discounted amount
    taxed_amount = sub_total * 0.05

    # Printing the sub_total, taxed_amount and final_amount
    print(f"Sub total amount: {sub_total}")
    print(f"Taxed amount: {taxed_amount}")
    print(f"Final amount: {sub_total + taxed_amount}")

except ValueError:
    # Handling the case where user entered non-numeric number
    print("Please enter an integer value")