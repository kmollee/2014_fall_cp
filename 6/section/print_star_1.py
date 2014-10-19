def print_star(num, break_line):
    '''
    input: int num > 0
    print out star, the amount depend input num
    return None
    '''
    if num < 0:
        return
    for _ in range(num):
        print('*', end='')
    if break_line:
        print()


def print_blank(num, break_line):
    '''
    input: int num > 0
    print out blank space, the amount depend input num
    return None
    '''
    if num < 0:
        return
    for _ in range(num):
        print(' ', end='')
    if break_line:
        print()


#col = 10
square = 10

print('=======start draw========')
for row in range(0, square + 1):
    print_blank(row, False)
    print_star(square - row, True)
print('=======end draw========')
