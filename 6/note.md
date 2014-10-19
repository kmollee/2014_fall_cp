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

# http

[Internet protocol suite](http://en.wikipedia.org/wiki/Internet_protocol_suite)

```
http://www.fakedomain.com/page1.html
```

- `http://` protocol
- `www.fakedomain.com` host
- `page1.html` document

```py
>>> import socket
>>> mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> mysocket.connect(("www.py4inf.com", 80))
```

```py
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/remeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysocket.close()
```

```py
from urllib.request import urlopen
html = urlopen("http://www.google.com/")
print(html)
```

```py
from urllib.request import urlopen

fhand = urlopen("http://www.py4inf.com/code/remeo.txt")
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
```

# def

refer previous week

## why use function

- have to reload file every time want to use it
- can't use smae variable names in other pieces of code

```py
if x > y:
    z = x
else:
    z = y
```

## benefit

- Use by simply calling name and providing input
- Internal detials hidden from users(like black box)
- Syntax
```py
def <function name>(<formal parameters>):
    <function body>
```
- `def` is keyword
- Name is any legal Python name
- Within parenthesis are zero or more formal parameters(each is variable name to be used inside function body)


simple example 
```py
def max(x, y):
    if x > y:
        return x
    else:
        return y
```

invoke

```py
z = max(3, 4)
```

When we call or invoke `max(3, 4)`, x is bound to 3, y is bound to 4, and then body expression(s) are evaluated.

## Function returns

- Body can consist of any number of legal Python expressions
- Expressions are evaluated until
    + Run out of expressions, in which case special value `None` is returned.
    + Or until special keyword `return` is reached, in which case subsequent expression is evaluated and that value is returned as value of function call.


## Summary of function call

- Expressions for each parameter are evaluated, bound to formal parameter names of function
- Control transfers to first expression in body of function
- Body expressions executed until `return` keyword reached(returning value of next expression) or run out of expressions(returning `None`)
- Invocation is bound to the returned value

env variable

```py
x = 5
y = 3

def max(x, y):
    if x > y:
        return x
    else:
        return y

z = max(3, 4)
```

example - compute powers of number

origin

```py
x = float(input("Enter a number:"))
p = int(input("Enter a interger power:"))

result = 1

for turn in range(p):
    print("iteration: " + str(turn) + "current result: " + str(result))
    result = result * x
print("final result:" + str(result))
```

use def

```py
def iterativePower(x, p):
    result = 1

    for turn in range(p):
        print("iteration: " + str(turn) + "current result: " + str(result))
        result = result * x
    return result
x = 3
y = 4
z = iterativePower(3, 5)
# x still is 3, y still is 4
print(z)# 243
```

```tex
f \left ( a, b, c, x  \right ) = a \cdot x^2 + b \cdot x + c
```

```py
def f(a, b, c, x):
    return a*x*x + b*x + c
```


Each function all creates a new environment which scopes bindings of formal parameter and value, and of local variavles(those created with assignments within body)

more example

```py
def square(x):
    return x * x

def twoPower(x, n):
    while n > 1:
        x = square(x)
        n = n / 2
    return x

x = 5
n = 1
print(twoPower(2, 8))
```

nest

```py
>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
>>> 19
```


other/findRoot2.py

```py
def findRoot2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    low = min(0, x)
    high = max(0, x)
    ans = (low + high) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans
print(findRoot2(25.0, 2, 0.01))
print(findRoot2(20.0, 2, 0.01))
print(findRoot2(16.0, 2, 0.01))
print(findRoot2(0.25, 2, 0.01))
```

# combine def with for
