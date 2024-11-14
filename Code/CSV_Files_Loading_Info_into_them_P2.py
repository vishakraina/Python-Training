# Topic 71 - CSV Files: Loading Information into Them (Part 2)


# Creating the CSV Writer Object

with open("whatever.csv", "w", newline="") as f:
    data_handler = csv.writer(f)


# Specifying the Delimiter

data_handler = csv.writer(f, delimiter=";")


# Writing Data with the CSV Writer

data_handler.writerow(["Year", "Event", "Winner"])
data_handler.writerow([1995, "Best-Kept Lawn", "None"])
data_handler.writerow([1999, "Gobstones", "Welch National"])
data_handler.writerow([2006, "World Cup", "Burkina Faso"])


# Example Code:

import csv

# Open or create a CSV file in write mode
with open("whatever.csv", "w", newline="") as f:
    # Create a CSV writer object
    data_handler = csv.writer(f, delimiter=",")  # You can change delimiter here
    # Write data to the CSV file
    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow([1995, "Best-Kept Lawn", "None"])
    data_handler.writerow([1999, "Gobstones", "Welch National"])
    data_handler.writerow([2006, "World Cup", "Burkina Faso"])
