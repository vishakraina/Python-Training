# Topic 66 - Modules

# Creating a Module

# calculations.py
def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax

# Using a Module in Your Main Program

import calculations

# Calling Functions from a Module

tax_for_this_order = calculations.calc_tax(sales_total=101.37, tax_rate=0.05)
