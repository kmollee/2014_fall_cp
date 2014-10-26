import operator


def merge(left, right, compare):
    """
    left:list object
    right:list object
    compare:operator object
    compare left and right list each time once get each one element make compare
    return list
    """
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    """
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    """

    return result


def mergeSort(L, compare=operator.lt):
    """
    L:list object
    compare:operator object
    default compare:less than
    return list(already sort)
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

assert [0, 1, 2, 3, 4, 5, 7] == mergeSort([3, 1, 2, 5, 7, 0, 4])
assert [1] == mergeSort([1])
