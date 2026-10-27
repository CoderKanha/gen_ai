# Dummy sales data
sales = [1200, 450, 980, 1500, 3000]

# Opening a file in write mode
with open('sales_data.txt', 'w') as sales_file:
    for data in sales:
        # Writing the sales amount in the file, each data on new line
        sales_file.write(f"{data}\n")

# Closing the file
sales_file.close()

# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:
    print(sales_file.read())

# Closing the file
sales_file.close()

# Optional
# Opening a file in write mode
with open('new_sales_data.txt', 'w') as sales_file:
    for data in sales:
        # Writing the sales amount in the file, each data separated with comma
        sales_file.write(f"{data}, ")

# Closing the file
sales_file.close()

# Opening a file in read mode
with open('new_sales_data.txt', 'r') as sales_file:
    # Printing the file data
    print(sales_file.read())

# Closing the file
sales_file.close()