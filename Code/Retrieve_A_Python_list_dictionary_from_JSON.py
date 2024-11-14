# Topic 75: How to Retrieve a Python List or Dictionary from a JSON File

# Import the JSON module:

import json

# Open the file to read the data:

with open("customer_29876.json") as f:

# Retrieve the data using json.load():

customer_29876 = json.load(f)

# Use the retrieved data:

print(customer_29876)

# Or to access a specific value:

print(customer_29876["last name"])

