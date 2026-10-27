new_sales_data = [5000, 2500, 1700]

# Opening a file in append mode
with open('sales_data.txt', 'a+') as sales_file:
    # Appending new sales data
    for data in new_sales_data:
        sales_file.write(f"{str(data)}\n")

# Closing the file
sales_file.close()

# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:
    # Printing file content
    print(f"Updated content of file: \n{sales_file.read()}")

# Closing the file
sales_file.close()


# Optional
# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:    
   
    print(f"Total number of lines: {len(sales_file.readlines())}")

# Closing the file
sales_file.close()