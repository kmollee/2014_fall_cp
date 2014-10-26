def selSort(L):
    for i in range(len(L) - 1):
        minIdex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIdex = j
                minVal = L[j]
            j += 1
        L[i], L[minIdex] = L[minIdex], L[i]
        '''
        tmp = L[i]
        L[i] = L[minIdex]
        L[minIdex] = tmp
        '''

if __name__ == '__main__':
    L = [3, 1, 4, 5, 2]
    selSort(L)
    print(L)
    assert L == [1, 2, 3, 4, 5]
