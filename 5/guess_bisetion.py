secret_num = 25

numGuesses = 0
low = 0
high = 100

print("Please think of a number between 0 and 100!")

inp = ""
ans = int((low + high) / 2)
while inp != "c":
    print("Is your secret number " + str(ans) + " ?")
    inp = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if inp == "h":
        high = ans
        ans = int((low + high) / 2)
    elif inp == "l":
        low = ans
        ans = int((low + high) / 2)
    elif inp == "c":
        pass
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(ans))
