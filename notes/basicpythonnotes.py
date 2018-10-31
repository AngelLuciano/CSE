"""
print("hello world!")

# apparently I'm going to slow,so I will speed up
# this is a comment
# This has no effect on the code
# this is used for a variety of things, such as
# 1. making personal notes about my code
# 2. commenting out the code that does not work

print("Notice what is happening here")
print()   # this creates a new line
print()   # Do you notice the underline here?
# hover over top it to see what is wrong.

# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)
print()

# semi-advanced math
print("figure this out")
print(6 // 4)
print(12 // 3)
print(9 // 4)  # This will ONLY give me a whole number
print()

print("figure this out too")
print(6 % 4)
print(5 % 3)
print(9 % 4)

# Defining variables
car_name = "Wiebe Mobile"   # String
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01  # Float

print("I have a car called %s. It's a pretty nice car" % car_name)
print("It has %d cylinders, but gets %f mpg" % (car_cylinders, car_miles_per_gallon))

# Taking input
name = input("What is your name?")
print("Hello %s" % name)

age = input("How old are you?")
print("%s? You belong in a museum" % age)

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print(hidden_age)
"""

# Multi-line Comments

"""
This is a multi-line comment
anything in between them is automatically commented out.
"""


# Defining Functions
def say_it():
    print("Hello World")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x) :
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# for loops
for i in (1, 2, 3):
    say_it()

for i in range(5): # Range (5) gives the number 0-4
    f(i)

for i in range(5):
    print(i**2)

# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # this is the same as a = a + 1


"""
Hints for loops
For loops - this when you know EXACTLY how many iterations
While loop - this when you DON'T know how many iterations
"""


# control statements (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 9():
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

#  Random numbers
import random  # this should ne on line 1
