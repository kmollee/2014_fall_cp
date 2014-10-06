# pound sign

# A hands-on to Python for beginning programmers

# Bool

"A" == "a"

"a" != "z"

1 > 0

2 >= 3

-1 < 0

"H" in "Hill"

"z" in "Hello"

"z" not in "Hello"

x == 4

1 != 0

len(0)

# indent must be 4 space
if "banana" in "bannanarama":
    print("I miss the 80s")

sister_age = 15
brother_age = 12

if sister_age > brother_age:
    print("sister is older")
else:
    print("brother is older")

temperature = 70

if temperature > 60 and temperature < 75:
    print("Just right!")
else:
    print("Too extreme")

sister_age = 15
brother_age = 15

if sister_age > brother_age:
    print("sister is older")
elif sister_age == brother_age:
    print("same age")
else:
    print("brother is older")

# variable is dynamic

# pass will do nothing

# visit http://www.codecademy.com/

# list

my_list = ["a", "b", "c"]
len(my_list)

# visit element
my_list[0]
my_list[1]
my_list[2]

# backforward
my_list[-1]

# what if we go outside of range

my_list[3]
# index out of range

# append d element
my_list.append("d")

my_list

len(my_list)

# get element
my_list[3]

# replace

my_list[0] = "z"

my_list

my_list.index("c")


"h" in "hello"

"a" in my_list

"z" in my_list

# slice list
my_list[0:2]

my_list[:3]

my_list[2:]

# copy whole list
my_list[:]

my_string = "Hello world"
my_string[:6]

my_string[3:]

your_list = ["hello", 1, True, 0.5]

names = ["Zelda", "Ellen", "Rick", "Bob"]

len(names)

"Ellen" in names

# sort list
names.sort()

# find max and min list
numbers = [ 3, -5, 0.6, 1700]

max(numbers)
min(numbers)

# real power thing about list
# you can loop through list
numbers = [ 3, -5, 0.6, 1700]

names

for name in names:
    print(name)

for x in names:
    print(x)

for name in names:
    print("hi" + name)


# loop over string

name = "Zelda"

for x in name:
    print(x)

for name in names:
    if name[0] in "AEIOU":
        print("name" + "starts with a vowel")

your_name = "Billy"
your_name[0]

your_name[0] in "AEIOU"

# you always assignment variable

name = ""

name

for name in names:
    if name[0] in "AEIOU":
        print(name + "starts with vowel")
    else:
        print(name + "starts with consonant")

# for loop is so powerful

vowel_names = []

len(vowel_names)

for name in names:
    if name[0] in "AEIOU":
        vowel_names.append(name)

vowel_names

names

# build own len


# init coutner
counter = 0

# a little bit tricky
for name in names:
    counter  = counter + 1

# show counter
counter


sentence = ""

for name in names:
    sentence = sentence + name

sentence

# for loop nest

# list and loops, in codecademy

sentence = "Four score and seven years ago"

sentence_without_vowels = ""

for letter in sentence:
    if letter not in "AEIOUaeiou":
        sentence_without_vowels = sentence_without_vowels + letter

sentence_without_vowels

