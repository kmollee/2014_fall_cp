def hypotenuse(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5

print(hypotenuse(3, 4))  # 5.0 (not 5)


def isPositive(n):
    return (n > 0)

print isPositive(10)  # True
print isPositive(-10)  # False
