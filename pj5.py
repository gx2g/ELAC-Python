# Author: Robert Resendez
# Date: 11-08-2024
# Purpose: Password Game – to check whether a password is very secure



n = 1

print("Welcome to the PASSWORD game of \"Robert Resendez\"!")
print(n, "===================================================="); n += 1;
pw = input("Please enter a password (Enter q to quit): ")

while (pw != "q"):
    print("The password you just entered is " + pw)
    # set all counts to zero
    
    badcount = 0 
    countdigits = 0
    countsymbols = 0
    countlower = 0
    countupper = 0
    countyears = 0

    # Counting 26 lower case leters:
    countlower += pw.count('a') + pw.count('b') + pw.count('c') + pw.count('e') + pw.count('f') + pw.count('g')
    countlower += pw.count('h') + pw.count('i') + pw.count('j') + pw.count('k') + pw.count('l') + pw.count('m')
    countlower += pw.count('n') + pw.count('o') + pw.count('p') + pw.count('q') + pw.count('r') + pw.count('s')
    countlower += pw.count('t') + pw.count('u') + pw.count('v') + pw.count('w') + pw.count('x') + pw.count('y') + pw.count('z')

    if(countupper < 2):
        print("R1: Your password is not secure for the matrix since it has less than 2 upper-case letters")
        badcount += 1


    if badcount == 0:
        print("Congratulations! Your password is very secure!")
    else: 
        print("Your password has the avoe, ", badcount, "problems to be fixed")
    
    pw = input("Please enter a password (Enter q to quit): ")





print(n, "===================================================="); n += 1;
print("Thank you for playing this PASSWORD game by Robert Resendez")
print(n, "================== END of GAME ====================="); n += 1;



