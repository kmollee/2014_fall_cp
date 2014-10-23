# palindrome
# remove all white space
# and don;t care about capitalization, all character should be lowercase
# base case
# a string of length 0 or 1 is a palindrome
# recursive case
# if first character matches last character,
# then is a palindrome if middle section is palindrome

# http://www.palindromelist.net/


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and isPalindrome(s[1:-1])
    return isPal(toChars(s))

assert True == isPalindrome('abba')
assert False == isPalindrome('abbac')  # should fail
assert True == isPalindrome('A but tuba.')
assert True == isPalindrome('A Santa at Nasa.')
assert True == isPalindrome('A Santa dog lived as a devil God at NASA.')
