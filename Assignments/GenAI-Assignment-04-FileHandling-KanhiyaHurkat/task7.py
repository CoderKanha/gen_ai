# Price dictionary
price = {
    "Mouses": 500.00,
    "Keyboard": 800.00,
    "Monitor": 7000.00,
    "Pendrive": 400.00,
    "Cameras": 5000.00,
}

# A safe check so user can't add unrealistice value
max_discount = 30
total_discounted_price = 0

try:
    # Taking value from the user
    discount_percent = int(input("Enter the discount percentage: "))

    # Checking if entered value is greater than max discount
    if discount_percent > max_discount:
        print(f"Maximun {max_discount}% discount is allowed...")
    else:
        # Opening the file 
        with open("discount_report.txt", "a") as discount_file:
            discount_file.write("Product \t | O. Price \t | Dis. Price\n")
            for price_detail in price.items():
                # Calculating the value and writing to the discount_report.txt file
                discounted_price = price_detail[1] * (discount_percent / 100)
                final_price = price_detail[1] - discounted_price
                total_discounted_price += final_price
                discount_file.write(f"{price_detail[0]} \t | {price_detail[1]} \t\t | {final_price}\n")

            # Optional
            discount_file.write(f"Total items: {len(price.keys())}\n")
            discount_file.write(f"Average dicsounted price: {total_discounted_price/len(price.keys())}")

        # Closing the file
        discount_file.close()


except:
    # Handling the non-integer value 
    print("Value must be integer")