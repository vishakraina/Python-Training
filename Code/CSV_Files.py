# Topic 67 - CSV Files

# Example of CSV format:

Year,Event,Winner  
1995,Best-Kept Lawn,None  
1999,Gobstones,Welch National  
2006,World Cup,Burkina Faso


# Import the CSV Module

import csv

# Reading CSV Files

with open("competitions.csv") as f:
    contents_of_file = csv.reader(f)

# Accessing Data in the CSV

with open("competitions.csv") as f:
    contents_of_file = csv.reader(f)
    for row in contents_of_file:
        print(row)

#Output

['Year', 'Event', 'Winner']
['1995', 'Best-Kept Lawn', 'None']
['1999', 'Gobstones', 'Welch National']
['2006', 'World Cup', 'Burkina Faso']
