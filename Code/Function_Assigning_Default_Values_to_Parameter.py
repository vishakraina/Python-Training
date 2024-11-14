# Topic 44 - Functions: Assigning Default Values to Parameters

# Defining a Default Value:

def calc_tax(sales_total, tax_rate=0.04):
    print(sales_total * tax_rate)

# Calling without tax_rate uses the default value 0.04
calc_tax(sales_total=101.37)  # Output: 4.0548

# Overriding the Default Value:

calc_tax(sales_total=101.37, tax_rate=0.075)  # Output: 7.60275

# Using an Empty Default Value for Optional Parameters:

def print_order(product_name, color, size, engraving_text=""):
    print(f"Product: {product_name}, Color: {color}, Size: {size}")
    if engraving_text:
        print(f"Engraving: {engraving_text}")
    else:
        print("No engraving.")

# Example calls
print_order("Mug", "Blue", "Large", "Happy Birthday")
# Output: Engraving: Happy Birthday

print_order("Mug", "Blue", "Large")
# Output: No engraving.
