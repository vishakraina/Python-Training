# Topic 64 - Data Files: Retrieving Data

# Opening the File for Reading

with open("greet.txt", "r") as f:

# Reading the File's Contents

with open("greet.txt", "r") as f:
    text_of_file = f.read()

# Displaying the Data

print(text_of_file)

# Output : Hello, World!