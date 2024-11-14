# Topic 49 - Functions: Local vs. Global Variables

# Creating and Using Global Variables

what_to_say = "Hello"  # Global variable
def greet():
    print(what_to_say)  # Accessible in functions

greet()  # Output: Hello

# Creating and Using Local Variables

def say_something():
    what_to_say = "Hi"  # Local variable
    print(what_to_say)

say_something()  # Output: Hi
print(what_to_say)  # Error: NameError: 'what_to_say' is not defined

# Avoiding Global Variable Use in Functions

greeting = "Hello"  # Global variable

def greet(message):  # Use parameters instead of global variables
    print(message)

greet(greeting)  # Output: Hello

# Local and Global Variables with Same Name

x = 10  # Global variable

def modify_x():
    x = 5  # Local variable in this function
    print(x)  # Output: 5

modify_x()
print(x)  # Output: 10 (global x remains unaffected)

