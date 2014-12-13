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


class debugmeta(type):

    def __new__(cls, clsname, bases, clsdict):
        # class gets created normally
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        # immediately wraped by class decorator
        clsobj = debugmethods(clsobj)
        return clsobj
