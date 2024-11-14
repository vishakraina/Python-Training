# Topic 68 - CSV Files: Reading Them

# Opening the CSV File

with open("competitions.csv") as f:

# Reading the File with csv.reader()

contents_of_f = csv.reader(f)

# Creating a List to Store Data

potter_competitions = []

# Looping Through the CSV Data

for each_line in contents_of_f:
    potter_competitions += each_line

# Displaying the Final List

print(potter_competitions)

#Output

['Year', 'Event', 'Winner', '1995', 'Best-Kept Lawn', 'None', '1999', 'Gobstones', 'Welch National', '2006', 'World Cup', 'Burkina Faso']
