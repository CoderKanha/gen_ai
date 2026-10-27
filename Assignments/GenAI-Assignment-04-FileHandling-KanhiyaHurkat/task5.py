total_product = 0

# Opening the file to add prooduct details
with open("products.txt", "w") as file:
    file.write("Product Name\t | Price\n")

    # Looping 3 times to add list of 3 products
    while total_product < 3:
        # Taking product name from user
        product_name = input("Enter product name: ")
        try:
            # Taking product price from user 
            product_price = int(input("Enter product price: "))

            # Writing the content in the file
            file.write(f"{product_name}\t | {product_price}\n")
            total_product += 1
            if total_product != 3: 
                print(f"Add {3 - total_product} more product")
        except:
            # Catching the error if user enter value apart from integer for price
            print("Product price should be integer")

# Closing the file
file.close()

# Opening the file in read mode
with open("products.txt", "r") as file:

    # Printing the content of the file
    print(file.read())

# Closing the file
file.close()