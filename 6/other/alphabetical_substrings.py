def alphabetical_substrings(s):
    '''
    input string s
    find out longest length alphabetical_substrings in order
    return string  longest length alphabetical_substrings
    '''
    substrings = []
    tmp = ''
    for word in s:
        if tmp == '':
            # only excute at beggin
            tmp = word
        else:
            if tmp[-1] <= word:
                tmp = tmp + word
            else:
                substrings.append(tmp)
                tmp = word
    substrings.sort(key=len, reverse=True)
    return substrings[0]

assert alphabetical_substrings('azcbobobegghakl') == 'beggh'
assert alphabetical_substrings('abcbcd') == 'abc'

'''
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
'''
