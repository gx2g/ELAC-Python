# Author: Robert Resendez
# Date: 11-05-2024
# Purpose: JP4 - Game of roll the dice. Earn/Lose money with initial money of 100 dollars. 
 
import random

# Global Variables 
n = 1 
yourMoney = 100


# print unicode charactors of dice set 1 through 6 to add cool icons to game
print(" ---------------" + " " + chr(0x2680) + " " + chr(0x2681) + " " + chr(0x2682) + " " + chr(0x2683) + " " + chr(0x2684) + " " + chr(0x2685) + " --------------");


print("Welcome to Rolling Dice Game by Robert Resendez" + chr(0x2757))
print("================================================")
print("Bank: You have $" + str(yourMoney) + " dollars to play with.")

# start of game
while True: 
    print(n, "------------------------------------------"); n+=1;
    # get bet from user
    bet = int(input("Enter your bet to roll the dice (enter 0 to quit):"))
    if bet == 0:
        break

    # dealer rolls dice
    dealer = random.randint(1, 6)
    # you roll dice
    you = random.randint(1, 6)

    print("Dealer got " + str(dealer) + " and you got " + str(you) + ".")

    if dealer > you:
        yourMoney -= bet
        print("You lost " + str(bet) + " dollars. now you have " + str(yourMoney) + " dollars")
    elif dealer < you:
        yourMoney += bet
        print("You won " + str(bet) + " dollars. now you have " + str(yourMoney) + " dollars")
    else: 
        print("Its a TIE! now you have " + str(yourMoney) + " dollars")


print(n, "================================================"); n+=1;
print("Thank you for playing the Rolling Dice Game by Robert Resendez")
print(n, "================================================"); n+=1;
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this concsole, then Enter to exit:")

print("end of game")