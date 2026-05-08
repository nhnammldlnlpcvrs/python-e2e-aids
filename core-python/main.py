# 1. PRINT
print("Hello Python")


# 2. VARIABLES
name = "Nam"
age = 18
height = 1.75
is_student = True

print(name, age, height, is_student)


# 3. DATA TYPES
# int
x = 10

# float
y = 3.14

# string
text = "Python"

# boolean
flag = False

# None
nothing = None


# 4. TYPE CHECKING
print(type(x))
print(type(text))


# 5. INPUT
username = input("Enter username: ")
print(username)


# 6. TYPE CASTING
a = "100"

a_int = int(a)
a_float = float(a)

print(a_int)
print(a_float)


# 7. OPERATORS
a = 10
b = 3

# arithmetic
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# comparison
print(a > b)
print(a == b)

# logical
print(True and False)
print(True or False)
print(not True)


# 8. IF ELSE
score = 8

if score >= 8:
    print("Good")
elif score >= 5:
    print("Average")
else:
    print("Bad")


# 9. FOR LOOP
for i in range(5):
    print(i)


# 10. WHILE LOOP
count = 0

while count < 3:
    print(count)
    count += 1


# 11. BREAK / CONTINUE
for i in range(10):

    if i == 3:
        continue

    if i == 7:
        break

    print(i)


# 12. STRING
text = "Hello Python"

print(text.lower())
print(text.upper())
print(text.replace("Python", "World"))
print(len(text))


# 13. LIST
numbers = [1, 2, 3, 4]

numbers.append(5)
numbers.remove(2)

print(numbers)
print(numbers[0])


# loop through list
for num in numbers:
    print(num)


# 14. TUPLE
point = (10, 20)

print(point[0])


# 15. SET
my_set = {1, 2, 3, 3, 3}

print(my_set)

my_set.add(10)

print(my_set)


# 16. DICTIONARY
student = {
    "name": "Nam",
    "age": 18
}

print(student["name"])

student["school"] = "ABC"

print(student)


# 17. FUNCTIONS
def say_hello():
    print("Hello")


say_hello()


# function with parameters
def add(a, b):
    return a + b


result = add(5, 3)

print(result)


# 18. DEFAULT PARAMETERS
def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Nam")


# 19. LAMBDA
square = lambda x: x * x

print(square(5))


# 20. LIST COMPREHENSION
squares = [x * x for x in range(5)]

print(squares)


# 21. FILE HANDLING
# write file
with open("test.txt", "w") as f:
    f.write("Hello File")


# read file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)


# 22. EXCEPTION HANDLING
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Done")


# 23. CLASSES & OBJECTS
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)


s1 = Student("Nam", 18)

print(s1.name)
s1.introduce()


# 24. INHERITANCE
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def bark(self):
        print("Woof")


dog = Dog()

dog.sound()
dog.bark()


# 25. MODULE IMPORT
import math

print(math.sqrt(25))


# 26. RANDOM
import random

print(random.randint(1, 10))


# 27. DATE TIME
from datetime import datetime

now = datetime.now()

print(now)


# 28. ENUMERATE
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(str(index) + ', ' + fruit)


# 29. ZIP
names = ["Nam", "An"]
scores = [8, 9]

for name, score in zip(names, scores):
    print(name, score)


# 30. MAP / FILTER
nums = [1, 2, 3, 4]

mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))

print(mapped)
print(filtered)


# 31. *ARGS / **KWARGS
def total(*args):
    return sum(args)

print(total(1, 2, 3))


def show_info(**kwargs):
    print(kwargs)

show_info(name="Nam", age=18)


# 32. GLOBAL VARIABLE
counter = 0

def increase():
    global counter
    counter += 1

increase()

print(counter)


# 33. F-STRING
name = "Nam"
age = 18

print(f"My name is {name}, age = {age}")


# 34. MATCH CASE (Python 3.10+)
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case _:
        print("Other")

print("Finished Python Basics")