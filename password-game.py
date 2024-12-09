# Author: Robert Resendez
# Date: 11-08-2024
# Purpose: Password Game – check password security

n = 1

print("Welcome to the PASSWORD game of \"Robert Resendez\"!")
print(n, "===================================================="); n += 1;
pw = input("Please enter a password (Enter q to quit): ")

# while loop, keep going until q is specified. 
while (pw != "q"):
    print("The password you just entered is " + pw)
    
    # set all counts to zero, variables for violations
    badcount = 0 
    countdigits = 0
    countsymbols = 0 
    countlower = 0
    countupper = 0
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

    # Counting if password is 7 characters long
    countdigits += pw.count('0') + pw.count('1') + pw.count('2') + pw.count('3') + pw.count('4') 
    countdigits += pw.count('5') + pw.count('6') + pw.count('7')
    
    # Counting for special characters
    countsymbols += pw.count('$') + pw.count('%') + pw.count('@') + pw.count('!') + pw.count('?') + pw.count('*')

    # Counting for recent years
    countyears += pw.count('2021') + pw.count('2022') + pw.count('2023') + pw.count('2024')
    
    # preforming checks with expressions
    if(countupper <= 1):
        print("Reason 1: Less than 2 upper-case letters")
        badcount += 1
    
    if(countlower <= 1):
        print("Reason 2: Less than 2 lower-case letters")
        badcount += 1
    
    if(len(pw) <= 6):
        print("Reason 3: Less then 7 characters long")
        badcount += 1
    
    if countdigits <= 1:
        print("Reason 4:less then 2 digits (numbers)")
        badcount += 1

    if (len(pw) >= 11):
        print("Reason 5: more then 12 characters long")
        badcount += 1
    
    if pw.count('') > 0:
        print("Reason 6: Not Secure, contains spaces")
        badcount += 1

    if pw.isdigit(): 
        print("Reason 7: not secure it contains only 1 digit")
        badcount += 1

    if pw.isalpha():
        print("Reason 8: not secure it contains only alphabets")
        badcount += 1

    if countsymbols <= 0:
        print("Reason 9: not secure contains none of these ($, %, @, !, ?, *)")
        badcount += 1

    if (countyears <= 1):
        print("Reason 10: not secure cointains 2024, 2023, 2022, or 2021")

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



