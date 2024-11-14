# Topic 77: A More Practical Example of Exception Handling

#Using a while True loop:

while True:

# try block to handle errors:

try:
    filename = input("What text file to open? ")
    with open(filename) as f:
        print(f.read())


# Using except to handle FileNotFoundError:

except FileNotFoundError:
    print("Sorry, " + filename + " not found.")


# break to exit the loop:

break

# Indents for readability:

while True:
    try:
        filename = input("What text file to open? ")
        with open(filename) as f:
            print(f.read())
        break
    except FileNotFoundError:
        print("Sorry, " + filename + " not found.")
