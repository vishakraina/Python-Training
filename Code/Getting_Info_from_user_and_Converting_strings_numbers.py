# Topic 23 - Getting Information from the User and Converting Strings and Numbers

# Example: Checking if a City is Environmentally Clean

# input function

city_to_check = input("Enter the name of a city: ")


'''
Breaking Down the Code
Variable to Store Input:
You need a variable (in this case, city_to_check) to hold the user’s input.

The input() Function:
input() captures what the user types and assigns it to city_to_check.

Prompt Message:
The prompt message (inside quotes) is displayed to the user.

The input() function always stores data as a string. 

'''

# Example: Converting User Input to an Integer

monthly_income = input("Enter your monthly income: ") # here it is stored as string.

# Converting a String to an Integer or a Float

monthly_income_as_integer = int(monthly_income)

monthly_income_as_float = float(monthly_income)


# Converting Numbers Back to Strings

min_wage = 15

# Here below statement will not print bcz it cannot concat string and integer.

print("The minimum wage in your state is $" + min_wage)

# So we change min_wage to str and then print it.

min_wage = str(min_wage)
print("The minimum wage in your state is $" + min_wage)


# Convert to integer,float or string

int(variable_name)
float(variable_name)
str(variable_name)

