# Topic 69 - CSV Files: Picking Information Out of Them

# CSV File Format

Year,Event,Winner
1995,Best-Kept Lawn,None
1999,Gobstones,Welch National
2006,World Cup,Burkina Faso


# Reading the CSV File

with open("competitions.csv") as f:
    contents_of_f = csv.reader(f)

# Steps for Finding the Winner

target = input("Enter the name of a competition: ")

# Find the Index of the Competition:

index_number_of_target = potter_competitions.index(target)

# Find the Winner's Index:

index_number_of_winner = index_number_of_target + 1

#  Retrieve the Winner:

the_winner = potter_competitions[index_number_of_winner]

# Display the Winner:

print("The winner was " + the_winner)


# Example code

import csv

with open("competitions.csv") as f:
    contents_of_f = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_f:
        potter_competitions += each_line

target = input("Enter the name of a competition: ")
index_number_of_target = potter_competitions.index(target)
index_number_of_winner = index_number_of_target + 1
the_winner = potter_competitions[index_number_of_winner]
print("The winner was " + the_winner)



Output : The winner was None


