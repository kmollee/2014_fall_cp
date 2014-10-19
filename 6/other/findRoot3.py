def findRoot3(x, power, epsilon):
    '''
    x and epsilon int or float, power an int
        epsilon > 0 and power > 1
    '''
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans
print(findRoot3(25.0, 2, 0.01))
print(findRoot3(20.0, 2, 0.01))
print(findRoot3(16.0, 2, 0.01))
print(findRoot3(0.125, 2, 0.01))
print(findRoot3(0.5, 2, 0.01))
# when fall witg a fractional argument like 0.25
# search 0 ~ 0.125
# which mean our first guess will be the average, or .125

# seach wrong field

print(findRoot3(25.0, 2, .001))
print(findRoot3(27.0, 3, .001))
print(findRoot3(-27.0, 3, .001))

print(findRoot3(0.25, 2, .001))
print(findRoot3(-0.125, 3, .001))


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ' + str(x) +
                  ' and power = ' + str(power))
            res = findRoot3(x, power, epsilon)
            if res == None:
                print('    No root')
            else:
                print('    ' + str(res ** power) + ' ~= ' + str(x))

testFindRoot()
