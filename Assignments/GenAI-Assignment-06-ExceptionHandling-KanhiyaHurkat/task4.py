# Getting file name from the user
filename = input("Enter the filename: ")
 
try:
    # Opening the file and reading the content
    with open(filename, "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    # Handling file not found error
    print(f"Error: File '{filename}' not found.")

except PermissionError:
    # Handling permission error
    print(f"Error: Permission denied for '{filename}'.")

else:
    # Printing first 3 lines of the file
    print("First 3 lines of the file:")
    for line in lines[:3]:
        print(line.rstrip())

finally:
    # Executing the final block
    print("File operation attempted.")