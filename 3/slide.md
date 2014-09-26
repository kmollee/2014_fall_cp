# Computer Programming Section

---

# Week3 - variable

---

# resources

- [cp.kmol.info](http://cp.kmol.info)
- [google forum](https://groups.google.com/forum/?hl=zh-TW#!forum/2014fall_cp)
- [github repo](https://github.com/kmollee/2014_fall_cp)
- google
- Me !


---

# Video Time

[![Harvard mark I](http://img.youtube.com/vi/4ObouwCHk8w/0.jpg)](http://www.youtube.com/watch?v=4ObouwCHk8w)

[![Kinect Fitting Room for Topshop](http://img.youtube.com/vi/L_cYKFdP1_0/0.jpg)](http://www.youtube.com/watch?v=L_cYKFdP1_0)


---

# Agenda

- Previous review
    + print
    + input

- Variable
    + type
    + name rule
    + convert

---

# print

    !python
    print("Hello world")
    print("hello this is computer programming section")
    print("have fun!")
    # print out mutiple string
    print("National Formosa University", "Department of Mechanical Design Engineering")
    # change sep to "-"
    print("NFU" ,"National Formosa University", sep="-")
    # change end to "" empty
    print("not insert newline", end="")

---

# input

    !python
    # ask name, then print out
    name = input("Enter your name:")
    print("your name is", name)
    # ask a number
    # then divide by 2
    # print out
    # it will be error, string can't use number operator
    number = input("Enter a number:")
    print("One half of", number, "=", number / 2) # error!
    # string -> int
    number = int(input("Enter a number:"))
    print("One half of", number, "=", number / 2)
    # string -> float number
    number = float(input("Enter a number:"))
    print("One half of", number, "=", number / 2)

---

# variable type

- Numbers
    - int
    - float
- String
- Bool
- List
- Tuple
- Dictionary
- None

---

# Numbers

int - integer ex: 5, 10, 15

floalt - float point ex: 3.14, 1.0

    !python
    a = 123
    b = 123.45

## Math

    !python
    y = 2 * x**x - 3 * x + 10
    z = (x + y) / 3

---

# String

    !python
    user_name = "Dave"
    filename1 = "data/data.csv"

## Text Strings

    !python
    a = "Hello"
    b = "world"
    len(a)
    a + b
    a.upper()
    a.startswith("Hello")
    a.replace("H", "M")

---

# Conversions

To convert value

    !python
    a = int(x)   # convert to int
    b = float(x) # convert to float
    c = str(x)   # convert to string

## example

    !python
    x = '123'
    x + 10 // will cause error
    int(x) + 10

---

# Some Built in Types

**in file 3/builtin_types.py**

---

# Some Built in constants

**in file 3/builtin_constants.py**

---

# Some Built in functions

**in file 3/builtin_functions.py**

---

# Some Builtin Operators

    | Category   | Operators                                          |
    |------------|----------------------------------------------------|
    | Arithmetic | +, -, *, /, //, **, %, - (unary), + (unary)        |
    | Relational | <. <=, >=, >, ==, !=, <>                           |
    | Assignment | +=, -=, *=, /=, //=, **=, %=, <<=, >>=, &=, |=, ^= |
    | Logical    | and, or, not                                       |

---

# example:

    !python
    x + y
    x < y
    y += 1
    a > 10 and a < 20

---

# Any Question?
