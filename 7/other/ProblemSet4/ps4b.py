from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    if calculateHandlen(hand) <= 1:
        return None

    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially
    # 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    currentScore = 0
    # For each word in the wordList

    for word in wordList:
        # filter word length is too long
        if len(word) > n:
            continue
        # also check the word is valid?
        elif not isValidWord(word, hand, wordList):
            continue
        # final check word is valid and also equal the n, break loop, return
        elif len(word) == n:
            return word

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or -
        # since you don't really need to test if the word
        # is in the wordList - you can make a similar function
        # that omits that test)

        # Find out how much making that word is worth
        currentScore = getWordScore(word, n)
        # If the score for that word is higher than your best score
        if currentScore > bestScore:
            # Update your best score, and best word accordingly
            bestScore = currentScore
            bestWord = word
    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    #isRanOut = False
    currentScore = 0
    word = None
    newhand = hand.copy()
    #isExhausted = False
    while True:
        displayHand(newhand)
        word = compChooseWord(newhand, wordList, n)
        if word is None:
            #isExhausted = True
            break
        currentScore = getWordScore(word, n)
        print('"' + str(word) + '"', 'earned', currentScore, 'points.', end='')
        totalScore += currentScore
        print(' Total score:', totalScore, 'points')
        hand = updateHand(newhand, word)
        if calculateHandlen(newhand) == 0:
            #isRanOut = True
            break
    # TO DO ... <-- Remove this comment when you code this function
    print('Total score:', totalScore, 'points')
#
# Problem #8: Playing a game
#
#


def getInput(s, ans):
    """
    s:string
    asn:list contain string element

    s will be input prompt
    if user input not in ans list
    keep loop until have an good input
    """
    while True:
        inp = input(s)
        if inp in ans:
            return inp
        print('Invalid command.')


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # track current Hand is....
    # init is None, must have new game to assign it
    currentHand = None
    # while loop, only if input is e will break the loop
    while True:
        # user input
        inp = getInput(
            'Enter n to deal a new hand, r to replay the last hand, or e to end game:', ['n', 'r', 'e'])
        # if input is n
        if inp == 'n':
            currentHand = dealHand(HAND_SIZE)
            UserOrPC = getInput(
                'Enter u to have yourself play, c to have the computer play:', ['u', 'c'])
            # deal new hand, assign to current, convient to track
            if UserOrPC == 'c':
                compPlayHand(currentHand, wordList, HAND_SIZE)
            else:
                playHand(currentHand, wordList, HAND_SIZE)
        # if user input r
        elif inp == 'r':
            # check last time user was played?
            # if was not, refuse, then let user input again
            if currentHand is None:
                print(
                    'You have not played a hand yet. Please play a new hand first!')
            # if was, use currentHand to play, no need generate new hand
            else:
                UserOrPC = getInput(
                    'Enter u to have yourself play, c to have the computer play:', ['u', 'c'])
                # deal new hand, assign to current, convient to track
                if UserOrPC == 'c':
                    compPlayHand(currentHand, wordList, HAND_SIZE)
                else:
                    playHand(currentHand, wordList, HAND_SIZE)
        # only key to out the loop
        elif inp == 'e':
            break
        # other input will be there
        else:
            print('Invalid command.')


# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    '''
    print(
        compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6))
    print(compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5))
    print(
        compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12))
    print(
        compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12))
    compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    compPlayHand(
        {'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    '''
