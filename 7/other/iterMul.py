def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


assert iterMul(3, 5) == 15
assert iterMul(10, 3) == 30
