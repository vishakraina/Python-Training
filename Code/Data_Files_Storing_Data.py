# Topic 63 - Data Files: Storing Data

# Opening a File to Write Data

with open("greet.txt", "w") as f:

# Writing Data to the File

with open("greet.txt", "w") as f:
    f.write("Hello, world!")

# Writing a String Stored in a Variable

greeting = "Hello, world!"
with open("greet.txt", "w") as f:
    f.write(greeting)

