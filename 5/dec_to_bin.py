# convert decimal to binary
num = 3
# check num is neg?
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ""

# if num equal 0, result should be 0
if num == 0:
    result = "0"
else:
    while num > 0:
        result = str(int(num % 2)) + result
        num = int(num / 2)
if isNeg:
    result = "-" + result
print(result)
'''
num = 8

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(int(num%2)) + result
    num = int(num/2)
if isNeg:
    result = '-' + result
print(result)
'''
