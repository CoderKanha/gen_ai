# List of given price
prices = [120, 350, 'abc', 500, -200, 800]
total = 0
 
for price in prices:
    try:
        # Comparing a non-number with 0 raises TypeError
        if price < 0:
            raise ValueError("Negative price not allowed")
        total += price
        print(f"Added {price} | Running total: {total}")
    except TypeError:
        # Handling price which is not a number 
        print(f"Skipped '{price}': not a number")
    except ValueError as e:
        # Handling negative value error
        print(f"Skipped {price}: {e}")

#  Printing the final price
print(f"\nFinal total: {total}")