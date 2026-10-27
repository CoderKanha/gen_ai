# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:
    # Printing file content using read() method
    print(f"Printing the complete content of file: \n{sales_file.read()}")

# Closing the file
sales_file.close()



# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:
    # Printing file content using readline() method
    print(f"Printing first line of file: {sales_file.readline()}")

# Closing the file
sales_file.close()



# Opening a file in read mode
sales_data_list = []
with open('sales_data.txt', 'r') as sales_file:
    # Adding sales data in list
    for data in sales_file.readlines():
        sales_data_list.append(int(data.strip('\n')))

    # Printing sales data
    print(sales_data_list)

# Closing the file
sales_file.close()