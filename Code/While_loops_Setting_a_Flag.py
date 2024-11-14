# Topic 52 - While Loops: Setting a Flag

# Setting a Flag for Loop Control

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
keep_looping = True

while keep_looping:
    user_input = input("Enter a city, or 'q' to quit: ")

    if user_input != "q":
        for city in cleanest_cities:
            if user_input == city:
                print("It's one of the cleanest cities")
                break  # Exit for loop if a match is found
    else:
        keep_looping = False  # Exit the loop by setting the flag to False
