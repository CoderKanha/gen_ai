order_list = []
# Running the while loop till user doesn't enter 'q'
while(True):
    print("Choose menu from the below options:")
    print("1 - Add order amount")
    print("2 - Show all orders")
    print("q - To exit the menu")

    # Taking user selection from the menu and running if..elif..else condition
    user_input = input("Enter your option: ")
    if user_input == "1":
        try:
            # Taking order amount from user in form of integer
            ordered_amount = int(input("Enter the ordered amount: "))
            order_list.append(ordered_amount)
        except ValueError:
            # Handling the case where user entered non-numeric number
            print("Please enter an integer value...:(")
            continue
    elif user_input == "2":
        # Printing the list of ordered amount with discount and total value
        print("-----------------------------------------------------------------------")
        print("Order Amount\t| Discount %\t| Discount Amount\t| Final Amount")
        print("-----------------------------------------------------------------------")
        if len(order_list) == 0:
            # Printing message if no order amount is available
            print("No orders available. Please add order amount...")
            continue
        else:
            for order_amount in order_list:
                discounted_amount = 0
                discount_percent = 0
                final_amount = 0
                if order_amount >= 2000:
                    discount_percent = 15
                    discounted_amount = order_amount * (discount_percent / 100)
                elif 1500 <= order_amount < 2000:
                    discount_percent = 10
                    discounted_amount = order_amount * (discount_percent / 100)
                elif 1000 <= order_amount < 1500:
                    discount_percent = 7
                    discounted_amount = order_amount * (discount_percent / 100)
                else:
                    discount_percent = 0
                    discounted_amount = 0

                final_amount = order_amount - discounted_amount
                print(f"{order_amount}\t\t| {discount_percent}\t\t| {discounted_amount:.2f}  \t\t| {final_amount:.2f}")
            continue
    elif user_input == 'q':
        # Breaking the loop if user enter 'q' as an option to exit the program
        break
    else:
        # Displaying message if user input doesn't available in menu and continuing the code
        print("Please select correct option...:(")
        continue