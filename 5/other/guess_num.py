# guess_num

target = '15'
ans = None

while target != ans:
    ans = input("Enter a number:")
    if target == ans:
        break
    print("wrong number, try again")

print("you guess right number! Good job")
