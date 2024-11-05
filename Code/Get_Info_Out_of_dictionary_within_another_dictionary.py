# Topic 40 - How to Get Information Out of a Dictionary Within Another Dictionary

# Setting Up a Dictionary with Nested Dictionaries:

customers = {
    0: {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd."
    },
    1: {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145"
    },
    2: {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St."
    }
}

# Accessing an Entire Inner Dictionary:

print(customers[2])
# Output: {'first name': 'Jill', 'last name': 'Somers', 'address': '3 Main St.'}


# Accessing Specific Information in an Inner Dictionary:

print(customers[2]["address"])
# Output: 3 Main St.

