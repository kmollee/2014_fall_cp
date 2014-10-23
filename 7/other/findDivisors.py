def findDivisors(n1, n2):
    """
    assumes n1 and n2 positive ints
    return tuple containing
    common divisors of n1 and n2
    """
    divisors = tuple()
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors += (i,)
    return divisors

divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    print(d)
    total += d
print("total:", total)
