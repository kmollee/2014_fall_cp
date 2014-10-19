def counting_bobs(s):
    '''
    input string
    counting bob of string
    return int couting
    '''
    count = 0
    is_end = False
    pos = 0
    while not is_end:
        pos = s.find('bob', pos)
        if pos != -1:
            count = count + 1
            pos = pos + 1
        else:
            is_end = True
    return count

assert counting_bobs('azcbobobegghakl') == 2
assert counting_bobs('bob bob bob') == 3


'''
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs
'''
