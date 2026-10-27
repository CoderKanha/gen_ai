import os

# Asking user for the file name
file_name = input("Enter the file name: ")

# Get the folder where the Python script is saved
folder_path = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the file
file_path = os.path.join(folder_path, file_name)

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print(file.read())

    file.close()
else:
    print("File not found. Please check the filename.")