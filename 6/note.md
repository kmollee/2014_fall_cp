# note

this week should focus on function and for loop
might be helpful for student's Midterm exam


# explain how cpu work with main and second memory

# introduce loop's continue and break

# i/o files

example from coursera Programming for everybody

count line in a file

```py
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line Count:", count)
```

---

reading the whole file

```py
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp)
print(inp[:20])
```

---

search through a file

have new line problem

```py
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line)
```

fix

```py
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
```

---

skipping with continue

```py
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #Skip start not with From:
    if not line.startswith("From:"):
        continue
    print(line)
```

---

using `in` to select lines

```py
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #Skip start not with From:
    if not "From:" in line:
        continue
    print(line)
```

---

prompt for filename

```py
fname = input("Enter the file name:")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject line in", fname)

```

handle bad file name

```py
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

```py
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

```py
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

```py
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

```py
count = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)
```

```py
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
my_count = dict()
for line in handle:
    if line.startswith("From:"):
        line = line.rstrip()
        mail_address = line.split()[1]
        my_count[mail_address]=my_count.get(mail_address,0)+1


biggest_num = None
biggest_address = None
for address, times in my_count.items():
    if biggest_num is None or times > biggest_num:
        biggest_num = times
        biggest_address = address

print(biggest_address, biggest_num)
```

# tuple

```py
d = {'a':10, 'b':1, 'c':22}
for k, v in sorted(d.items()):
    print(k, v)
```

```py
d = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in sorted(d.items()):
    #print(k, v)
    tmp.append((v, k))
tmp.sort(reversed=True)
print(tmp)
```

```py
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
my_count = dict()
for line in handle:
    if line.startswith("From:"):
        line = line.rstrip()
        mail_address = line.split()[1]
        my_count[mail_address]=my_count.get(mail_address,0)+1

lst = list()
for key, val in my_count.items():
    lst.append(val, key)

lst.sort(reversed=True)

for val, key in lst[:10]:
    print(key, val)
```

use list comprehension

```py
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k) for k, v in c.items()]))
```

```py
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if line.startswith("From "):
        hr = line.rstrip().split()[-2].split(':')[0]
        count[hr] = count.get(hr, 0) + 1
        #print line
lst = sorted([(key, val) for key, val in count.items()])

for key, val in lst:
    print(key, val)
```

# Regular Expressions

[cheat sheet](http://www.cheatography.com/davechild/cheat-sheets/regular-expressions/)


origin - search line contain "From:" and print out the line

```py
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)
```

use re lib

```py
import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
```

search line start with "From:" and print out the line

```py
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
```

use re lib

```py
import re
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    # re.search will return True or False
    # return True if it find match pattern
    if re.search("^From:", line):
        print(line)
```

use re.findall

```py
>>> import re
>>> x = "My 2 favorite numbers are 19 and 42"
>>> y = re.findall("[0-9]+",x)
>>> y
['2', '19', '42']
>>> y = re.findall('[AEIOU]+', x)
>>> x
'My 2 favorite numbers are 19 and 42'
>>> y
[]
>>> 
```


example 2, why not `"From:"` ? beacuse `+` is greedily, try to match string as larger as he can find

```py
>>> import re
>>> x = 'From: Using the : character'
>>> y = re.findall("^F.+:", x)
>>> y
['From: Using the :']
>>>
```

example 3

```py
>>> import re
>>> x = 'From: Using the : character'
>>> y = re.findall("^F.+?:", x)
>>> y
['From:']
>>> 
```

example 4 pull out a email address from string

```
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```

```py
>>> import re
>>> s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('\S+@\S+', s)
>>> y
['stephen.marquard@uct.ac.za']
>>>
```

```py
>>> import re
>>> s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('^From (\S+@\S+)', s)
>>> y
['stephen.marquard@uct.ac.za']
>>>
```

example 5 get host name

```py
>>> import re
>>> s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('@([^ ]*)', s)
>>> y
['uct.ac.za']
>>> 
```

`@([^ ]*)` match `@(not white space 0 to manay time)`

```py
>>> import re
>>> s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> y = re.findall('^From .*@([^ ]*)', s)
>>> y
['uct.ac.za']
>>> 
```

example find `X-DSPAM-Confidence:` biggest number

```py
import re
fhand = open('mbox-short.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))
```

example Escape Character

```py
>>> import re
>>> x = 'We just received $10.00 for cookies.'
>>> y = re.findall('\$[0-9.]+', x)
>>> y
['$10.00']
>>> 
```


example show how regular expression match the pattern

origin txt

```txt
X-Sieve: CMU Sieve 2.3
```

re

```re
^X.*:
```

more specific

```re
.^X-\S+:
```

- `^`        Matches the beginning of a line
- `$`        Matches the end of the line
- `.`        Matches any character
- `\s`       Matches whitespace
- `\S`       Matches any non-whitespace character
- `*`        Repeats a character zero or more times
- `*?`       Repeats a character zero or more times (non-greedy)
- `+`        Repeats a chracter one or more times
- `+?`       Repeats a character one or more times (non-greedy)
- `[aeiou]`  Matches a single character in the listed set
- `[^XYZ]`   Matches a single character not in the listed set
- `[a-z0-9]` The set of characters can include a range
- `(`        Indicates where string extraction is to start
- `)`        Indicates where string extraction is to end

# def

refer previous week

# combine def with for
