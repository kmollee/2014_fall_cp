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


def debugmethods(cls):
    # cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

# can decorate all methods at once?


@debugmethods
class Spam(object):

    def grok(self):
        pass

    def bar(self):
        pass

    def foo(self):
        pass
if __name__ == '__main__':
    s = Spam()
    s.grok()
