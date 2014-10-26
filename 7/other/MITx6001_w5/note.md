# Efficiency and Orders of Growth

## Measuring complexity

- Goals in designing programs
    - (1) It returns the correct answer on all legal input
    - (2) It performs the computation efficiently
- Typically (1) is most important, but sometimes (2) is also critical, e.g.,programs for collision detection
- Even when (1) is most important, it valuable to understand and optimize (2)

## Computational complexity

- How much time will it take a program to run?
- How much memory will it need to run?
- Need to balance minimizing computational complexity with conceptual complexity
    + Keep code simple and easy to understand, but where possible optimize performance

## How do we measure complexity

- Given a function, would like to answer: "How ling will this take to run?"
- Could just run on some input and time it.
- Problem is that this depends on:
    + (1) Speed of computer
    + (2) Specifics of Python implementation
    + (3) Value of input
- Avoid (1) and (2) by measuring time in terms of number of basic steps executed.

## Measuring basic steps

- Use a **random access machine(RAM)** as model of computation
    + Steps are executed sequentially
    + Step is an operation that take constant time
        * Assignment
        * Comparison
        * Arithmetic operation
        * Accesssing object in memory
- For point (3), measure time in terms of size of input

## But complexity might depend on value of input?

```py
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False
```

- If `x` happens to be near front of `L`, then returns `True` almost immediately
- If `x` not in `L`, then code will have to examine all elements of `L`
- Need a general way of measuring

## Cases for measuring complexity

- **Best case:** minimum running time over all possible inputs of a given size
    + For linearSearch - constant, i.e. independent of size of inputs
- **Worst case:** maximum running time over all possible input of a given size
    + For linearSearch - linear in size of input
- **Average(or expected) case:** average running time over all possible inputs of a given size
- We will focus on worst case - a kind of **upper bound** on running time

### Example

```py
def fact(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
```

- Number of steps
    + `1`(for assignment)
    + `5*n`(1 for test, plus 2 for first assignment, plus 2 for second assignment in `while`; repeated n times through `while`)
    + `1`(for return)
- `5*n + 2` steps
- But as n gets large, 2 is irrelevant, so basically `5*n` steps
- What about the multiplicative constant (5 in this case)?
- We argue that in general, multiplicative constants are not relevant when comparing algorithms

```py
def sqrtExhaust(x, eps):
    step = eps**2
    ans = 0.0
    while abs(ans**2 - x) >= eps and ans <= max(x, 1):
        ans += step
    return ans
```

- If we call this on 10 and 0.0001, will take one billion iterations of the loop
    + Have roughly 8 steps within each iteration

```py
def sqrtBi(x, eps):
    low = 0.0
    high = max(1, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= eps:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans
```

- If we call this on 10 and 0.0001, will take thirty iterations of the loop
    + Have roughly 10 steps within each iteration
- 1 billion or 8 billion versus 30 or 300 - it is size of problem that matters

## Measuring complexity

- Given this difference in iterations through loop, multiplicative factor (number of whin loop) probably irrelevant
- Thus, we will focus on measuring the complexity as a function of input size
    + Will focus on the largest factor in this expression
    + Will be mostly concerned with the worst case scenario

## Asymptotic notation

- Need a formal way to talk about relationship between running time and size of inputs
- Mostly interested in what heppens as size of inputs gets very large, i.e. approaches infinity

### Example

```py
def f(x):
    for i in range(1000):
        ans = i
    for i in range(x):
        ans += 1
    for i in range(x):
        for j in range(x):
            ans += 1
```

- Complexity is `1000 + 2*x + 2*x^2`
- If x is small, constant term dominates
    + E.g., `x=10` then 1000 of 1220 steps are in first loop
- If x is large, quadratic term dominates
    + E.g. `x=1000000`, then first loop takes 0.000000005% of time, second loop takes 0.0001% of time(out of 2,000,002,001,000 steps)
- So really only need to consider the nested loops(quadratic component)
- Does it matter that this part takes `2*x^2` steps, as opposed to say `x^2` steps?
    + For our example, if our computer executes 100 million steps per second, difference is 5.5 hrours versus 2.25 hours
    + On the other hand if we can find a linear algorithm, this would run in a fraction of second
    + So multiplicative factors probably not crucial, but order of growth is crucial


## Rules of thumb for complexity

- Asymptotic complexity
    + Describe running time in terms of number of basic steps
    + If running time is sum of multiple terms, keep one with the largest growth rate
    + If remaining term is a product, drop any multiplicative constants

(Big O notation)

## Complexity classes

- `O(1)` denotes constant running time
- `O(log n)` denotes logarithmic running time
- `O(n` denotes linear running time
- `O(n log n)` denotes log-linear running time
- `O(n^c)` denotes polynomial running time(`c` is a constant)
- `O(c^n)` denotes exponential running time(`c` is a constant being rasied to a power based on size of input)
- Complexity independent of inputs
- Very few interesting algorithms in this class, but can often have pieces that fit this class
- Can have loops or recursive calls, but number of iterations or calls independent of size of input

## Logarithmic complexity

- Complexity grows as log of size of one of its inputs
- Example:
    + Bisection search
    + Binary search of a list

```py
def intToStr(i):
    if type(i) != int:
        raise TypeError("i should be int")
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = int(i / 10)
    return result
```

- Only have to look at loop as no function calls
- Within while loop constant number of steps(6 steps)
- How manay times through loops?
    + How many time can one divide i by 10?
    + `O(log(i))`

## Linear complexity

- Searching a list in order to see if an element is present
- Add characters of a string, assumed to be composed of decimal digits

```py
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
```

- `O(len(s))`
- Complexity can depend on number of recursive calls

```py
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
```

- Number of recursive calls?
    + `fact(n)` then `fact(n-1)`, etc. until get to `fact(1)`
    + Complexity of each call is constant
    + `O(n)`

## Log-linear complexity

- Many practical algorithms are log-linear
- Very commonly used log-linear algorithm is merge sort
- Will return to this

## Polynomial complexity

- Most common polynomial algorithms are quadratic, i.e., complexity grows with square of size of input
- Commonly occurs when we have nested loops or recursive function calls

```py
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

- Outer loop executed `len(L1)` times
- Each iteration will execute inner loop up to `len(L2)` times
- `O(len(L1)*len(L2))`
- Worst case when `L1` and `L2` same length, none of elements of `L1` in `L2`
- `O(len(L1)^2)`

Find intersection of two lists, return a list with each element appearing only once

```py
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res
```

- First nested loop takes `len(L1)*len(L2)` steps
- Second loop takes at most `len(L1)` steps
- Latter term overwhelmed by former term
- `O(len(L1)*len(L2))`

## Exponential complexity

- Recursive functions where more than one recursive call for each size of problem
    + Towers of Hanoi

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

- Many important problems are inherently exponential
    + Unfortunate, as cost can be high
    + Will lead us to consider approximate solutions more quickly

`/7/other/MITx6001_w5/genSubsets.py`

```py
def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    # get all subsets without last element
    extra = L[-1:]
    # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra)
    # for all smaller solutions, add one with last element
    return smaller + new
    # combine those with last element and those without
```

- Assuming append is constant time
- Time includes time to solve smaller problem, plus time needed to make a copy of all elements in smaller problem
- But important to think about size of smaller
- Know that for a set of size `k` there are `2^k` cases
- So to solve need `2^(n-1) + 2^(n-2)+...+2^0` steps
- Math tells us this is `O(2^n)`

## L9 PROBLEM 4

6.00.1x staff decide to hold an online chess tournament, and n 6.00.1x students respond to participate in it. If the tournament is a single-elimination tournament (this means you are eliminated when you lose once), how many games do we need to decide the winner, in terms of n? Assume there will be no draws or byes.

`O(n)`

You are asked to write an n page research paper. You've written plenty of research papers in your time, and you know it always takes you 30 minutes to write one page of a research paper. In terms of n, what is the complexity order that describes the amount of time this research paper will take to write?

`O(n)`

You are asked to write an n page personal essay. You've written plenty of personal essays in your time, and you know it always takes you two hours to write a personal essay, no matter the length. In terms of n, what is the complexity order that describes the amount of time this personal essay will take to write?

`O(1)`

You just dropped a box of glass toys and n toys in the box broke in half. You'd like to match the halves of the toys so that you could glue them together, but the only way to tell whether two halves belonged to one toy is to physically pick up the two pieces and try to fit them together. Express how long this matching process will take in terms of n.

`O(n^2)`

## L9 PROBLEM 6

```py
# Assume n has been previously bound to some value
i = 0
while i < 5:
   n *= 2
   i += 1

print n
```

`O(1)`

```py
def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result
```

`O(b)`

```py
def recurPower(a, b):
   print a, b
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)
```

`O(b)`

```py
def recurPowerNew(a, b):
   print a, b
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)
```

`O(log(b))`

## L9 PROBLEM 7

```py
def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])
```

`O(len(s))`

```py
def isIn(a, s):
   '''
   a is a character, or, singleton string.
   s is a string, sorted in alphabetical order.
   '''
   if len(s) == 0:
      return False
   elif len(s) == 1:
      return a == s
   else:
      test = s[len(s)/2]
      if test == a:
         return True
      elif a < test:
         return isIn(a, s[:len(s)/2])
      else:
         return isIn(a, s[len(s)/2+1:])
```

`O(log(len(s)))`

```py
def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp
```

`O(n^2)`

```py
def unionNew(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = []
   for e1 in L1:
      flag = False
      for e2 in L2:
         if e1 == e2:
            flag = True
            break
      if not flag:
         temp.append(e1)
   return temp + L2
```

`O(n^2)`

## Compareing complexities

- So does it really mater if our code is of a particular class of complexity?
- Depends on size of problem, but for large scale problems, complexity of worst case makes a difference

## Observations

- A logarithmic algorithm is often almost as good as a constant time algorithm
- Logarithmic costs grow very slowly
- Logarithmic clearly better for large scale problems than linear
- Does not imply linear is bad, however
- While `log(n)` may grow slowly, when multiplied by a linear factor, growth is much more rapid than pure linear
- `O(n log n)` algorithms are still very valuable
- Quadratic is often a problem, however.
- Some problems inherently quadratic but if possible always better to look for more efficient solutions
- Exponential algorithms very expensive
- Exponential generally not of use except for small problems

# Memory and Search

## Algorithms and data structures

- How do you find efficient alogrithms?
    + Hard to invent new ones
    + Easier to reduce problems to know solutions
        * Understand inherent complexity of problem
        * Think about how to break problem into sub-problems
        * Relate sub-problems to other problems for which there already exist efficient algorithms

## Search algorithms

- Search algorithm - method for finding an item or group of items with specific properties thin a collection of items.
- Collection called the search space
- Saw examples - findnig square root as search problem
    + Exhaustive enumeration
    + Bisection search
    + Newton-Raphson

## Linear search and indirection

- Simple search method

```py
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False
```

- Complexity?
    + If element not in list, `O(len(L))` tests
    + So at best linear in length of L
- Why "at best linear"?
    + Assumes each test in loop can be done in constant time
    + But does Python retrieve the `i^th` element of a list in constant time?
## Indirection

- Simple case:list of ints
    + Each element is of same size(e.g., four units of memory - or four eight bit bytes)
    + Then address in memory of `i^th` element is `start + 4 * i` where `start` is address of start of list
    + So can get to that point in memory in constant time
- Bit what if list is of objjects of arbitrary size?
- Use **indirection**
- Represent a list as a combination of a length(numer of objects), and a sequence of fixed size pointers to objects(or memory addresses)
- If length field is 4 units of memory, and each pointer occupies 4 units of memory
- Then **address** of `i^th` element is stored at `start + 4 + 4 * i`
    + `start` - list start address
    + first 4 - length of list
    + second 4 times `i` - go to location
- This address can be found in constant time, and value stored at address also found in constant time
- So search is linear
- **Indirection:** accessing something by first accessing something else that contains a reference to thing sought

## Binary search

- Can we do better than `O(len(L))` for search?
- If know nothing about values of elements in list, then no.
- Worst case, would have to look at every element

## What if list is ordered?

- Suppose elements are sorted in ascending order

```py
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

- Improves average complexity, but worst case still need to look at every element

## Use binary search

1. Pick an index, `i`, that divides list in half
2. Ask if `L[i]==e`
3. If not, ask if `L[i]` larger or smaller than `e`
4. Depending on answer, search left or right half of `L` for `e`

A new version of a divide-and-conquer algorithm

- Break into smaller version of problem(smaller list), plus some simple operations.

```py
def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low]
        mid = low + int((high - low) / 2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
```

## Analyzing binary search

- Does tha recursion halt?
    + Decrementing function
        1. Maps values to which formal parameters are bound to no-negative interger
        2. When value is `<= 0`, recursion terminates
        3. For each recursive call, value of fucntion is strictly less than value on entry to instance of function
    + Here function is high-low(range)
        * At least `0` first time called `(1)``
        * When exactly `0`, no recursive call, return `(2)`
        * Otherwise, halt or recursively call with value halved `(3)`
- So terminates
- What is complexity?
    + How many recursive calls?(work within each call is constant)
    + How many times can we divide `high - low` in half before reaches `0`?
    + `log (high - low) base on 2`
    + thus search complexity is `O(log(len(n)))`

## EASIER TO READ SEARCH PROCEDURE

One of the nice things about coding is that there are many ways of writing a program to do the same thing. Not only that, there are many reasons to write code. The point of presenting code in the text, slides, and lectures to precisely explain a computer science concept. Code is more precise than a lengthy wordy description. In the first few lectures, the goal is to show how to write code in Python. Now, the goal is to discuss algorithms and their complexity. When we want to discuss the running time of an algorithm, it is important to account for all the overheads. This can be difficult when programming languages provide very concise notation for complex operations. For example, in Python, newList = oldList[:] is one simple line, but it makes a copy of the whole list. If the list is long, then the copy can take a long time (O(n) in fact). On the other hand, it is much easier to read than a "for loop" that makes the overhead of the copying obvious.

The lecture on searching is concerned with the running time of various searching algorithm -- how long does it take to find an item in an ordered list. It is important to ensure that there is not any hidden overhead such as list copying. This is why the code in the lectures use indices.

This short memo points out the Python way of describing the search algorithm in a way that is clear to understand, but may have some hidden overhead. When we are not concerned with the complexity or counting the operations, then clarity and readability is more important. It is up to you to know when to use each.

An iterative "Pythonic" search procedure:

```py
def search(list, element):
    for e in list:
        if e == element: 
            return True
    return False
```

The recursive way:

```py
def rSearch(list,element):
    if element == list[0]:
        return True
    if len(list) == 1:
        return False
    return rSearch(list[1:],element)
```

A recursive "Pythonic" binary search procedure:

```py
def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list)/2
    if list[mid] > element:
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        return rBinarySearch( list[mid : ] , element)
    return True
```

## Sorting algorithms

- So what about cost of sorting?
- Assume complexity of sorting alist is `O(osrt(L))`
- Then if we sort and search we want to know if `(sort(L) + log (len(L)) < len(L)`
    + i.e. should we sort and search using binary, just use linear search
- Can't sort in less than linear time!

## Amortizing costs

- But suppose we want to search a list k times?
- Then is `(sort(L) + k*log(len(L)) < k*len(L)`?
    + Depends on k, but one expects that if sort can be done efficiently, then it is better to sort first
    + Amortizing cost of sorting over multiple searches may make this worthwhile
    + How efficiently can we sort?

### Example

```py
def selSort(L):
    for i in range(len(L) - 1):
        minIdex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIdex = j
                minVal = L[j]
            j += 1
        L[i], L[minIdex] = L[minIdex], L[i]
```

## Analyzing slection sort

- Loop invariant
    + Given prefix of list `L[0:i]` and suffix `L[i+1:len(L)-1]`, then prefix is sorted and no elment is prefix is larger than smallest element in suffix
    1. Base case: prefix empty, suffix whole list - invariant true
    2. induction step: move minimum element from suffix to end of prefix. Since invariant true before move, prefix sorted after append
    3. When exit, prefix is entire list, suffix empty, so sorted
- Complexity of inner loop is `O(len(L))`
- Complexity of outer loop alos `O(len(L))`
- So overall complexity is `O(len(L)^2)` or quadratic
- Expensive

## L10 PROBLEM 5

```py
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
```

And here is a suggested alternative:

```py
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
```

1. two function result in the same sorted list.
2. `newSort` may use more - but never fewer - inserts than `selSort`.
3. `newSort` and `selSort` have the same complexity.

## Merge sort

- Use a divide-and-conquer approach:
    1. If list is length 0 or 1, already sorted
    2. If list has more than one element, split into two lists, and sort each
    3. Merge results
        1. To merge, just look at first element of each, move smaller to end of the result
        2. When one list empty, just copy rest of other list

## Complexity of merge sort

- Comparison and copying are constant
- Number of comparisons - `O(len(L))`
- Number of copyings - `O(len(L1)+len(L2))`
- So merging is linear in lenth of the list
- Merge is `O(len(L))`
- Mergesort is `O(len(L))` times number of call merge
    + `O(len(L))` times number of call to mergesort
    + `O(len(L)*log(len(L)))`
- Log linear - `O(n log n)`, where `n` is `len(L)`
- Does come with cost in space, as make new copy of list

```py
import operator


def merge(left, right, compare):
    """
    left:list object
    right:list object
    compare:operator object
    compare left and right list each time once get each one element make compare
    return list
    """
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L, compare=operator.lt):
    """
    L:list object
    compare:operator object
    default compare:less than
    return list(already sort)
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
```

## Imporving efficiency

- Combining binary search with merge sort very efficient
    + If we search list k times, then efficiency is `n*log(n) + k*log(n)`
- Can we do better?
- Dictionaries use concpet of hashing
    + Lookup can be done in time almost independent of size of dictionary

## Hashing

- Convert key to an int
- Use int to index into a list (constant time)
- Conversion done using a **hash function**
    + Map large space of inputs to smaller space of outputs
    + Thus a manay-to-one mapping
    + When tow inputs go to same output - a **collision**
    + A good hash function has a uniform distribution-minimizes probability of a collision

## Complexity

- If no collisions, then `O(1)`
- If everything hashed to same bucket, then `O(n)`
- But in general, can trade off space to make hash table large, and with good function get close to uniform distribution, and reduce complexity to close to `O(1)`

