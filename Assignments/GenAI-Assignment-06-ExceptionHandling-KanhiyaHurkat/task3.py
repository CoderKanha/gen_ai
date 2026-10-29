# Function to check the value of age is in range or not
def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return age
 
 
try:
    # Taking age as an input from user
    age = int(input("Enter your age: "))
    check_age(age)

    # Printing age if it is within the range
    print(f"Valid age: {age}")
except ValueError as e:
    # Printing the exception error
    print(e)