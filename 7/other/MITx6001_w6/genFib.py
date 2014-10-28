def genFib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-1)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        fib_next = fibn_1 + fibn_2
        yield fib_next
        fibn_2 = fibn_1
        fibn_1 = fib_next

foo = genFib()


print(next(foo))
print(next(foo))
print(next(foo))
