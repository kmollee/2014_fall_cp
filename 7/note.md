# Recursion

## iterative algorithms

Resursion

- reduce a problem to a simpler(or smaller) version of the same problem, plus some simple computations
    + Recursive step
- kepp reducing until reach a simple case that can to solve directly
    + Base case
- a * b = a;if b = 1(Base case)
- a * b = a + a * (b-1);otherwise(Recursive case)

```txt
iterMul(3, 5)
3 * 5 = 3 + 3 + 3 + 3 + 3
```

`other/iterMul.py`

```py
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

assert iterMul(3, 5) == 15
assert iterMul(10, 3) == 30
```

`other/recurMul.py`

```py
def recurMul(a, b):
    # base case
    if b == 1:
        return a
    # recursive step
    else:
        return a + recurMul(a, b - 1)

assert recurMul(3, 5) == 15
assert recurMul(10, 3) == 30
```

Some observations

- Each recursive call to a function crates its own environment, with local scoping of variables
- Bindings for variables in each frame are distinct, and bindings are not changed by the recursive call
- Folw of control will pass back to earlier frame once function call returns value


Inductive reasoning

- How do we know that our recursive code will work?
- iterMul terminates beacuse b is initially postive, and decrease by 1 each time around the loop;thus must eventually become less than 1
- recurMul called with `b = 1` has no recursive call and stops
- recurMul called with `b > 1` makes a recursive call with a smaller version of b;must eventually reach call with `b = 1`

Mathematical induction

- To prove a statement indexed on intergers is true for all values of n:
    - Prove it is true when n is smallest value(e.g. n=0 or n=1)
    - Then prove that if it is true for an arbitrary value of n, one can show that it must be true for `n+1`

example

```txt
0+1+2+3+....+n = (n(n+1))/2
```

- If `n=0`, then LHS is 0 and RHS is `0*1/2=0`, so true
- Assume true for some `k`, then need to show that
    + `0+1+2+3+.....+k+(k+1)=((k+1)(k+2))/2`
    - LHS is `k(k+1)/2 + (k+1)` by assumption that property hold for problem of size k
    - This becomes, by algebra, `((k+1)(k+2))/2`

```py
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result
```

factorial

```
n! = n * (n-1) * ... * 1
```

```py
def factI(n):
    '''
    assumes that n is an int > 0, return n!
    '''
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res 
```


```py
def factR(n):
    '''
    assumes that n is an int > 0, return n!
    '''
    if n == 1:
        return n
    return n * factR(n - 1)
```


Write a function recurPower(base, exp) which computes base^exp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem. 

```py
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    return base * recur(base, exp - 1)
```

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
```
    gcd(2, 12) = 2

    gcd(6, 12) = 6

    gcd(9, 12) = 3

    gcd(17, 12) = 1
```

```py
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
```

```py
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    return gcdRecur(b, a % b) 
```

`other/towers_of_hanoi.py`

```py
def printMove(fr, to):
    print('move from ' + str(fr) + '  to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)
print('=======n = 1=======')
Towers(1, 'f', 't', 's')
print('=======n = 2=======')
Towers(2, 'f', 't', 's')
print('=======n = 5=======')
Towers(5, 'f', 't', 's')
```

## fibonacci


Base cases:

- Females(0) = 1
- Females(1) = 1

Recursive case
- Females(n) = Females(n-1) + Females(n-2)

```py
def fib(x):
    '''
    assumes x an int >= 0
    return Fibonacci of x
    '''
    assert type(x) == int and x >= 0
    if x==0 or x ==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
```

`other/isPalindrome.py`

```py
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

assert True == isPalindrome('A but tuba.')
assert True == isPalindrome('A Santa at Nasa.')
assert True == isPalindrome('A Santa dog lived as a devil God at NASA.')
```

# xml

```py
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
# get the text
print("Nmae:", tree.find("name").text)
# get attr
print("Attr:", tree.find("email").get("hide"))
```

```py
import xml.etree.ElementTree as ET

inp = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(inp)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

```


# json

```py
import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])
```


```py
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
```

# tupe

- Concatenation
- Indexing
- Slicing

- Singletons

```py
t1 = (1, 'tow', 3)
t2 = (t1, 'four')

print(t1+t2)
print((t1+t2)[3])
print((t1+t2)[2:5])
t3 = ('five',)
```

Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple'). 


```py
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]
```


# list

- Look a lot like tuples
    + Ordered sequence of values, each identified by an index
    + Use [1,2,3] rather than (1,2,3)
    + Singletons are now just [4] rather than (4,)
- Big Didderence
    + List are mutable
    + While tupe, int float str are immutable
    + So lists can be modified after they are created

```py
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)

def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)
```

```py
# applyToEach

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)
```

# Dictionaries

- `Dict` is generalization of lists, but now indices don't have to be integers(can be values of any immutable type)
- Refer to indices as `keys`, since arbitrary in form
- A `dict` is then a collection of `<key, value>` pairs
- Syntax

```py
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3}
monthNumbers['Jan']# => 1
monthNumbers['Apr'] = 4 # assign to dict
for key in monthNumbers:
    print('key:', key)
    print('value:', monthNumbers[key])
```

```py
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:
```
>>> biggest(animals)
'd'
```

```py
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if not aDict:
        return
    return max((len(v), k) for k,v in aDict.iteritems())[1]
```

```py
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
```

# Black-box testing

- Test suit designed without looking at code
    + Can be done by someone other than implementer
    + Will aovid inherent biases of implementer, expoing potential bugs more easily.
    + Testing designed without knowledge of implementation, thus can be reused even if implementation changed

Paths through a specification

```py
def sqrt(x, eps):
    """
    assumes x eps float
    x >= 0 eps >0
    return res such that x-eps <= res*res <= x+eps
    """
```

x = 0
x > 0

Paths through a specification

- Also good to consider boundary case
    + For lists:empty list, singleton list, many  element list
    + For numbers:very small, very large, "typical"


# Glass-box Testing

- Use code directly to guide desing of test cases
- Glass-gox test suite is path-complete if every potenial path through the code is tested at least once
    - Not always possible if loop can be exercised arbitrary times, or recursion can be arbitrarily deep

```py
def abs(x):
    """
    Assumes x is an int
    return x if x >= 0 and -x otherwise
    """
    if x < - 1:
        return -x
    else:
        return x
```

- test suite of `{-2,2}` will be path complete
- But will miss `abs(-1)` which incorrectly returns -1
    - Testing boundary cases and typical cases would catch this `{-2 -1, 2}`

## Rules of thumb for glass-box testing

- Exercise both branches of all `if` statements
- Ensure each except clause is executed
- For each for loop, have test where:
    - Loop is not enterd
    - Body of loop executed exactly once
    - Body of loop executed more than once
- For each while loop:
    - Same cases as for loops
    - Cases that catch all ways to exit loop
- For recursive functions, test with no recursive calls, one recursive call, and more than one recursive call

# Good testing Pratice

- start with unit test
- move to integration testing
- Afte code is corrected, be sure to do **regression testing**
    + check that program sitll passes all the tests it used to pass, i.e., that your code fix hasn't broken something that used to work

# Runtime bugs

- Overt vs. covert:
    + Overt has an obvious manifestation - code crashed or runs forever
    + Covert has no obious manifestation - code returns value, which may be incorrect but hard to determine
- Persistent vs. intermittent
    + Persistent occurs every time code is run
    + Intermittent only occurs some times, even if run on same input

# Categories of bugs

- Overt and persistent
    - Obvious to detect
    - Good programmers use `defensive programming` to try to ensure that if error is made, bug will fall into category
- Overt and intermittent
    + More frustrating, can be harder to debug, but if conditions that prompt bug can be reprouduce, can be handled
- Covert
    + Highly dangerous, as users may not realize answers are incorrect until code has been run for long period


# Debugging skills

- Treat as search problem:looking for explanation for incorrect behavior
    + Sutdy available data-both correct test cases and incorrect ones
    + Form an hypothesis consistent with the data
    + Design and run a repeatable experiment with potential to refute the hypothesis
    + Keep record of experiments performed:use narrow range of hypotheses

# Debugging as search

- Want to narrow down space of possible sources of error
- Design experiments that expose intermediate stages of computation ( use `print` statements) and use results to further narrow search
- Binary search can be a powerful tool for this

example
```py
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    
    for i in range(n):
        result = []
        elem = input('Enter element:')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

```py
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def silly(n):
    
    for i in range(n):
        result = []
        elem = input('Enter element:')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

```py
def isPal(x):
    assert type(x) == list
    temp = x
    print(temp, x)
    temp.reverse
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        
        elem = input('Enter element:')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

```py
def isPal(x):
    assert type(x) == list
    temp = x
    print(temp, x)
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        
        elem = input('Enter element:')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

```py
def isPal(x):
    assert type(x) == list
    temp = x[:]
    print(temp, x)
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element:')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

# Some paragmatic hint

- Look for the usual suspects
- Ask why the code is doing what it is, not why is not doing what you want
- The bug is probaly not where you think it is - eliminate locations
- Explain the problem to someone else
- Don't believe the documentation
- Take a break and come back to the bug later

# What is an exception

- What happens when procedure execution hits an unexpected condition?
    + Trying to access beyond the limits of a list will raise an `IndexError`
        * `Test=[1,2,3]`
        * `Test[4]`
    + Trying to convert an inappropriate type will raise a `TypeError`
        * `int(Test)`
    + Referencing a non-existing variable will raise a `NameError`
        * `a`
    + Mixing data types without appropriate coercion will raise a `TypeError`
        * `'a'/4`
- These are exceptions - exceptions to what was expected

# What to do with exceptions?

- What to do when procedure execution is stymied by an error condition
    + Fail silently:substitude default values, contitnue
        * Bad idea! User gets no indication results may be suspect
    + Return an `error` value
        * What value to chose? `None`?
        * Callers must include code to check for this special value and deal with consequences -> cascade of error values up the call tree
    + Stop execution, signal error condition
        * in Python: raise an exception

```py
raise Exception("descriptive string")
```

# Deailing with exceptions

```py
try:
    f = open('grades.txt')
except:
    raise Exception("Can't open grades file")
```

Exceptions raised by statements in body of `try` are handled by the `except` statement and execution continues with the body of the `except` statement

#Handling specific exceptions

- Usually the handler is only meant to deal with a particular type of exception. Sometimes we need to clean up before continuing.

```py
try:
    f = open('grades.txt')
except IOError as e:
    print("Can't open grades file" + str(e))
    sys.exit(0)
except ArithmeticError as e:
    raise ValueError("Bug in grades calculation " + str(e))
```

# Types of exceptions

- Already seen common error types:
    + SyntaxError:Python can't parse program
    + NameError:local or global name not found
    + AttributeError:atribute reference fails
    + TypeError:operand doesn't have correct type
    + ValueError:operand type ok, but value is illegal
    + IOError:IO system reports malfunction(e.g. file not found)

# Other extensions to `try`

- `else`:
    + Body of this clause is executed when execution of associated `try` body completes with no exceptions
+ `finally`:
    * Body of this clause is always executed after `try`, `else` and `except` clauses, even if they raised another error or executed a `break`, `continue` or `return`
    * Useful for clean-up code that should be run no matter what else happened(e.g. close file)

## An example

```py
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print('division by zero! ' + str(e))
    except TypeError:
        divide(int(x), int(y))
    else:
        print('result is', result)
    finally:
        print('executing finally clause')
```
