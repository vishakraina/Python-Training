# Topic 16 - Lists: Adding and Changing Elements

# Example of Initial List Setup:

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]


# Appending Elements

cities.append("New York")
# Now cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle", "New York"]

# Alternative Method for Appending - Using + Operator

cities = cities + ["Dubuque", "New Orleans"]
# Now cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle", "New York", "Dubuque", "New Orleans"]

# Inserting Elements

cities.insert(0, "New York")  # Insert at the beginning
# Now cities = ["New York", "Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

# Or, to insert "Dallas" before "Baltimore":

cities.insert(2, "Dallas")
# Now cities = ["New York", "Atlanta", "Dallas", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

# Modifying Existing Elements

cities[2] = "Houston"  # Change "Dallas" to "Houston"
# Now cities = ["New York", "Atlanta", "Houston", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

