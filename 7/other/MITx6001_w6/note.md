# Leture 11- Classes

## Objests

- python supports manay different kinds of data:
    + `1234`
    + `3.14159`
    + `"hello"`
    + `[1,2,3,4,5]`
    + `{'CA':'California', 'MA':'Massachusetts'}`
- Each of the above is an **object**.
- Objects have:
    + A type(a particular object is said to be an **instance** of a type)(behavior to type)
    + An internal data representation(primitive or composite)
    + A set of procedures for interaction with the object

## Eample:[1,2,3,4]

- Type:list
- Internal data representation
    + int length L, an object array of size `S>=L`, or
    + A linked list of individual cells `<data, pointer to next cell>`
```txt
Internal representation is private - user of the objects should not rely on particular details of the implementation.
Correct behavior may be compromised if you manipulate internal representation directly
```
- Procedures for manipulating lists
    + `I[i]`, `I[i:j]`, `I[j:j:k]`, `+`, `*`
    + `len()`, `min()`, `max()`, `del I[i]`
    + `I.append(..)`, `I.extend(..)`, `I.count(....)`, `I.index(....)`, `I.insert(...)`, `I.pop(...)`, `I.remove(..)`, `I.reverse(..)`, `I.sort(...)`


## Ojbect-oriented programming(OOP)

- Everything is an **object** and has a **type**
- Objects are a data abstraction that encapsulate
    + Internal representation
    + Interface for interacting with object
        * Defines behavior, hides implementation
        * Atributes: data, methods(procedures)
- One can
    + Create new instances of objects(explicitly or using literals)
    + Destory objects
        * Explicitly using `del` or just "forget" about them
        * Python system will reclaim destroyed or inaccessible objects - called "garbage collection"

## Advantages of OOP

- Divide-and-conquer development
    + Implement and test behaviror of each class separately
    + Increased modularity reduce complexity
- Classes make it easy to reuse code
    + Many Python modules define new classes
    + Eash class has a separate environment(no collision on function names)
    + Inheritance allows subclasses to redefine or extend a selected subset of superclass's behavior

# Defining new types

- In Python, the `class` statmenet is used to define a new type

```py
class Coordinate(object):
    define attributes here
```

- As with `def`, indentation used to indicate with statments ar part of the class definition
- Classes can inherit attributes from other classes, in this case, `Coordinate` inherits from the object class. `Coordinate` is said to be a `subclass` of object, object is a `superclass` of `Coordinate`. One can override an inherited attribute with a new definition in the class statement.

## Creating an instance

- Usually when creating an instance of a type, we will wnat to provide some initial values ofr the internal data. Todo this, define an `__init__` method:

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```txt
Method is another name for a procedural attribute, or a procedure that "belogs" to this class
```

- The `.` operator is used to access an attribute of an object. So the `__init__` method above is defining two attributes for the new `Coordinate` object: `x` and `y`

```txt
When accessing an attribute of an instance, start by looking within the class definition, then move up to the definition of a superclass, then move to the global environment.
```

```txt
Data attributes of an instance are often call "instance variables".
```

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
c = Coordinate(3, 4)
"""
note that don't provide argument for self, Python does it automatically
"""
origin = Coordinate(0, 0)
print(c.x, origin.x)
```

`self`: Python will automatically pass into argument, it mean instance frame it self

```txt
The expression
    classname(values..)
creates new object of type
classname and then calls its __init__ method with new object and values.. as the arguments.
When the method is finished executing, Python returns the initialized object as the value.
```

## An environment view of classes

- Class definition creates a binding of class name in global environment to a new frame or environment
- That frame contains any attribute bindings, either varibables or local procedures
- That frame also knows that parent environment from which it can inherit
- Suppose the class is invoked
    + `c=Coordinate(3, 4)`
- A new frame is created(this is the instance)
- The `__init__` method is then called, with self bound to this object, plus any other arguments
- The instance knows about the frame in which `__init__` was called
- Evaluating the body of `__init__` created bindings in the frame of the instance
- Finally the frame created by the class call is returnd, and bound in the global environment
- Given such bindings, calls to attribues are easily found
- `c.x` will return `3` because `c` points to a frame, and within that frame `x` is locally bound
- Note that `c` has access to any binding in the chain of environments

```py
c.__init__(5, 6)
```

- will change the bindings for `x` and `y` within `c`
- Creating a new instace, creates a new environment, e.g. `Origin = Coordinate(0, 0)`
- This shares information within the class environment

## Print representation of an object

- Left to its own devices, Python uses a unique but uninformative print presentation for an object

```py
>>> print(c)
<__main__.Coordinate object at memory_address>
```

- One can define a `__str__` method for a class, which Python will call when it needs a string to print. This method will be called with the object as the first argument and should return a `str`.

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<' + self.x + ',' + self.y + '>'
```

will print out

```py
>>> print(c)
<3,4>
```

## Type of an Object

- We can ask for the type of an object

```py
>>> print(type(c))
<class '__main__.Coordinate'>
```

- This makes sense since

```py
>>> print(Coordinate, type(Coordinate))
<class '__main__.Coordinate'> <class 'type'>
```

- Use `isinstance()` to check if an object is a `Coordinate`

```py
>>> print(isinstance(a, Coordinate))
True
```

## Adding other methods

- Can add our own methods, not just change built-in ones.

```py
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<' + self.x + ',' + self.y + '>'
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
```

## L11 PROBLEM 4

```py
class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute
        # directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
```

## Example: a set of integers

- Create a new type to represent a set(or collection) of integers
    + Initially the set is empty
    + A particular integer appear only once in a set (behavior)
        * This is constraint, called a `representational invariant`, is enforce by the code in the methods
- Internal data representation
    + Use a list to remeber the elements of set
- Interface
    + `insert(e)` - insert integer `e` into set if not there
    + `member(e)` - return `True` if integer `e` is in set, `False` else
    + `remove(e)` - remove integer `e` from set, `error` if not present

```py
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

```

## L11 PROBLEM 6

```txt
For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer science data structure. A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain a specific order. When you want to get something off the end of a queue, you get the item that has been in there the longest (this is known as 'first-in-first-out', or FIFO). You can read up on queues at Wikipedia if you'd like to learn more.

In your Queue class, you will need three methods:

__init__: initialize your Queue (think: how will you store the queue's elements? You'll need to initialize an appropriate object attribute in this method)
insert: inserts one element in your Queue
remove: removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError.
When you're done, you should test your implementation. Your results should look something like this:
```

```py
>>> queue = Queue()
>>> queue.insert(5)
>>> queue.insert(6)
>>> queue.remove()
5
>>> queue.insert(7)
>>> queue.remove()
6
>>> queue.remove()
7
>>> queue.remove()
Traceback (most recent call last):
  File "<stdin>", line 26, in <module>
  File "queue.py", line 15, in remove
    raise ValueError()
ValueError
```

```py
class Queue(object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()
```

# Object Oriented Programming

## Using Inheritance

- Let's build an application that organizes info about people!
    + Person: name, birthday
        * Get last name
        * Sort by last name
        * Get age

## How `plist.sort()` works

- Python uses the timsort algorithm for sorting sequences - a highly-optimized combination of merge and insertion sorts that has very good average case performance
- The only knowledge needed about the objects being sorted is the result of a "less than" comparison between two objects
- Python interpreter translates `obj1 < obj2` into a method call on `obj1 -> obj1.__lt__(obj2)`
- To enable sort operations on instances of a class, implement the `__lt__` special method

```py
import datetime


class Person(object):

    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError('please set birthday first!')
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.nameort()
    for std in classMateList:
        print(std)
```

## Using Inheritance

- Let's build an application that organizes info about people!
    + Person: name, birthday
        * Get last name
        * Sort by last name
        * Get age
    + MITPerson: Person + ID Number
        * Assign ID numbers in sequence
        * Get ID number
        * Sort by ID number

```py
class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign
    # this is class's attribute, not instance

    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        # set up instance attribue idNum to class's attribute
        self.idNum = MITPerson.nextIdNum
        # class's attribute + 1
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        # sorting MIT people uses their ID number, not name
        return self.idNum < other.idNum
```

## Suppose we want to compare things

- Note that MITPerson has its own `__lt__` method
- This method `shadows` the Person method, meaning that if we compare an MITPerson object, since its environment inherits from the MITPerson class environment, Python will see this version of `_lt__` not the Person version
- Thus, `p1 < p2` will be converted into `p1.__lt__(pe)` which applies the method associated with the type of `p1`, or the MITPerson version

## Who inherits

- Why does `p4 < p1` work, but `p1 < p4` doesn't?
    + `p4 < p1` is equivalent to `p4.__lt__(p1)`, which means we use the `__lt__` method associated with the type of `p4`, namely a `Person`(the one that compares based on name)
    + `p1 < p4` is equivalent to `p1.__lt__(p4)`, which means we use the `__lt__` method asscoiated with the type of `p1`, namely an `MITPerson`(the one that compares based on `IDNum`) and since `p4` is a `Person`, it does not have an `IDNum`


## L12 PROBLEM 1

```py
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
```

1. What are the parent class(es)? Note that the term "parent class" is interchangable with the term "superclass". `Spell`
2. What are the child class(es)? Note that the term "child class" is interchangable with the term "subclass". `Accio`, `Confundo`
4. what getDescription method is called when studySpell(Confundo()) is executed? The getDescription method defined within the Confundo class
5. how do we need to modify Accio so that print Accio() will print the following description?

```txt
Summoning Charm Accio
This charm summons an object to the caster, potentially over a significant distance.
```

```py
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return '''This charm summons an object to the caster, potentially over a significant distance.'''
```

## Using Inheritance

- Let's build an application that organizes info about people!
    + Person: name, birthday
        * Get last name
        * Sort by last name
        * Get age
    + MITPerson: Person + ID Number
        * Assign ID numbers in sequence
        * Get ID number
        * Sort by ID number
    + Students: several types, all MITPerson
        * Undegraduate student: has class year
        * Graduate student

`/7/other/MITx6001_w6/UG_Grad.py`

```py
class UG(MITPerson):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(MITPerson):
    pass


def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)

```


## Cleaning up the hierarchy

`/7/other/MITx6001_w6/UG_Grad.py`

```py
class UG(MITPerson):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(MITPerson):
    pass


class TransferStudent(MITPerson):
    pass


def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)
```

Now I have to rethink `isStudent`


## Class Hierarchy & Substitution Principle

- Be careful when overriding methods in a subclass
    + **Substitution principle:** important behaviors of superclass should be supported by all subclasses

## Cleaning up the hierarchy

`/7/other/MITx6001_w6/UG_Grad.py`

```py
class Student(MITPerson):
    pass


class UG(Student):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)
```

- Better is to create a superclass that covers all students
- Ingeneral, creating a class in the hierarchy that captures common behaviors of subclasses allows us to concentrate methods in a single place, and lets us think about subclasses as a coherent whole

## Example class: A Gradebook

- Create class that incldes instances of other classes within it
- Concept:
    + Build a data structure that can hold grades for students
    + Gather together data and procedures for dealing with them in a single structure, so that users can manipulate without having to know internal detail

`/7/other/MITx6001_w6/Gradebook.py`

```py
class Grades(object):

    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  # return copy of list of students
```

## Using a gradebook without knowing internal detail

`/7/other/MITx6001_w6/Gradebook.py`

```py
def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)
```

## Setting up an example

`/7/other/MITx6001_w6/Gradebook.py`

```py
if __name__ == '__main__':
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('John Henry')
    g2 = Grad('George Steinbrenner')

    six00 = Grades()
    six00.addStudent(g1)
    six00.addStudent(ug2)
    six00.addStudent(ug1)
    six00.addStudent(g2)

    for s in six00.allStudents():
        six00.addGrade(s, 75)
    six00.addGrade(g1, 100)
    six00.addGrade(g2, 25)

    six00.addStudent(ug3)

    print(gradeReport(six00))
```

## Using this example

- I could list all students using:(object method)
```py
for s in six00.allStudents():
    print(s)
```
- This print out the list of student names sorted by `idNum`
- Why not just do
```py
for s in six00.students:
    print(s)
```
- This violates the data hiding aspect of an object, and exposes internal representation
    + If I were to change how I want to represent a grade book, I should only need to change the methods within that object, not external procedures that use it([if I were...](http://chrisleung1954.blogspot.tw/2011/01/if-i-were-you.html))

## Comments on the example

- Nicely separates collection of data from use of data
- Access is through methods associated with the gradebook object
- But current version is inefficient - to get a list of all students, I create a copy of the internal list
    + Let's me manipulate without change the internal structure
    + But expensive in a MOOC with 100,000 students


## L12 PROBLEM 3


`/7/other/MITx6001_w6/hand.py`

```py
import random


class Hand(object):

    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = int(self.HAND_SIZE / 3)

        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0, len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(
            len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1

    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Make a copy of the hand, and try to update it
        new_hand = self.hand.copy()
        for letter in word:
            try:
                new_hand[letter] -= 1
            except KeyError:
                # if 'letter' isn't in the hand, we can't make the word from
                # this hand.
                return False
        for letter in new_hand:
            # If any of the letter counts of the new hand are less than zero after the
            # update, then we can't make the word from this hand.
            if new_hand[letter] < 0:
                return False
        # If we've gotten to here, we must be able to make the word from this hand.
        # Set self.hand to the new, updated hand and return True.
        self.hand = new_hand
        return True

myHand = Hand(7)
print(myHand)
print(myHand.calculateLen())

myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

print(myHand.update('az'))
print(myHand)
```

## Generators

- Any procedure or method with a `yield` statement is called a `generator`

```py
def genTest():
    yield 1
    yield 2
```

```py
>>> genTest()
<generator object genTest at 0x7f0b5bb07a20>
>>> foo = genTest()
>>> next(foo)
1
>>> next(foo)
2
>>> next(foo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

- Generators have a `next()` method which starts/resumes execution of the procedure. Inside of generator
    + `yield` suspends execution and returns a value
    + Returning from a generator raises a `StopIteration` exception

- `first next(foo)` - Execution will proceed in body of foo, until reaches first `yield` statement; then returns value associated with that statement
- `second next(foo)` Execution will resume in body at point where stop, until reaches next yield statement; then returns value associated with that statement

## Using generators

- We can use a generator inside looping structure, as it will continue until it get a `StopIteration` exception

```py
>>> for n in genTest():
...     print(n)
... 
1
2
```

## A fancier example:

```py
def genFib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-1)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        fib_next = fibn_1 + fibn_2
        yield fib_next
        fibn_2 = fibn_1
        fibn_1 = fib_next

```

- Evaluating

```py
fib = genFib()
```

- creates a generator object
- Calling

```py
next(fib)
```
- will return the first Fibonacci number, and subsequence calls will generate each number in sequence

- Evaluating

```py
for n in genFib():
    print(n)
```

- will produce all of the Fibonacci numbers (an infinite sequence)

## Fix to Grades class

Before

```py
def allStudents(self):
    """Return a list of the students in the grade book"""
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    return self.students[:]  # return copy of list of students
```

After

```py
def allStudents(self):
    """Return a generator of the students in the grade book"""
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s
```

## L12 PROBLEM 5

`/7/other/MITx6001_w6/genPrime.py`

```py
# refer
# http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/


def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number ** 0.5 + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def genPrimes():
    index = 1
    while True:
        if isPrime(index):
            yield index
        index += 1
```
