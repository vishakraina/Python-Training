# Topic 45 - Functions: Mixing Positional and Keyword Arguments

# Using Both Positional and Keyword Arguments. Note Arguments are in funcion call.

def give_greeting(greeting, first_name):
    print(greeting + ", " + first_name)

give_greeting("Hello there", first_name="Al")
# Output: Hello there, Al

# Including Default Values in the Mix

def give_greeting(greeting, first_name, flattering_nickname=" the wonder boy"):
    print(greeting + ", " + first_name + flattering_nickname)

give_greeting("Hello there", first_name="Al")
# Output: Hello there, Al the wonder boy

# Using Lists and Dictionaries as Arguments

customers = {
    0: {"first name": "John", "last name": "Ogden", "address": "301 Arbor Rd."},
    1: {"first name": "Ann", "last name": "Sattermyer", "address": "PO Box 1145"},
    2: {"first name": "Jill", "last name": "Somers", "address": "3 Main St."},
}

def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])

# Example call
find_something(customers, 2, "last name")
# Output: Somers



