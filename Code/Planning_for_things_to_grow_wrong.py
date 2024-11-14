# Topic 76: Planning for Things to Go Wrong

# Using try block:

try:
    filename = input("What text file to open? ")
    with open(filename) as f:
        print(f.read())


# Catching specific exceptions with except:

except FileNotFoundError:
    print("Sorry, " + filename + " not found.")

# Indentation:

try:
    # Code that might cause an error
except ErrorType:
    # Code that handles the error

# Handling Multiple Errors:

try:
    # Some risky code
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Value error occurred")

# Generic Exception Handling:

except Exception as e:
    print("An error occurred:", e)
