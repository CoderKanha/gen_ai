daily_sales = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for sales in daily_sales:
    if sales == -1:
        # Breaking the loop if sales value is corrupted
        break
    elif sales == 0:
        # Not adding the sales and continuing the loop if sales is 0
        continue
    else:
        # Adding up the sales value in the total sales
        total_sales += sales
# Printing the total sales after completing the loop 
print(f"Total sales: {total_sales}")
