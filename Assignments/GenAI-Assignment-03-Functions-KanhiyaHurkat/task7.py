# Function to add a new price to list
def add_price(prices_list, price):
    prices_list.append(price)
    print("Price added successfully...")


# Function to calculate and return average price
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0  # Return 0 if list is empty

    return sum(prices_list) / len(prices_list)


# Function to return maximum price
def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None  # Return None if list is empty

    return max(prices_list)


prices = []

# Display the menu repeatedly until the user chooses to quit
while True:
    print("\n===== PRICE MENU =====")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - Quit")

    choice = input("Enter your choice: ").lower()

    # Option 1: Add a price to the list
    if choice == "1":
        try:
            price = float(input("Enter the price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                add_price(prices, price)

        except ValueError:
            print("Invalid input! Please enter a numeric price")

    # Option 2: Calculate and display average price
    elif choice == "2":
        average = get_average_price(prices)

        if len(prices) == 0:
            print("No prices available. Please add a price first.")
        else:
            print("Average price:", average)

    # Option 3: Display highest price
    elif choice == "3":
        highest = get_max_price(prices)

        if highest is None:
            print("No prices available. Please add a price first.")
        else:
            print("Highest price:", highest)

    # Option q: Exit the program
    elif choice == "q":
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please select valid option from menu...")