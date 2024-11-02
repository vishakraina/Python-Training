# Topic 12 - Testing Sets of Conditions

# Examples of Testing Sets of Conditions:

# Example with `and`
if weight > 300 and time < 6:
    status = "try to recruit him"

# Example with `or`
if SAT > avg or GPA > 2.5 or parent == "alum":
    message = "Welcome to Leeds College!"

# How to Test Sets of Conditions in Python

# Using and for Combined Condition Testing

if weight > 300 and time < 6:
    status = "try to recruit him"

# Using or for Combined Condition Testing

if SAT > avg or GPA > 2.5 or parent == "alum":
    message = "Welcome to Leeds College!"

# Combining and and or Conditions with Parentheses

# Example 1: Both conditions in parentheses need to be true for a pass
if (age > 65 or age < 21) and res == "U.K.":
    pass_status = "Eligible"

# Example 2: Either condition outside or inside parentheses needs to be true
if age > 65 or (age < 21 and res == "U.K."):
    pass_status = "Eligible"
