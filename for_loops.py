# Topic 21 - for Loops

# Example Scenario: Checking for a Clean City

city_to_check = "Tucson"

# list of cleanest cities
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

# Without for loop

if city_to_check == cleanest_cities[0]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[1]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[2]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[3]:
    print("It's one of the cleanest cities")
elif city_to_check == cleanest_cities[4]:
    print("It's one of the cleanest cities")

# Using a for Loop

for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")

# Optimizing with break

for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
        break

# Readable Variable Names

for x in y:
    if x == z:
        print("It's one of the cleanest cities")
