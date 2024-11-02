#  Topic 24 - Changing Case


'''
Let’s create code that will:

Ask the user to enter their city.
Convert their input to lowercase.
Check if their city is on the list of the cleanest cities.

'''

city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()

cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"]

for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")


'''

Explanation of the Code

Convert User Input to Lowercase:
By using lower(), we ensure that the city name entered by the user is all lowercase, which makes comparisons easier:

city_to_check = city_to_check.lower()

List of Cleanest Cities:
We store the list of clean cities in all-lowercase format as well:

cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"]

Comparing User Input with Each Clean City:
Using a for loop, we compare the lowercase user input to each city in cleanest_cities. If there’s a match, it displays the message:

if city_to_check == a_clean_city:
    print("It's one of the cleanest cities")

'''

# Alternative: Storing Original Input in a Different Variable

lowercase_city_to_check = city_to_check.lower()

# Using Uppercase

city_to_check = city_to_check.upper()
cleanest_cities = ["CHEYENNE", "SANTA FE", "TUCSON", "GREAT FALLS", "HONOLULU"]


# Converting for Display Purposes

city_to_check = city_to_check.title()
print("Great news! " + city_to_check + " is one of the cleanest cities.")

# Output - Great news! Cheyenne is one of the cleanest cities.

# Summary - Convert to upper, lowers or title:

variable_name.upper()
variable_name.lower()
variable_name.title()


