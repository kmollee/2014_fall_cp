def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print('division by zero! ' + str(e))
    except TypeError:
        divide(int(x), int(y))
    else:
        print('result is', result)
    finally:
        print('executing finally clause')
