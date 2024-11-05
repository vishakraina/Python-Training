# Topic 38 - How to Get Information Out of a List Within a Dictionary

# Define the customer dictionary with a list of discounts:

customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
    "discounts": ["brother-in-law", "standard", "volume", "loyalty"]
}


# Use if and elif statements to find the biggest applicable discount:
    
if "brother-in-law" in customer_29876["discounts"]:
    discount_amount = 0.30
elif "loyalty" in customer_29876["discounts"]:
    discount_amount = 0.15
elif "volume" in customer_29876["discounts"]:
    discount_amount = 0.10
elif "standard" in customer_29876["discounts"]:
    discount_amount = 0.05

