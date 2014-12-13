from functools import wraps
import os


def debug(func):
    # func is function to be wrapped
    if 'DEBUG' not in os.environ:
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(func.__name__)
        print(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


@debug
def add(x, y):
    """
    return x + y
    """
    return x + y


@debug
def sub(x, y):
    return x - y


@debug
def mul(x, y):
    return x * y


@debug
def div(x, y):
    return x / y


if __name__ == '__main__':
    print(div(3, 4))
