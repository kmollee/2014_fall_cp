def fib(x):
    '''
    assumes x an int >= 0
    return Fibonacci of x
    '''
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

assert fib(2) == 2
assert fib(3) == 3

print(fib(15))
