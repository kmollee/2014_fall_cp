# refer
# http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/


def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number ** 0.5 + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def genPrimes():
    index = 1
    while True:
        if isPrime(index):
            yield index
        index += 1
