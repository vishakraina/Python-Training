# Topic 17 - Lists: Taking Slices Out of Them

# Example of Initial List Setup:

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

# Basic Slicing Syntax

smaller_list_of_cities = cities[2:5]
# Result: ["Chicago", "Denver", "Los Angeles"]

# Omitting the Start or End Index

# Omitting the start index (equivalent to cities[0:5])
smaller_list_of_cities = cities[:5]
# Result: ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles"]

# Omitting the end index
smaller_list_of_cities = cities[2:]
# Result: ["Chicago", "Denver", "Los Angeles", "Seattle"]

# Negative Indexing:

# Slicing from the third-to-last element to the end
end_cities = cities[-3:]
# Result: ["Denver", "Los Angeles", "Seattle"]

# Full list copy
all_cities = cities[:]

# Reversing the list
reversed_cities = cities[::-1]
