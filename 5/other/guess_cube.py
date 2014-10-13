x = 25
epsilon = 0.01
step = epsilon ** 2
# step may have some tradeoff
# larger step with small guess time, but might miss solution
# small step with larger guess time, but more close solution
numGuesses = 0
ans = 0
while (abs(ans ** 2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print("numGuesses = " + str(numGuesses))

if abs(ans ** 2 - x) >= epsilon:
    print("Fail on square root of " + str(x))
else:
    print(str(ans) + "is clos to the square root of " + str(x))
