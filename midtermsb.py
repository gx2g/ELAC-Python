# create a function that takes 3 arguments, print a char 4 times 6 rows
def printBox(char, length, width):
    for _ in range(width):
        print(char * length)

printBox('&', 4, 6)



