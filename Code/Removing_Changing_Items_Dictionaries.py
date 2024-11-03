# Topic 30 - Removing and Changing Items in Python Dictionaries

'''

How:
To remove a key-value pair from a dictionary, use the del statement, followed by the dictionary name and key in square brackets [].

'''

# Dictionary with customer info
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Removing the address
del customer_29876["address"]

# To change a value for an existing key, simply reassign the key to the new value.

customer_29876["city"] = "Winnipeg"