# Topic 33 - Looping Through Key-Value Pairs in Python Dictionaries

'''
How
To loop through key-value pairs in a dictionary, 
use the .items() method within a for loop. 
Here’s an example:

'''

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Loop through and print each key-value pair
for each_key, each_value in customer_29876.items():
    print("The customer's " + each_key + " is " + each_value)


'''
Output:
The customer's first name is David
The customer's last name is Elliott
The customer's address is 4803 Wellesley St.
'''