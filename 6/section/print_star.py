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


# draw square
for row in range(1, 10):
    print_star(10, True)


# draw triangle
for row in range(1, 10):
    print_star(row, True)

# origin
for row in range(1, 10):
    for _ in range(row):
        print('*', end='')
    print()
