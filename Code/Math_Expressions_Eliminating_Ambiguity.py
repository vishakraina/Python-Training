# Topic 7 - Math Expressions: Eliminating Ambiguity

# What Are Math Expressions and Order of Operations in Python?

total_cost = 1 + 3 * 4

# How to Use Parentheses to Control Order of Operations in Python

# 1.	Multiplying before adding:

total_cost = 1 + (3 * 4)  # Result: 13

# 2.	Adding before multiplying:

total_cost = (1 + 3) * 4  # Result: 16

# 3.	Practical Example with Nested Operations:

result_of_computation = (2 * 4) * 4 + 2

#  Multiply first, then add:

result_of_computation = ((2 * 4) * 4) + 2  # Result: 34

#	Multiply by the sum:

result_of_computation = (2 * 4) * (4 + 2)  # Result: 48