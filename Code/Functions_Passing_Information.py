# Topic 42 - Functions: Passing Information

# Basic Function with Arguments:

def add_numbers(first_number, second_number):  # Function accepts two arguments
    total = first_number + second_number
    print(total)

add_numbers(53, 109)   # Call function and pass 53 and 109 as arguments
# Output: 162


# Parameters and Arguments:
'''
Parameters are variable names in the function definition (e.g., first_number, second_number).
Arguments are the values or variables you pass into the function call (e.g., 53, 109).
'''

# Positional Arguments:

'''
Arguments are assigned to parameters based on their position in the function call.
The first argument goes to the first parameter, the second to the second, etc.
'''

add_numbers(1.11, 2.22)  # 1.11 -> first_number, 2.22 -> second_number
# Output: 3.33

# Variable Arguments:

#You can pass variables instead of hard-coded values.
#The parameter catches the value of the variable passed.

greeting = "Hello, there."
def greet_user(message):
    print(message)

greet_user(greeting)  # Pass greeting variable
# Output: Hello, there.

# Naming Parameters and Arguments:

'''
The names of arguments (in the call) and parameters (in the definition) don’t have to match.
However, it’s often helpful to give them matching names for clarity.
'''
whatever = "Hello, there."
def greet_user(message): 
    print(message)

greet_user(whatever)   # Variable whatever is passed to parameter message
# Output: Hello, there.

