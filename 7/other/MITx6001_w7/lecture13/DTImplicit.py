def DTImplicit(toConsider, avail):
    """
    assume toConsider is a list, avail is a positive number(weight)
    return tuple(value, taken)
    """
    #print("toConsider, avail", toConsider, avail)
    # if toConsider is empty list or avail is 0
    if toConsider == [] or avail == 0:
        result = (0, ())
    # if consider now item is larger than avial
    # skip it
    elif toConsider[0][1] > avail:
        result = DTImplicit(toConsider[1:], avail)
    else:
        # get item from toConsider list(first)
        nextItem = toConsider[0]
        #print('nextItem:', nextItem)
        # if take first item and recursive remainder list look
        withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
        withVal += nextItem[0]
        #print(withVal, withToTake)
        withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
        #print(withVal, withToTake)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

if __name__ == '__main__':

    # value and weight
    a = [6, 3]
    b = [7, 2]
    c = [8, 4]
    d = [9, 5]

    stuff = [a, b, c, d]

    val, taken = DTImplicit(stuff, 10)

    print('')
    print('implicit decision search')
    print('value of stuff')
    print(val)
    print('actual stuff')
    print(taken)
