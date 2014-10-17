# explain how cpu work with main and second memory

# introduce loop's continue and break

# i/o files

example from coursera Programming for everybody

count line in a file

```py3
fhand = open("file.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line Count:", count)
```

---

reading the **while** file

```py3
fhand = open("file.txt")
inp = fhand.read()
print(len(inp))
print(inp)
print(inp[:20])
```

---

search through a file

have new line problem

```py3
fhand = open("file.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line)
```

fix

```py3
fhand = open("file.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
```

---

skipping with continue

```py3
fhand = open("file.txt")
for line in fhand:
    line = line.rstrip()
    #Skip start not with From:
    if not line.startswith("From:"):
        continue
    print(line)
```

---

using `in` to select lines

```py3
fhand = open("file.txt")
for line in fhand:
    line = line.rstrip()
    #Skip start not with From:
    if not "From:" in line:
        continue
    print(line)
```

---

prompt for filename

```py3
fname = input("Enter the file name:")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject line in", fname)

```

handle bad file name

```py3
fname = input("Enter the file name:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject line in", fname)

```

int float string Bool  tuple all is Immutable data type

list, dict is mutable

# continue while example

count average

```py3
toatl = 0
count = 0
while True:
    inp = input("Enter a number(or enter done to exit):")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print("Average:", average)
```

enter password

```py3
password = '15'
ans = None

while password != ans:
    ans = input("Enter a number:")
    if password == ans:
        break
    print("wrong password, try again")

print("login...successful")

```

# dictionary

```py3
purse = dict()

# assgin key and value to dict
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75

print(purse)

# reassgin
purse = ["candy"] + 2

print(purse)
```

# def

refer previous def

# combine def with for
