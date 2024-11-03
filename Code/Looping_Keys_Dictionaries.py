# Topic 32 - Looping Through Keys in Python Dictionaries

'''
How
To iterate over the keys in a dictionary, use a for loop with the .keys() method. Here’s an example:

'''

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Loop through and print each key
for each_key in customer_29876.keys():
    print(each_key)


# Output will be:
'''
first name
last name
address
'''