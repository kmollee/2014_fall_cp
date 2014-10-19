def findRoot2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    low = min(0, x)
    high = max(0, x)
    ans = (low + high) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans
print(findRoot2(25.0, 2, 0.01))
print(findRoot2(20.0, 2, 0.01))
print(findRoot2(16.0, 2, 0.01))
print(findRoot2(9.0, 2, 0.01))
# when fall witg a fractional argument like 0.25
# search 0 ~ 0.125
# which mean our first guess will be the average, or .125

# seach wrong field


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ' + str(x) +
                  ' and power = ' + str(power))
            res = findRoot2(x, power, epsilon)
            if res == None:
                print('    No root')
            else:
                print('    ' + str(res ** power) + ' ~= ' + str(x))

testFindRoot()
