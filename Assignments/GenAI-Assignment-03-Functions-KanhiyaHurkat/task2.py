# Defined factorial function taking one argument as number
# If value is 0 or 1, return 1 as a value
# If value is negative printing the error message
# Or else returing the factorial value
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        print('Value cannot be negative')
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))
