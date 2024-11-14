# Topic 50 - Functions within Functions

# Basic Nested Function Example

def now_say_it(message):
    print(message)  

def say_something():
    what_to_say = "Hi"  # Local variable
    now_say_it(what_to_say)  # Pass the local variable as an argument

say_something()  # Output: Hi

# Using Parameters and Arguments to Avoid Scope Errors

def now_say_it(content):  # Accepting parameter
    print(content)  # Output the received parameter

def say_something():
    what_to_say = "Hello"
    now_say_it(what_to_say)  # Passing as argument

say_something()  # Output: Hello
