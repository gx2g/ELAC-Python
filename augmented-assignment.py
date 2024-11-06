
# old method
# x = x + 3
# x = x - 3
# x = x * 2
# x = x / 2
# x = x % 6

# assign 15 to x
x = 15

# Augmented Assignment Operators

# 15 + 3 = 18 answer
x += 3
print(x)

# x is now 18 - 3 goes back to 15 answer
x -= 3
print(x)

# x is 15 * 2 = 30 answer
x *= 2
print(x)
print(type(x))

# x is 30 / 2 = 15.0 floating type
x /= 2
print(x)
print(type(x))

#module 6 goes into 15 twice (6 + 6) = 12, left over is = 3 is answer
x %= 6
print(int(x))
print(type(x))
