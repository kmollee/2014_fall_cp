# add all X to Y even number

X = 1
Y = 10
total = 0
# make sure X is odd
if X % 2 != 0:
    X = X + 1

for num in range(X, Y + 1, 2):
    total = total + num

print("total is:", total)
