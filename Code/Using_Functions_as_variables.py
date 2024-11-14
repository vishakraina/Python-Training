# Topic 48 - Using Functions as Variables

# Basic Example:

def add_numbers(first_number, second_number):
    return first_number + second_number

def subtract_numbers(first_number, second_number):
    return first_number - second_number

# Traditional way
result_of_adding = add_numbers(1, 2)
result_of_subtracting = subtract_numbers(3, 2)
sum_of_results = result_of_adding + result_of_subtracting
print(sum_of_results)  # Output: 4

# Using functions as variables in one line
sum_of_results = add_numbers(1, 2) + subtract_numbers(3, 2)
print(sum_of_results)  # Output: 4


# Using Functions Directly in Expressions

print(add_numbers(5, 10))  # Output: 15


# Nesting Functions

result = add_numbers(subtract_numbers(10, 5), 3)
print(result)  # Output: 8

