

def testAdd(s1, s2, s3) :
    points = 10
    sum = int(input("please enter the sum of these three numbers: "))
    if sum == (int(s1) + int(s2) + int(s3)) :
        print("Congratulations! You are right! You earned " + str(points) + " points now.")
        npts[0] += points
    else :
        print("So Sorry, it is not correct! You lose " + str(points) + " points now.")
        npts[0] -= points

n = 1
npts = [0]

print("Welcome to the Super Numbering game by Robert Resendez !!!")
your_name = input("Please enter your full name: ")
print(your_name + ": Welcome to play this game. You have " + str(npts[0]) + " points to start.")

while True :
    print(n, "================================================="); n+=1;
 
    s1 = input("Enter first number: ")
    s2 = input("Enter first number: ")
    s3 = input("Enter first number: ")
    print("You just entered 3 numbers: ", s1, s2, s3)
    testAdd(s1, s2, s3)
    print("Now, you have " + str(npts[0]) + " points in your account!")
    play_again = input("Would you like to contine this game? 'yes' or 'no': ")
    if play_again == "no" or play_again == "n" :
            break

    print(n, "================================================="); n+=1;
    print("Finally, you have " + str(npts[0]) + " points in your account!")
    print("Thank you for playing this wonderful game designed by Robert Resendez")

    print(n, "================================================="); n+=1;
    x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit")
