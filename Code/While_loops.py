# Topic 51 - While Loops

# Basic Structure of a While Loop

user_input = ""
while user_input != "q":
    user_input = input("Enter a city, or 'q' to quit: ")
    print(f"You entered: {user_input}")

# Using While Loops to Process User Input Until a Condition Is Met

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
user_input = ""

while user_input != "q":
    user_input = input("Enter a city, or 'q' to quit: ")
    if user_input != "q":
        for city in cleanest_cities:
            if user_input == city:
                print("It's one of the cleanest cities")
                break  # Exit for loop if a match is found

# Using Indentation to Define Nested Blocks in Loops and Conditionals

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
user_input = ""

while user_input != "q":  # Starts while loop
    user_input = input("Enter a city, or 'q' to quit: ")

    if user_input != "q":  # Checks if user wants to continue
        for city in cleanest_cities:  # Starts for loop to check city
            if user_input == city:
                print("It's one of the cleanest cities")
                break  # Ends for loop if match is found
