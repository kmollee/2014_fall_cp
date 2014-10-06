# datetime is a module for manipulating and display time
import datetime

now = datetime.datetime.utcnow()

# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

time_format = "%a %b %d %I:%M %p"

print("Right now is:")

# use timedelta to add and subtract times
time = now + datetime.timedelta(hours=11)
print(time.strftime(time_format), "Melbourne(UTF + 11)")

time = now + datetime.timedelta(hours=8)
print(time.strftime(time_format), "Taipei(UTF + 8)")

time = now + datetime.timedelta(hours=-4)
print(time.strftime(time_format), "New York(UTF -4)")

def qwe(qew):
    print()

for i in range(1, 50, 5):
    print()