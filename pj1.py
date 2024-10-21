# Author: gx2g
# Date: 10/19/2024
# Purpose: Gain or lose points by guessing the sum of numbers game. 



# Global Scope Variables
n = 1
npts = [0]

# function that takes in 3 args
def testAdd(s1, s2, s3) :

    points = 10 # local scope variable
    sum = int(input("please enter the sum of these three numbers: ")) # takes input 

    # checks sum of n, else if neg
    if sum == (int(s1) + int(s2) + int(s3)) :
        print("Congratulations! You are right! You earned " + str(points) + " points now.")
        npts[0] += points
    else :
        print("So Sorry, it is not correct! You lose " + str(points) + " points now.")
        npts[0] -= points


# program Starts Here
print("Welcome to the Super Numbering game by Robert Resendez !!!") # welcome statement
your_name = input("Please enter your full name: ") #variable with user input right assignemnt
print(your_name + ": Welcome to play this game. You have " + str(npts[0]) + " points to start.") #variable with str() strick enforcement

# while True loop, game is running
while True :
    print(n, "================================================="); n+=1;
 
    s1 = input("Enter first number: ") #pass user input 
    s2 = input("Enter first number: ")
    s3 = input("Enter first number: ")
    
    print("You just entered 3 numbers: ", s1, s2, s3) # display user input to screen

    ## function call ##
    testAdd(s1, s2, s3) # run user input through function for calculation 
    
    print("Now, you have " + str(npts[0]) + " points in your account!") # print updated results string enforcement

    play_again = input("Would you like to contine this game? 'yes' or 'no': ") # prompt user if they want to play again

    # if no or n break
    if play_again == "no" or play_again == "n" :
       break


# print ending messages after break
print(n, "================================================="); n+=1;
print("Finally, you have " + str(npts[0]) + " points in your account!")
print("Thank you for playing this wonderful game designed by gx2g")

print(n, "================================================="); n+=1;
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit")
