# Topic 28 - Dictionaries: Versatile Keys and Values

'''
In previous examples, we created dictionaries with both keys and values as strings. 
For instance:
'''

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

# Keys don’t have to be strings; they can also be numbers. For example:

rankings = {
    5: "Finland",
    2: "Norway",
    3: "Sweden",
    7: "Iceland",
}

# Accessing a Value with a Number Key:

second_ranking_country = rankings[2]

# Values in a dictionary can also be numbers:

country_ranks_so_far = {
    "Finland": 5,
    "Norway": 2,
    "Sweden": 3,
    "Iceland": 7,
}

'''
Accessing a Value with a String Key:
To retrieve Norway’s rank:
'''

norway_ranking = country_ranks_so_far["Norway"]

'''
Mixing Data Types in Keys and Values
Python dictionaries allow you to mix and match data types for both keys and values. 
Here’s an example:
'''

things_to_remember = {
    0: "the lowest number",
    "a dozen": 12,
    "snake eyes": "a pair of ones",
    13: "a baker's dozen",
}

'''
Readability in Longer Dictionaries
When defining a dictionary with multiple key-value pairs, you can improve readability by placing each pair on a separate line. 
Also, adding a comma after the last pair helps avoid errors if you add more pairs later.
'''

things_to_remember = {
    0: "the lowest number",
    "a dozen": 12,
    "snake eyes": "a pair of ones",
    13: "a baker's dozen",
}
