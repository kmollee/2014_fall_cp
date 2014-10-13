# lecture 3.4, slide 4

x = float(input('Enter a decimal number between 0 and 1: '))
p = 0
while ((2 ** p) * x) % 1 != 0:
    print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

print("final p:", p)

num = int(x * (2 ** p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(int(num % 2)) + result
    num = int(num / 2)

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' +
      str(x) + ' is ' + str(result))

# print is auto round the float number
# so 0.1 is not real 0.1 in machine
