# Topic 43 - Functions: Passing Information with Keyword Arguments

# Using Keyword Arguments:

def say_names_of_couple(husband_name, wife_name):
    print("The names of the couple are " + husband_name + " and " + wife_name)

# Calling with keyword arguments
say_names_of_couple(husband_name="Bill", wife_name="Zelda")
# Output: The names of the couple are Bill and Zelda

# order doesnot matter

say_names_of_couple(wife_name="Zelda", husband_name="Bill")
# Output: The names of the couple are Bill and Zelda


# Mixing Positional and Keyword Arguments:

def introduce_person(name, age):
    print(f"{name} is {age} years old.")

introduce_person("Alice", age=30)  # Valid
# Output: Alice is 30 years old.

# You can use positional arguments along with keyword arguments, but positional arguments must come before any keyword arguments in the function call. 
#introduce_person(age=30, "Alice")  # Invalid
