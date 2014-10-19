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


def drawPyramid(box_square):
    '''
    # box_square must be positive and odd
    print out Pyramid
    return None
    '''
    #box_square = 5
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
    # downside
    for row in range(downPyramid - 1, 0 - 1, -1):
        star_amount = star_base + 2 * row
        blank_amount = int((box_square - star_amount) / 2)
        print_blank(blank_amount, False)
        print_star(star_amount, True)

drawPyramid(5)
drawPyramid(9)
drawPyramid(15)
'''
col = 10
star_base = 1
box_square = 5
for row in range(0, 3):
    start_amount = star_base + 2 * row
    space = int((box_square - start_amount) / 2)
    print_blank(space, False)
    print_star(start_amount, True)
for row in range(1, 0 - 1, -1):
    start_amount = star_base + 2 * row
    space = int((box_square - start_amount) / 2)
    print_blank(space, False)
    print_star(start_amount, True)
print("====end===")
'''
