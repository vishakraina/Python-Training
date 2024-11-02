# Topic 11 - Else and Elif Statements

# What are Else and Elif Statements?

species = "cow"
if species == "cat":
    print("Yep, it's a cat.")
else:
    print("Nope, not a cat.")

# Multiple conditions using elif
donut_condition = "not fresh"
donut_price = "low"
if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0

# Else Statement

species = "cat"
if species == "cat":
    print("Yep, it's a cat.")
else:
    print("Nope, not a cat.")

# Elif Statement

donut_condition = "fresh"
donut_price = "low"
if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0

# Using Multiple Independent If Statements

donut_condition = "fresh"
donut_filling = "chocolate"
donut_price = "reasonable"
buy_score = 0
if donut_condition == "fresh":
    buy_score += 10
    print(buy_score)
if donut_filling == "chocolate":
    buy_score += 5
    print(buy_score)
if donut_price == "reasonable":
    buy_score += 7
    print(buy_score)