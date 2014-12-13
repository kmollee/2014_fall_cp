from functools import wraps, partial


def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(func.__name__)
        print(msg)
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


@debug(prefix='***')
def div(x, y):
    return x / y


if __name__ == '__main__':
    print(div(3, 4))
    print(mul(3, 4))
    print(debug())
