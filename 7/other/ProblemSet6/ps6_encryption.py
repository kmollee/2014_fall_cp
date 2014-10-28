# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print("  ", len(wordList), "words loaded.")
    return wordList


def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words
    returns: a word from wordList at random
    """
    return random.choice(wordList)


def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])


def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25))
              for i in range(len(s)) if s[i - 1] == ' ']
    return applyShifts(s, shifts)[:-1]


def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    myDict = {}
    uppderList = list(string.ascii_uppercase)
    lowerList = list(string.ascii_lowercase)
    currentList = None
    currentPos = None
    for c in (uppderList + lowerList):
        if c in uppderList:
            currentList = uppderList
        else:
            currentList = lowerList
        currentPos = currentList.index(c)
        shiftPos = (currentPos + shift) % 26
        myDict[c] = currentList[shiftPos]

    return myDict


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """

    encryptDict = coder
    encryptString = ''
    avaiableCharacter = string.ascii_uppercase + string.ascii_lowercase
    for c in text:
        if c in avaiableCharacter:
            encryptString += encryptDict[c]
        else:
            encryptString += c
    return encryptString


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    # HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxRealWord = 0
    bestShift = 0

    for shift in range(0, 26):
        new_text = applyShift(text, shift)
        new_text_list = new_text.split()
        realWordCount = 0
        for word in new_text_list:
            if isWord(wordList, word):
                realWordCount += 1
        if realWordCount > maxRealWord:
            maxRealWord = realWordCount
            bestShift = shift
    return bestShift


def decryptStory(wordList):
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """

    fStory = getStoryString()
    print(fStory)
    shift = findBestShift(wordList, fStory)
    return applyShift(fStory, shift)
    # return "Not yet implemented."

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()

    # print(buildCoder(3))
    # print(buildCoder(9))

    assert 'Khoor, zruog!' == applyCoder("Hello, world!", buildCoder(3))
    assert 'Hello, world!' == applyCoder("Khoor, zruog!", buildCoder(23))
    assert 'Bpqa qa i bmab.' == applyShift('This is a test.', 8)
    assert 'This is a test.' == applyShift('Bpqa qa i bmab.', 18)

    s = applyShift('Hello, world!', 8)
    shift = findBestShift(wordList, s)
    print(shift)
    print(applyShift(s, shift))
    assert 'Hello, world!' == applyShift(s, shift)

    print(decryptStory(wordList))
