import math


def f(x):
    return 10 * math.e ** (math.log(0.5) / 5.27 * x)


def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def radiationExposure(start, stop, step):
    totolRadiation = 0
    for year in xfrange(start, stop, step):
        activity = f(year)
        totolRadiation += activity * 1
    return totolRadiation


def isAround(num1, num2):
    return (num1 - num2) < 0.01


assert isAround(radiationExposure(0, 5, 1), 39.10318784326239) == True
assert isAround(radiationExposure(5, 11, 1), 22.94241041057671) == True
assert isAround(radiationExposure(0, 11, 1), 62.0455982538) == True
assert isAround(radiationExposure(40, 100, 1.5), 0.434612356115) == True
