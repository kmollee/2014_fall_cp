# import math module
import math


def f():
    # define function f
    print("This is a user-defined function")
    return 42

# refer https://www.cs.cmu.edu/~112/notes/notes-data-and-exprs.html

# print out object and it's type
print("Some basic types in Python")   # int
print(2, "==>", type(2))
print(2 ** 500, "==>", type(2 ** 500))
print("2.2", "==>", type("2.2"))
print(2 < 2.2, "==>", type(2 < 2.2))
print(math, "==>", type(math))
print(math.tan, "==>", type(math.tan))
print(f, "==>", type(f))
print(type(42), "==>", type(type(42)))

print("######################################")

# further some object type
print("And some other types we will see later in the course...")
print(Exception(), "==>", type(Exception()))  # Exception
print(range(5), "==>", type(range(5)))        # xrange
print([1, 2, 3], "==>", type([1, 2, 3]))      # list
print((1, 2, 3), "==>", type((1, 2, 3)))      # tuple
print({1, 2}, "==>", type({1, 2}))            # set
print({1: 42}, "==>", type({1: 42}))          # dict (dictionary or map)
print(2 + 3j, "==>", type(2 + 3j))
# complex  (complex number) (we may not see this type)
