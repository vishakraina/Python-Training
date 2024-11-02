# Topic 14 - Comments

# Creating a Comment

# This is a comment.
# This line explains what the following code does.
print("Hello, world!")


# Commenting Out Code for Debugging

if first_name == "Harry":
    if last_name == "Potter":
        # if interest == "wizardry"  # Commented out to test
        print("Welcome back to Hogwarts, Harry!")

# If you find an error (like a missing colon), you can correct it:

if first_name == "Harry":
    if last_name == "Potter":
        if interest == "wizardry":  # Colon added
            print("Welcome back to Hogwarts, Harry!")

# Full-Line Comments

# This is a full-line comment.
print("Hello, world!")

# Inline Comments

print("Hello, world!")  # Greet the world

# Multi-Line Comments

'''
This is a multi-line comment.
Python ignores all the lines within these triple quotes.
Useful for adding longer explanations.
'''
print("Hello, world!")




