#Topic 36 - Adding a New Dictionary to a List of Dictionaries

# Identify the new customer’s ID by getting the length of the list, which provides the next index for the new customer dictionary.

new_customer_id = len(customers)

# Prepare the customer information in variables

new_first_name = "Maria"
new_last_name = "Garcia"
new_address = "1234 Elm St."

# Create a new dictionary with the customer’s ID and other information

new_customer = {
    "customer id": new_customer_id,
    "first name": new_first_name,
    "last name": new_last_name,
    "address": new_address,
}

# Append the new dictionary to the list

customers.append(new_customer)

