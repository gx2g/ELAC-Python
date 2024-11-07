# Author: Robert Resendez
# Date: 11-05-2024
# Purpose: To play a game of rolling 2 dice between dealer and you, and win lose money until either side has no money.
 
import random

# Global Variables 
n = 1 
yourMoney = 100
dealerMoney = 100


# print unicode charactors of dice set 1 through 6 to add cool icons to game
print(" ---------------" + " " + chr(0x2680) + " " + chr(0x2681) + " " + chr(0x2682) + " " + chr(0x2683) + " " + chr(0x2684) + " " + chr(0x2685) + " --------------");


print("Welcome to the Rolling 2 Dice Game by Robert Resendez" + chr(0x2757))
print("================================================")

 # get bet from user
bet = int(input("Enter your bet to roll 2 dice for this complete game (enter 0 to quit):"))
if bet == 0:
    exit()

print("Bank: You have $" + str(yourMoney) + " to play th game, Dealer also has " + str(dealerMoney) + " dollars to play with.")

# start of game
while True: 
    print(n, "------------------------------------------"); n+=1;
   
    # dealer rolls dice
    dealer = random.randint(1, 6) + random.randint(1, 6)
    # you roll dice
    you = random.randint(1, 6) + random.randint(1, 6)

    # print results of bet
    print("Roll 2 Dice twice, Dealer got " + str(dealer) + " and you got " + str(you) + ".")

    # dealer greater then you, you lost
    if dealer > you:
        yourMoney -= bet
        dealerMoney += bet
        print("You lost! Now you have " + str(yourMoney) + " dollars!, and dealer has " + str(dealerMoney) + " dollars!")

    # you greater then dealer, you won
    elif dealer < you:
        dealerMoney -= bet
        yourMoney += bet
        print("You Won! Now you have " + str(yourMoney) + " dollars!, and dealer has " + str(dealerMoney) + " dollars!")

    # if tie then just print dollars left to play
    else: 
        print("Its a TIE! now you have " + str(yourMoney) + " dollars!, and dealer has " + str(dealerMoney) + " dollars!")

    # if dealer or you dollars 0 then exit game
    if dealerMoney <=0 or yourMoney <=0:
        break

# final print statements
print(n, "================================================"); n+=1;
print("Game ends. You have " + str(yourMoney) + " dollars! and dealer has " + str(dealerMoney) + " dollars.")
print(n, "================================================"); n+=1;
print("Thank you for playing this Rolling 2 Dice Game by Robert Resendez")
print(n, "================================================"); n+=1;
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then Enter to exit:")