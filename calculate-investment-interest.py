# Author: Robert Resendez
# Date: 10/21/2024
# Purpose: Calculate investment interest over years 

# MAIN PROGRAM

# global varaibles
n = 1

# ===========================

print("Welcome to the Investment Report Tool by Robert Resendez!")
print(n, "==========================="); n + 1;

# Accept the inputs
startBalance = float(input("Enter the investment ammount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table
print("%20s%20s%20s%20s" % ("Years", "Starting balance", "Interest", "Ending balance"))

# Compute and display the results for each year

for year in range(1, years + 1):
    # interest is startBalance times rate f rom user input
    interest = startBalance * rate

    # endBalance is startBalance after rate times then we add interest to it. 
    endBalance = startBalance + interest

    # string formating with left side padding creates table effect with variables after calculation            
    print("%20d%20.2f%20.2f%20.2f" % (year, startBalance, interest, endBalance))
    
    # after calculations start balance equals end balance
    startBalance = endBalance

    # total interest increments 
    totalInterest += interest

print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)

print(n, "==========================="); n + 1;
print("Thank you for using the Investment Report Tool by Robert Resendez!")
print(n, "==========================="); n + 1;

x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then Enter to exit: ")

# End of MAIN PROGRAM
