# Icome Tax Form
# Author: Robert Resendez
# Compute a person's income tax

'''

1. Significant constants:
    tax rate
    standard deduction
    deduction per dependent

2. The inputs are:
    gross income
    number of dependents

3. Computations: 
    taxable income = gross income - the standard deduction - a deduction for each dependent
    income tax = is a fixed percentage of the taxable income 

4. the out are: 
    the income tax

'''
userName = input("What is your name? ")
print("Welcome: " + userName)

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 1000.0
DEPENDANT_DEDUCTION = 3000.0

#Request the inputs
grossIncome = float(input("Enter your gross income: "))
numDependents = int(input("ENter the number of dependents: "))

# Compute the income tax
taxbleIncome = grossIncome - STANDARD_DEDUCTION - DEPENDANT_DEDUCTION * numDependents
incomeTax = taxbleIncome * TAX_RATE

# Display the income tax

print("the income tax is $ " + str(incomeTax))

