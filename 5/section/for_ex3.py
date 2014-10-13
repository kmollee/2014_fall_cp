# add all X to Y odd number
X = 1
Y = 10
total = 0

for num in range(X, Y + 1):
    if num % 2 == 1:
        total = total + num

print("total is:", total)
