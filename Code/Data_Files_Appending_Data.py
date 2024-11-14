# Topic 65 - Data Files: Appending Data

# Opening a File for Appending

with open("greet.txt", "a") as f:

# Writing to the File

with open("greet.txt", "a") as f:
    f.write("\nHave a nice day!")


# After this operation, the file content becomes:

Hello, World!
Have a nice day!

# Reading and Displaying the File

with open("greet.txt") as f:
    message = f.read()
print(message)

# This will output:

Hello, World!
Have a nice day!
