# all symbol is row 9 col 7
# 1. try use function print out symbol 1, 2, 3
# 2. try get input from user, then loop the input and print out
# 3. use dictionary map function


def symbol1():
    s = '''
    ***O***
    **OO***
    ***O***
    ***O***
    ***O***
    ***O***
    ***O***
    ***O***
    *OOOOOO
    '''
    print(s)


def symbol2():
    """
    row is a positive int
    print None
    """
    s = '''
    *OOOOO*
    *O****O
    ******O
    ******O
    ******O
    **OOOOO
    *O*****
    *O*****
    *OOOOOO
    '''
    print(s)


def symbol3():
    s = '''
    *OOOOO*
    ******O
    ******O
    ******O
    *OOOOO*
    ******O
    ******O
    ******O
    *OOOOO*
    '''
    print(s)

# test symbol function is work correctly
'''
symbol1()
symbol2()
symbol3()
'''
symbolDict = {"1": symbol1, "2": symbol2, "3": symbol3}

inp = input("Enter a string:")

for c in inp:
    # print(c)
    symbolDict[c]()
