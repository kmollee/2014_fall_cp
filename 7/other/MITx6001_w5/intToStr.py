def intToStr(i):
    if type(i) != int:
        raise TypeError("i should be int")
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = int(i / 10)
    return result

print(intToStr(123))
print(intToStr(123.1))
