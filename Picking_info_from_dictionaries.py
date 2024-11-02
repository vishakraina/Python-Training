# Topic 27 - Dictionaries: How to Retrieve Information

# In the previous chapter, we created a dictionary called customer_29876:

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}


# Suppose we want to find the address for customer_29876:

address_of_customer = customer_29876["address"]
print(address_of_customer) # Output - 4803 Wellesley St.

'''
In a list, you access an element by its index:
city_to_check = cities[3]  # Accessing the 4th item in the list (index 3)

In a dictionary, you access a value by using its key:
address_of_customer = customer_29876["address"]  # Accessing value using the key "address"

'''