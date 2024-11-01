# Topic 18 - Lists: Deleting and Removing Elements

# Example List Setup:

tasks = ["email Frank", "call Sarah", "meet with Zach"]


# Example of Deleting by Index:

del tasks[0]  
# Now tasks = ["call Sarah", "meet with Zach"]

# Syntax of the del Statement

del tasks[1]
# Deletes "call Sarah" and leaves ["email Frank", "meet with Zach"]

# Using remove() to Delete by Value

tasks.remove("call Sarah")  
# Now tasks = ["email Frank", "meet with Zach"]

# Syntax of the remove() Method

tasks.remove("meet with Zach")
# Removes "meet with Zach" and leaves ["email Frank", "call Sarah"]

# Deleting First Task After Completion:

tasks = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[0]
# Result: ["call Sarah", "meet with Zach"]

# Removing a Task by Specifying Its Name:

tasks = ["email Frank", "call Sarah", "meet with Zach"]
tasks.remove("call Sarah")
# Result: ["email Frank", "meet with Zach"]

# Deleting Multiple Tasks Using Index:

tasks = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[1]  # deletes "call Sarah"
del tasks[0]  # deletes "email Frank"
# Result: ["meet with Zach"]

