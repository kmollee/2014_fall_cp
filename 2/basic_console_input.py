#!/usr/bin/env python3

# input 內建函數以獲取用戶輸入的資訊

# ask name, then print out
name = input("Enter your name:")
print("your name is", name)

# ask a number
# then divide by 2
# print out

# it will be error, string can't use number operator
number = input("Enter a number:")
print("One half of", number, "=", number / 2)  # error!


# string -> int
number = int(input("Enter a number:"))
print("One half of", number, "=", number / 2)


# string -> float number
number = float(input("Enter a number:"))
print("One half of", number, "=", number / 2)

