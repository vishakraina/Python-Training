# Topic 62 - Data Files

# Opening a File in Write Mode

with open("whatever.txt", "w") as file_to_work_with:

# Write Data to the File

with open("whatever.txt", "w") as file_to_work_with:
    file_to_work_with.write("Hello, world!\n")

# File Path

# Windows Path Example
with open("data\\whatever.txt", "w") as file_to_work_with:

# OS X/Linux Path Example
with open("data/whatever.txt", "w") as file_to_work_with:

# Changing the Handle Name

with open("whatever.txt", "w") as f:
    f.write("More data\n")
