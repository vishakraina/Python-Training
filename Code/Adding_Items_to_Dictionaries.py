# Topic 29 - Adding Items to Python Dictionaries

'''
To add a new key-value pair to an existing dictionary, follow these steps:

Specify the dictionary name.
Set the key in square brackets [].
Assign a value to this key.

'''


# Example: Suppose we have a dictionary customer_29876:
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}



# To add a city, we can write:

customer_29876["city"] = "Toronto"

# After adding, customer_29876 now includes:

{
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
    "city": "Toronto"
}

# To create a dictionary with no key-value pairs, write:

things_to_remember = {}


# Then, add pairs one at a time:

things_to_remember[0] = "the lowest number"
things_to_remember["a dozen"] = 12




