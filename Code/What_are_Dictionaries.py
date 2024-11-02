# Topic 25 - Dictionaries: What They Are

# Comparing lists and dictionaries

my_cats = ["Draco", "Bellatrix", "Voldemort"]

# in lists, you can access items by index's.

print(my_cats[0])  # Output: Draco

'''
Suppose you have the following details about a customer:

First name: David
Last name: Elliott
Address: 4803 Wellesley St.
City: Toronto
Province: ON
Country: Canada
Postal Code: M7A1N3

In a dictionary, you can store this information in key-value pairs, 
making it easy to access any piece of information with a descriptive key:

'''

customer_29876 = {
    "first_name": "David",
    "last_name": "Elliott",
    "address": "4803 Wellesley St.",
    "city": "Toronto",
    "province": "ON",
    "country": "Canada",
    "postal_code": "M7A1N3"
}

# Accessing Data in a Dictionary

print(customer_29876["city"])  # Output: Toronto
print(customer_29876["country"])  # Output: Canada
