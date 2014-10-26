# all symbol is row 9 col 7


def symbolSpace(row):
    s = [
        '*******',
        '*******',
        '*******',
        '*******',
        '*******',
        '*******',
        '*******',
        '*******',
        '*******',
    ]
    return s[row]


def symbol1(row):
    s = [
        '***O***',
        '**OO***',
        '***O***',
        '***O***',
        '***O***',
        '***O***',
        '***O***',
        '***O***',
        '*OOOOOO',
    ]
    return s[row]


def symbol2(row):
    """
    row is a positive int
    return None
    """
    s = [
        '*OOOOO*',
        '*O****O',
        '******O',
        '******O',
        '******O',
        '**OOOOO',
        '*O*****',
        '*O*****',
        '*OOOOOO',
    ]
    return s[row]


def symbol3(row):
    s = [
        '*OOOOO*',
        '******O',
        '******O',
        '******O',
        '*OOOOO*',
        '******O',
        '******O',
        '******O',
        '*OOOOO*',
    ]
    return s[row]

'''
# test symbol function is work correctly
symbol1(1)
symbol2(2)
'''

# dict map key:string value:function
# string->function
symbolDict = {"1": symbol1, "2": symbol2, "3": symbol3}

row = 9

while True:
    inp = input("Enter a string to display or 'exit' to end program:")
    if inp == 'exit':
        break
    for r in range(row):
        for c in inp:
            print(symbolDict[c](r), end='')
        print()
print('game over')
