# Topic 72: CSV Files: Loading Information into Them (Part 3)

# Open the file for writing:

with open("whatever.csv", "w", newline="") as f:

# Create a CSV writer object:

data_handler = csv.writer(f, delimiter=",")

# Write rows of data:

data_handler.writerow(["Year", "Event", "Winner"])
data_handler.writerow(["1995", "Best-Kept Lawn", "None"])
data_handler.writerow(["1999", "Gobstones", "Welch National"])

