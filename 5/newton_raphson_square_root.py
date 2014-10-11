# Lecture 3.7, slide 3

# Newton-Raphson for square root

# http://upload.wikimedia.org/wikipedia/commons/e/e0/NewtonIteration_Ani.gif

epsilon = 0.01
y = 24.0
guess = y / 2.0

while abs(guess * guess - y) >= epsilon:
    # (((guess ** 2) - y) / (2 * guess)) calculate x axis move
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
