# Topic 13 - Nested if Statements

# Example of Nested if Statement:

if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f

#  How to Use Nested if Statements in Python

# Starting with the First-Level Condition

if c == d:
    # Nested conditions will go here

# Adding Nested Conditions

if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f

# Including an else Block

if c == d:
    # Nested conditions are here
else:
    e = f

# Using Indentation for Clarity

if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f
