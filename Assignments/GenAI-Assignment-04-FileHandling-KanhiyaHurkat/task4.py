sales_data = []
# Opening a file in read mode
with open('sales_data.txt', 'r') as sales_file:
    for sales in sales_file.readlines():
        sales_data.append(int(sales.strip("\n")))

# Closing the file
sales_file.close()

# Printing sales data list
print(f"Sales data: {sales_data}")

# Printing total sale
print(f"Total Sales: {sum(sales_data)}")

# Printing highest sale
print(f"Highest Sales: {max(sales_data)}")

# Printing lowest sale
print(f"Lowest Sales: {min(sales_data)}")

# Printing average sale
print(f"Average Sales: {sum(sales_data) / len(sales_data)}")