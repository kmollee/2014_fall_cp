def counting_vowel(s):
    '''
    s is input string
    function will count how much vowel in the string
    return a int number
    '''
    count = 0
    for word in s:
        if word.lower() in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
    return count


# test ====
assert counting_vowel("apple") == 2
assert counting_vowel("banana") == 3
