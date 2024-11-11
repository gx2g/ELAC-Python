# Author: Robert Resendez
# Date: 11-08-2024
# Purpose: Password Game – check password security

n = 1

print("Welcome to the PASSWORD game of \"Robert Resendez\"!")
print(n, "===================================================="); n += 1;
pw = input("Please enter a password (Enter q to quit): ")

while (pw != "q"):
    print("The password you just entered is " + pw)
    # set all counts to zero
    
    # variable for how many valiolations
    badcount = 0 
    # variable for numbers
    countdigits = 0
    # variable for special characters
    countsymbols = 0
    # variable to check lower case 
    countlower = 0
    # variable to check upper case
    countupper = 0
    # variable to count years
    countyears = 0


    # Counting 26 upper case leters:
    countupper += pw.count('A') + pw.count('B') + pw.count('C') + pw.count('D') + pw.count('E') + pw.count('F') + pw.count('G')
    countupper += pw.count('H') + pw.count('I') + pw.count('J') + pw.count('K') + pw.count('L') + pw.count('M')
    countupper += pw.count('N') + pw.count('O') + pw.count('P') + pw.count('Q') + pw.count('R') + pw.count('S')
    countupper += pw.count('T') + pw.count('U') + pw.count('V') + pw.count('W') + pw.count('X') + pw.count('Y') + pw.count('Z')


    # Counting 26 lower case leters:
    countlower += pw.count('a') + pw.count('b') + pw.count('c') + pw.count('d') + pw.count('e') + pw.count('f') + pw.count('g')
    countlower += pw.count('h') + pw.count('i') + pw.count('j') + pw.count('k') + pw.count('l') + pw.count('m')
    countlower += pw.count('n') + pw.count('o') + pw.count('p') + pw.count('q') + pw.count('r') + pw.count('s')
    countlower += pw.count('t') + pw.count('u') + pw.count('v') + pw.count('w') + pw.count('x') + pw.count('y') + pw.count('z')

    
    if(countupper <= 1):
        print("Reason: Less than 2 upper-case letters")
        badcount += 1
    
    if(countlower <= 1):
        print("Reason: Less than 2 lower-case letters")
        badcount += 1
    



    if badcount == 0:
        print("Congratulations! Your password is very secure!")
    else: 
        print("Your password has the above,", badcount,"problems to be fixed")
    
    print(n, "----------------------------------------------------"); n += 1;    
    pw = input("Please enter a password (Enter q to quit): ")
    print("-------------------------------------------------------")


print("====================================================")
print("Thank you for playing this PASSWORD game by Robert Resendez")
print("================== END of GAME =====================")



