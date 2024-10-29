# Topic 10 - Comparison Operators

# Types of Comparison Operators:

full_name = "Mark Myers"
if full_name == "Mark Myers":
    print("Full name matches.")

total_cost = 100
if total_cost != 200:
    print("Cost does not match.")

age = 18
if age >= 18:
    print("You are eligible.")

# Equality and Not Equal Operators (== and !=)

your_ticket_number = 477208
if your_ticket_number != 487208:
    print("Better luck next time.")

# Greater Than and Less Than Operators (> and <)

temperature = 110
if temperature > 100:
    print("It's very hot!")

age = 15
if age < 18:
    print("You are a minor.")

# Greater Than or Equal To and Less Than or Equal To (>= and <=)

balance = 0
if balance >= 0:
    print("Balance is positive.")

quantity = 10 
stock = 20
if quantity <= stock:
    print("Order can be fulfilled.")

# Using Comparison Operators in Complex Expressions

x = 1
y = 3
a = 6
b = 2
if x + y == a - b:
    print("The values match.")
    
total_cost = 40
materials_cost = 10 
labor_cost = 30
if total_cost == materials_cost + labor_cost:
    print("Total cost is correct.")
