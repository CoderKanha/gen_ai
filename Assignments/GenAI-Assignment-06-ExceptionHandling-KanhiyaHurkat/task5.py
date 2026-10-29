# Empty cart list
cart = []
 
while True:
    # Taking user input value as a price
    entry = input("Enter price (or 'q' to quit): ")

    # Breaking the loop if user enter 'q'
    if entry.lower() == 'q':
        break
 
    try:
        # Converting price into float
        price = float(entry)

        if price < 0:
            # Raising error if value is negative
            raise ValueError("Negative price not allowed")

        # Adding price to the cart
        cart.append(price)
        print(f"Added {price}")

    except ValueError as e:
        # Covers both invalid input and the custom negative price error
        if "Negative" in str(e):
            print(f"Error: {e}")
        else:
            # Error handling for invalid numbers
            print("Error: Please enter a valid number.")

#  Printing total items and bill of the cart
print(f"\nTotal items: {len(cart)}")
print(f"Total bill: {sum(cart)}")