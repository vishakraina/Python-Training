# Topic 73: CSV Files: Appending Rows to Them

# Open the file in append mode:

with open("whatever.csv", "a", newline="") as f:

# Create a CSV writer object:

data_handler = csv.writer(f, delimiter=",")

# Append new rows:

data_handler.writerow(["2006", "World Cup", "Burkina Faso"])
data_handler.writerow(["2011", "Butter Cup", "France"])
data_handler.writerow(["2012", "Coffee Cup", "Brazil"])
