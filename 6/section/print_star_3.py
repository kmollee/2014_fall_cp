# Pyramid
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


box_square = 15
star_base = 1
# determine upside and downside
upPyramid = round((box_square + 0.5) / 2)
downPyramid = box_square - upPyramid
# print(upPyramid)
# print(downPyramid)
# upside
for row in range(upPyramid):
    star_amount = star_base + 2 * row
    blank_amount = int((box_square - star_amount) / 2)
    print_blank(blank_amount, False)
    print_star(star_amount, True)
