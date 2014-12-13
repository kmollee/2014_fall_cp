from functools import wraps


def debug(prefix=''):

    def decorate(func):
        # func is function to be wrapped

        msg = prefix + func.__qualname__

        @wraps(func)
        def wrapper(*args, **kwargs):
            # print(func.__name__)
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@debug()
def add(x, y):
    """
    return x + y
    """
    return x + y


@debug()
def sub(x, y):
    return x - y


@debug()
def mul(x, y):
    return x * y


@debug(prefix='***')
def div(x, y):
    return x / y


if __name__ == '__main__':
    print(div(3, 4))
    print(mul(3, 4))
