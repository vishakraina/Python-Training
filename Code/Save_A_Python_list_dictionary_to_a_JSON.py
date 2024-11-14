# Topic 74: How to Save a Python List or Dictionary in a File: JSON

# Import the JSON module:

import json


# Define the list or dictionary:

alphabet_letters = ["a", "b", "c"]


# Or a dictionary:

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Open the file to save the data:

with open("alphabet_list.json", "w") as f:

# Write the data using json.dump():

json.dump(alphabet_letters, f)

# or for a dictionary:

with open("customer_29876.json", "w") as f:
    json.dump(customer_29876, f)


