# all symbol is row 9 col 7
# 1. try use function print out symbol 1, 2, 3
# 2. try get input from user, then loop the input and print out
# 3. use dictionary map function
# 4. try use dict map to function, then use function print out first line
# 5. use row range, print out all line of symbol


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
row = 9

symbolDict = {"1": symbol1, "2": symbol2, "3": symbol3}

inp = input("Enter a string:")
for r in range(row):
    for c in inp:
        # print(c)
        print(symbolDict[c](r), end='')
    print()
