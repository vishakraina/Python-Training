# Topic 37 - Creating a Dictionary That Contains Lists

# Define the customer dictionary, including a key named "discounts", which holds a list of discounts:

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
    "discounts": ["standard", "volume", "loyalty"]
}

# The "discounts" key points to a list that contains strings representing the types of discounts available to the customer.

# Access elements within the list using the dictionary key:

print(customer_29876["discounts"])
# Output: ['standard', 'volume', 'loyalty']

# Access specific items from the list:

print(customer_29876["discounts"][1])
# Output: 'volume'
