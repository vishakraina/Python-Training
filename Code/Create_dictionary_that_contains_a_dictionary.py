# Topic 39 - Creating a Dictionary That Contains a Dictionary


# Original Approach with List of Dictionaries:

customers = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd."
    },
    {
        "customer id": 1,
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145"
    },
    {
        "customer id": 2,
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St."
    }
]


# Convert to a Dictionary of Dictionaries:

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

# Flexible Key Options:

customers = {
    "johnog": {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd."
    },
    "coder1200": {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145"
    },
    "madmaxine": {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St."
    }
}
