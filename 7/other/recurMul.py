def recurMul(a, b):
    # base case
    if b == 1:
        return a
    # recursive step
    else:
        return a + recurMul(a, b - 1)

assert recurMul(3, 5) == 15
assert recurMul(10, 3) == 30
