# Topic 31 - Looping Through Values in Python Dictionaries

'''
How
To loop through values in a dictionary, 
use a for loop along with the .values() method. 
This method retrieves each dictionary value in sequence, 
letting you process or display them as needed.
'''

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Loop through and print each value
for each_value in customer_29876.values():
    print(each_value)

'''
Output:
David
Elliott
4803 Wellesley St.
'''
