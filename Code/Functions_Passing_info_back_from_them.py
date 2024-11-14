# Topic 47 - Functions: Passing Information Back from Them

# Adding a return statement

def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax

# Using the return value
sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print(sales_tax)  # Output: 5.0685

# Condensing Code with return

def calc_tax(sales_total, tax_rate):
    return sales_total * tax_rate

# Directly using the return value
print(calc_tax(sales_total=101.37, tax_rate=.05))  # Output: 5.0685
