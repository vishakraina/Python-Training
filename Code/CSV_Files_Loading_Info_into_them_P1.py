# Topic 70 - CSV Files: Loading Information into Them (Part 1)

# Import the CSV Module

import csv

# Opening a CSV File for Writing

with open("whatever.csv", "w", newline="") as f:


# Example

import csv

# Open (or create) a new CSV file in write mode
with open("whatever.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # You can write rows of data to the CSV file
    writer.writerow(["Year", "Event", "Winner"])
    writer.writerow([1995, "Best-Kept Lawn", "None"])
    writer.writerow([1999, "Gobstones", "Welch National"])
    writer.writerow([2006, "World Cup", "Burkina Faso"])


