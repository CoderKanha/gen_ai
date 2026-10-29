try:
    # Taking user inputs for numerator and denominator 
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator

except ValueError:
    # Handling value error exception 
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    # Handling zero division error
    print("Error: Denominator cannot be zero.")

else:
    # Printing the result of division
    print(f"Result: {result}")

finally:
    # Executing the finally block
    print("Operation Complete")