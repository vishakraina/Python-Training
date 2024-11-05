# Topic 35 - Retrieving Information from a List of Dictionaries in Python

customers = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    {
        "customer id": 1,
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
]

# Step 1: Get the dictionary of the customer with id 1
dictionary_to_look_in = customers[1]

# Step 2: Access the address
customer_address = dictionary_to_look_in["address"]
print(customer_address)  # Outputs: PO Box 1145
