X = 1
Y = 10
Z = 3
total = 0
for num in range(X, Y + 1, Z):
    total = total + num
assert total == 12
print(X, "~", Y, "with", Z, "setp, total is", total)
