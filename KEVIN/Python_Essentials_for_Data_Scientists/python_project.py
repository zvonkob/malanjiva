#!/usr/bin/env python
# coding: utf-8

# # Project: Python Essentials for Data Scientists
# 
# https://courses.dataschool.io/view/courses/python-essentials-for-data-scientists
# 
# © 2023 Data School. All rights reserved.

# # Project: Part 1

# ## Project Overview
# 
# This project is a series of 7 exercises inspired by Veritasium's excellent 22-minute video, [The Simplest Math Problem No One Can Solve](https://youtu.be/094y1Z2wpJg).
# 
# If you have the time, I recommend watching the entire video right now! (Watching it now won't "spoil" anything about the project.)
# 
# But if you don't have the time, you can simply watch the short section of video related to each exercise before working on it! (I'll link to that section in the instructions for each exercise.)

# ## While Loops

x = 4


# if statement checks a condition, runs once
if x > 0:
    print('positive')


# for loop runs one or more times
for letter in 'hello':
    print(letter)


# while loop checks a condition, runs as long as condition is true
# condition should eventually become false
while x > 0:
    print(x)
    x = x - 1


# **Article:** [Python "while" Loops](https://realpython.com/python-while-loop/) (Real Python)

# ## f-strings

x = 4


if x > 0:
    print('positive')


# you can pass multiple objects to the print function
if x > 0:
    print(x, 'is positive')


# substitute an object into a string using an f-string
if x > 0:
    print(f'{x} is positive')


name = 'Kevin'


# call a method in an f-string
f'My name is {name.upper()}'


# use a function in an f-string
f'My name is {name}, which has {len(name)} letters'


# evaluate an expression in an f-string
f'Divide {x} by 3 to get {x / 3}'


# use a "format specification" to format a number
f'Divide {x} by 3 to get {x / 3:.2f}'


# **Article:** [Python f-string tips & cheat sheets](https://www.pythonmorsels.com/string-formatting/) (Python Morsels)

# ## Mathematical Operators

# addition operator
5 + 3


# subtraction operator
5 - 3


# multiplication operator
5 * 3


# division operator
5 / 3


# "true division" always returns a float
6 / 3


# "floor division" rounds down
5 // 3


6 // 3


# converting to an integer is equivalent to floor division
int(5 / 3)


int(6 / 3)


# round function rounds to the nearest integer
round(5 / 3)


# you can specify the number of decimal places
round(5 / 3, 2)


round(6 / 3, 2)


# modulo operator returns the remainder after division
5 % 3


6 % 3


7 % 3


# ## Project Exercise 1
# 
# This exercise relates to the following portion of the video: [0:00 to 3:31](https://youtu.be/094y1Z2wpJg?t=0).
# 
# Define a function called `path()` that accepts one required argument called `start`. (We are requiring `start` to be a positive integer, but your function doesn't need to validate that it's a positive integer.)
# 
# Within the function, do the following:
# 
# - Create a list called `nums` in which the first element is `start`.
# - Check if `start` is odd or even:
#     - If odd, then multiply by 3 and add 1.
#     - If even, then divide by 2. (Make sure the result is an integer, not a float.)
#     - Append the resulting number to `nums`.
# - Repeat this pattern until you reach the number 1, and then stop.
# - Print out `nums`, which should start with `start` and end with 1.
# - Use the `max()` function to calculate the maximum number reached, and print that out.
# - Print out the number of steps it took to arrive at 1. (Inputting the starting number does not count as a step.)
# 
# For example, if you run `path(10)`, it should print out this:
# 
# ```
# path: [10, 5, 16, 8, 4, 2, 1]
# max: 16
# steps: 6
# ```

# ## Solution to Exercise 1

def path(start):
    
    nums = [start]  # create a list with one number
    num = start     # we will modify num (rather than start)


def path(start):
    
    nums = [start]
    num = start

    while num > 1:          # stop running once num is 1

        if num % 2 == 0:    # check if even
            num = num // 2  # use floor division to return an integer
        else:
            num = num * 3 + 1
    
        nums.append(num)


def path(start):
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    print(f'path: {nums}')
    print(f'max: {max(nums)}')        # you can pass any iterable to max
    print(f'steps: {len(nums) - 1}')  # starting number is not a step


path(10)


# functions without a return statement implicitly return None
path(10) == None


path(7)


path(26)


path(27)


# # Project: Part 2

# ## Separating Functions

# calculates the path and prints info about the path
def path(start):
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    print(f'path: {nums}')
    print(f'max: {max(nums)}')
    print(f'steps: {len(nums) - 1}')


# calculates the path and returns it
def get_path(start):
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    return nums


get_path(10)


# prints info about the path
def print_path_info(start):
    
    nums = get_path(start)
    print(f'path: {nums}')
    print(f'max: {max(nums)}')
    print(f'steps: {len(nums) - 1}')


print_path_info(10)


# get_path and print_path_info don't need to use the same variable names
def print_path_info(s):
    
    n = get_path(s)
    print(f'path: {n}')
    print(f'max: {max(n)}')
    print(f'steps: {len(n) - 1}')


print_path_info(10)


# **Video:** [Variable Scope](https://www.youtube.com/watch?v=QVdf0LgmICw) (Corey Schafer)

# ## Writing Docstrings

# triple-quoted string at the start of a function becomes the docstring
def get_path(start):
    """Given a starting value (positive integer), return the path (list of integers)."""
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    return nums


# multi-line docstring allows for more details
def get_path(start):
    """
    Given a starting value, return the path.
    
    Args:
        start (int): Positive starting value
    Returns:
        List of integers representing the path
    """
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    return nums


# docstring gets printed by help function
help(get_path)


def print_path_info(start):
    """
    Given a starting value, print the path information.
    
    Args:
        start (int): Positive starting value
    Returns:
        None
    """

    nums = get_path(start)
    print(f'path: {nums}')
    print(f'max: {max(nums)}')
    print(f'steps: {len(nums) - 1}')


help(print_path_info)


# **Article:** [Docstring Formats](https://realpython.com/documenting-python-code/#docstring-formats) (Real Python)

# ## Project Exercise 2
# 
# Exercises 2, 3, and 4 all relate to the following portion of the video: [5:10 to 6:57](https://youtu.be/094y1Z2wpJg?t=310).
# 
# Define a function (with a docstring) called `get_first_digits()` that accepts one required argument called `start`, which is a positive integer.
# 
# Within the function, do the following:
# 
# - Calculate the path, using `start` as the starting value.
# - Return a list of integers containing the first digit of each number in that path. (You can use any method you like to extract the first digit, but I recommend using string indexing.)
# 
# For example, `get_first_digits(10)` should return `[1, 5, 1, 8, 4, 2, 1]`.

# ## Solution to Exercise 2

# convert integer to string
str(234)


# extract first digit and convert back to integer
int(str(234)[0])


int(str(2)[0])


def get_first_digits(start):
    """
    Given a starting value, return the first digit of each number in the path.
    
    Args:
        start (int): Positive starting value
    Returns:
        List of integers representing the first digit of each number in the path
    """


def get_first_digits(start):
    """
    Given a starting value, return the first digit of each number in the path.
    
    Args:
        start (int): Positive starting value
    Returns:
        List of integers representing the first digit of each number in the path
    """
    
    nums = get_path(start)
    return [int(str(num)[0]) for num in nums]  # list comprehension


get_path(10)


get_first_digits(10)


get_path(26)


get_first_digits(26)


# # Project: Part 3

# ## Classes

# import sqrt function from the math module
from math import sqrt


# call sqrt function, get back a return value
sqrt(49)


# import Counter class from the collections module
# class names usually start with capital letter
from collections import Counter


# call Counter class, get back a Counter object (an "instance" of Counter)
Counter('hello')


# call str class, get back a str object
str(1011)


s = str(1011)
type(s)


# call int class, get back an int object
int('1011')


# call list class, get back a list object
list('1011')


# count is a function defined for str class, thus strings have a count method
s.count('1')


# str class doesn't contain an append function
s.append('1')


# **Article & Video:** [What is a class?](https://www.pythonmorsels.com/what-is-a-class/) (Python Morsels)

# ## Counter

# pass an iterable to Counter, it counts how many times each element appears
# an iterable is anything you can loop through (string, list, dictionary, etc.)
Counter('hello')


# count how many times each integer appears in the list
Counter([1, 3, 7, 7, 7, 7, 1])


# Counter acts similar to a dictionary since it's a subclass of dict class
c = Counter([1, 3, 7, 7, 7, 7, 1])
type(c)


# pass a key to Counter and it returns a value
c[7]


# use update method to count more things
c.update([6, 6, 7])
c


# list elements from most common to least common
c.most_common()


# sort it by the first element in each tuple
sorted(c.most_common())


# **Python Documentation:** [Counter](https://docs.python.org/3/library/collections.html#collections.Counter)

# ## Range

# call range class, get back a range object
range(4)


# pass it an integer, get back 0 through that number (exclusive of it)
list(range(4))


# first number defines the start (inclusive), second defines the end (exclusive)
list(range(0, 4))


list(range(2, 4))


# use range to run a for loop a set number of times
for num in range(4):
    print(num)


# ## Project Exercise 3
# 
# Exercises 2, 3, and 4 all relate to the following portion of the video: [5:10 to 6:57](https://youtu.be/094y1Z2wpJg?t=310).
# 
# Define a function (with a docstring) called `count_first_digits()` that accepts one required argument called `end`, which is a positive integer.
# 
# Within the function, do the following:
# 
# - For each integer 1 through `end`, calculate the first digit of every number in that path.
# - Tally up all of the first digits across all of those paths.
# - Return a sorted list of tuples, in which the first element of each tuple is the digit and the second element is how many times that digit appeared.
# 
# For example, `count_first_digits(3)` should return `[(1, 5), (2, 2), (3, 1), (4, 1), (5, 1), (8, 1)]`.
# 
# Hint: You can start with an empty Counter.
# 
# Once your function is working, try running `count_first_digits(5000)` and see what you notice.

# ## Solution to Exercise 3

# count_first_digits will build on top of get_first_digits
help(get_first_digits)


# count_first_digits(3) should tally up the three lists below
get_first_digits(1)


get_first_digits(2)


get_first_digits(3)


# create an empty Counter
digits = Counter()
digits


# use the update method to add this list to the Counter
digits.update(get_first_digits(1))
digits


digits.update(get_first_digits(2))
digits


digits.update(get_first_digits(3))
digits


# convert digits Counter into a sorted list of tuples
sorted(digits.most_common())


# range assumes a start of 0
list(range(3))


# count_first_digits(3) would need the values 1, 2, 3
list(range(1, 4))


def count_first_digits(end):
    """
    Given an ending value, return a tally of all first digits of every number
    across every path generated by the starting values 1 through end (inclusive).
    
    Args:
        end (int): Positive ending value
    Returns:
        Sorted list of tuples in which the first element of each tuple is the
        digit and the second element is how many times that digit appeared
    """

    digits = Counter()

    for num in range(1, end + 1):
        digits.update(get_first_digits(num))

    return sorted(digits.most_common())


count_first_digits(3)


# roughly follows Benford's Low
count_first_digits(5000)


# # Project: Part 4

# ## Zip

# zip function loops over two or more iterables and "zips" them together
# returns an iterator of tuples
names = ['Homer', 'Marge', 'Lisa', 'Bart']
roles = ['dad', 'mom', 'daughter', 'son']
zip(names, roles)


# convert into a list of tuples
list(zip(names, roles))


# convert into a dictionary
dict(zip(names, roles))


# convert into a tuple of tuples
tuple(zip(names, roles))


# ## Project Exercise 4
# 
# Exercises 2, 3, and 4 all relate to the following portion of the video: [5:10 to 6:57](https://youtu.be/094y1Z2wpJg?t=310).
# 
# Define a function (with a docstring) called `percentage_first_digits()` that accepts one required argument called `end`, which is a positive integer.
# 
# This function should convert the output of `count_first_digits()` from whole numbers into percentages of the total.
# 
# For example, the output of `count_first_digits(5000)` is this:
# 
# ```
# [(1, 116648),
#  (2, 67801),
#  (3, 45331),
#  (4, 48426),
#  (5, 31109),
#  (6, 20746),
#  (7, 21962),
#  (8, 21867),
#  (9, 19078)]
# ```
# 
# `percentage_first_digits(5000)` should instead return this:
# 
# ```
# [(1, 0.297),
#  (2, 0.173),
#  (3, 0.115),
#  (4, 0.123),
#  (5, 0.079),
#  (6, 0.053),
#  (7, 0.056),
#  (8, 0.056),
#  (9, 0.049)]
# ```
# 
# Here's how I suggest writing the function:
# 
# 1. Save the output from `count_first_digits()`.
# 2. Get all of the numbers (1 through 9) into a list.
# 3. Get all of the counts into another list.
# 4. Calculate the total of those counts.
# 5. Calculate the percentage of that total for each count.
# 6. Zip the numbers with the percentages.

# ## Solution to Exercise 4

# list of tuples
output = count_first_digits(5000)
output


# get the first element of each tuple
nums = [t[0] for t in output]
nums


# get the second element of each tuple
counts = [t[1] for t in output]
counts


# sum the numbers in an iterable
total = sum(counts)
total


percentages = [count / total for count in counts]
percentages


# round the output to 3 decimal places
percentages = [round(count / total, 3) for count in counts]
percentages


list(zip(nums, percentages))


def percentage_first_digits(end):
    """
    Given an ending value, return the percentage of first digits of every number
    across every path generated by the starting values 1 through end (inclusive).
    
    Args:
        end (int): Positive ending value
    Returns:
        Sorted list of tuples in which the first element of each tuple is the
        digit and the second element is the percentage that digit appeared
    """
    
    output = count_first_digits(end)
    nums = [t[0] for t in output]
    counts = [t[1] for t in output]
    total = sum(counts)
    percentages = [round(count / total, 3) for count in counts]
    return list(zip(nums, percentages))


count_first_digits(5000)


percentage_first_digits(5000)


count_first_digits(3)


# still works even though not all digits are present
percentage_first_digits(3)


# # Project: Part 5

# ## Line Plots with Matplotlib

# Matplotlib is not part of the Python standard library
import matplotlib.pyplot as plt


# we want to plot this path
get_path(26)


# draw a line plot: x-axis is index of each list element, y-axis is value
plt.plot(get_path(26))


# Jupyter users: run this if you aren't seeing a plot
# %matplotlib inline


# Non-Jupyter users: run this if you aren't seeing a plot
plt.show()


# path info matches the plot
print_path_info(26)


print_path_info(27)


# plot matches the path info
plt.plot(get_path(27))


# These are the plots we saw in the following portion of the video: [2:32 to 3:11](https://youtu.be/094y1Z2wpJg?t=152).
# 
# **Matplotlib Documentation:** [Installation](https://matplotlib.org/stable/users/getting_started/)

# ## Bar Plots

# we want to plot this data
percentage_first_digits(5000)


# two separate line plots is not what we wanted
plt.plot(percentage_first_digits(5000))


# we need two separate objects for the bar plot: nums and percentages
plt.bar()


# list of tuples
output = percentage_first_digits(5000)
output


# get the first element of each tuple
nums = [t[0] for t in output]
nums


# get the second element of each tuple
percentages = [t[1] for t in output]
percentages


# draw a bar plot: x-axis is nums, y-axis is percentages
plt.bar(nums, percentages)


# This is the plot we saw in the following portion of the video: [5:10 to 6:15](https://youtu.be/094y1Z2wpJg?t=310).

# ## Multiple Assignment

# point on a graph
point = (5, -3)


# use indexing to extract x and y coordinates
x = point[0]
y = point[1]
print(x)
print(y)


# better way is through multiple assignment (also called tuple unpacking)
x, y = point
print(x)
print(y)


# multiple assignment works with other iterables (but is most common with tuples)
x, y = [10, 20]
print(x)
print(y)


# multiple assignment is not limited to two objects
x, y, z = [10, 20, 30]
print(x)
print(y)
print(z)


# number of elements must match the number of objects being assigned
x, y = [10, 20, 30]


# returns a tuple (by virtue of the comma)
def analyze_square(side):
    perimeter = side * 4
    area = side ** 2
    return perimeter, area


analyze_square(10)


# unpack the tuple into separate objects
p, a = analyze_square(10)
print(p)
print(a)


shapes = {'triangle':3, 'square':4, 'pentagon':5}


# looping through a dictionary loops through the keys
# during each loop, a shape name is implicitly assigned to "name"
for name in shapes:
    print(name)


# returns a list-like object containing the keys and values
shapes.items()


# implicit and multiple assignment from each tuple into "name" and "sides"
for name, sides in shapes.items():
    print(f'A {name} has {sides} sides.')


# **Article & Video:** [Tuple unpacking](https://www.pythonmorsels.com/tuple-unpacking/) (Python Morsels)

# ## Unpacking into a Function Call

shapes


# returns a list-like object containing the values
shapes.values()


# convert it into an actual list
sides = list(shapes.values())
sides


# print each of the values separated by a space
print(sides[0], sides[1], sides[2])


# unpack the iterable into a function call using the asterisk operator
# loop over "sides", get one item at a time, pass as separate arguments to print
print(*sides)


# this use of the asterisk operator only works within a function call
*sides


# list of tuples
pairs = list(shapes.items())
pairs


# print each tuple separated by a space
print(*pairs)


# pass the three tuples to zip, get back a list of two tuples
list(zip(*pairs))


# ## Project Exercise 5
# 
# In the Bar Plots lesson, we created a list of tuples called `output`:
# 
# ```
# output = percentage_first_digits(5000)
# output
# [(1, 0.297),
#  (2, 0.173),
#  (3, 0.115),
#  (4, 0.123),
#  (5, 0.079),
#  (6, 0.053),
#  (7, 0.056),
#  (8, 0.056),
#  (9, 0.049)]
# ```
# 
# Then, we used list comprehensions to create the `nums` and `percentages` objects:
# 
# ```
# nums = [t[0] for t in output]
# nums
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# percentages = [t[1] for t in output]
# percentages
# [0.297, 0.173, 0.115, 0.123, 0.079, 0.053, 0.056, 0.056, 0.049]
# ```
# 
# Your task is to create `nums` and `percentages` from `output` in a single line of code by using the asterisk operator and multiple assignment.

# ## Solution to Exercise 5

# goal: aggregate first elements into "nums" and second elements into "percentages"
output = percentage_first_digits(5000)
output


# list of nine tuples has become a list of two tuples
list(zip(*output))


# unpack the list using multiple assignment
nums, percentages = list(zip(*output))
print(nums)
print(percentages)


# bar plot
plt.bar(nums, percentages)


# # Project: Part 6

# ## Dictionary Comprehensions

words = ['data', 'science', 'python']


# create a list of word lengths
length = []
for word in words:
    length.append(len(word))
length


# use a list comprehension instead
[len(word) for word in words]


# create a dictionary of words and their lengths
word_length = {}
for word in words:
    word_length[word] = len(word)
word_length


# use a dictionary comprehension instead
{word:len(word) for word in words}


# ## Project Exercise 6
# 
# This exercise relates to the following portion of the video: [14:00 to 14:34](https://youtu.be/094y1Z2wpJg?t=840).
# 
# Define a function (with a docstring) called `get_max_nums()` that accepts one required argument called `end`, which is a positive integer.
# 
# Within the function, do the following:
# 
# - For each integer 1 through `end`, calculate the path that starts with that integer.
# - Return a dictionary in which each key is the starting number and each value is the maximum number reached during its path. (Use a dictionary comprehension for this.)
# 
# For example `get_max_nums(5)` should return `{1: 1, 2: 2, 3: 16, 4: 4, 5: 16}`.

# ## Solution to Exercise 6

# get_max_nums(5) would need the values 1, 2, 3, 4, 5
end = 5
list(range(1, end + 1))


# path for starting number of 3
get_path(3)


# maximum number reached during the path
max(get_path(3))


# combine into a dictionary comprehension
# key is starting number, value is maximum number reached during the path
{num:max(get_path(num)) for num in range(1, end + 1)}


def get_max_nums(end):
    """
    Given an ending value, return the maximum number reached during every path
    generated by the starting values 1 through end (inclusive).
    
    Args:
        end (int): Positive ending value
    Returns:
        Dictionary in which each key is the starting number and each value is the
        maximum number reached during its path
    """
    
    return {num:max(get_path(num)) for num in range(1, end + 1)}


get_max_nums(5)


max_nums = get_max_nums(10000)


# underscores within numbers are ignored
max_nums = get_max_nums(10_000)


# scatterplot: x-axis is starting numbers, y-axis is maximum numbers reached
plt.scatter(x=max_nums.keys(), y=max_nums.values())


# outlier in the upper right corner of the plot
max(get_path(9663))


# set the y-axis limit to 100,000
plt.scatter(x=max_nums.keys(), y=max_nums.values())
plt.ylim(0, 100_000)


# set "s" to make the points smaller, set "alpha" to add transparency
plt.scatter(x=max_nums.keys(), y=max_nums.values(), s=1, alpha=0.5)
plt.ylim(0, 100_000)


# # Project: Part 7

# ## Membership Operators

x = 2


# comparisons return either True or False
x > 0


x == 0


x != 0


# logical "or" returns True if either comparison is True
x == 0 or x == 1


x == 0 or x == 1 or x == 2


# preferable to use the membership operator "in"
# returns True if x is a member of the list
x in [0, 1]


x in [0, 1, 2]


# in operator works with tuples
x in (0, 1, 2)


# in operator works with strings
'science' in 'data science'


'I' in 'team'


word_length


# in operator checks dictionary keys
'science' in word_length


# in operator doesn't check dictionary values
7 in word_length


# not operator does negation
not True


not False


# "not in" membership operator is the opposite of the "in" operator
'science' not in word_length


'math' not in word_length


# membership operators are useful for conditional statements and while loops
if x in [0, 1]:
    print('x is a binary number')


if x not in [0, 1]:
    print('x is not a binary number')


# ## Project Exercise 7
# 
# This exercise relates to the following portion of the video: [14:34 to 15:09](https://youtu.be/094y1Z2wpJg?t=874).
# 
# Modify the `get_path()` function (and its docstring) so that the `start` argument can be any integer.
# 
# - If `start` is positive, the path should stop once it reaches 1.
# - If `start` is negative, the path should stop once it reaches -1, -5, or -17.
# - If `start` is zero, the path should only contain the integer 0.
# 
# For example:
# 
# `get_path(10)` should return `[10, 5, 16, 8, 4, 2, 1]`
# 
# `get_path(-3)` should return `[-3, -8, -4, -2, -1]`
# 
# `get_path(-9)` should return `[-9, -26, -13, -38, -19, -56, -28, -14, -7, -20, -10, -5]`
# 
# `get_path(-200)` should return `[-200, -100, -50, ..., -68, -34, -17]`
# 
# `get_path(0)` should return `[0]`

# ## Solution to Exercise 7

# start with our existing get_path function
def get_path(start):
    """
    Given a starting value, return the path.
    
    Args:
        start (int): Positive starting value
    Returns:
        List of integers representing the path
    """
    
    nums = [start]
    num = start

    while num > 1:

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    return nums


def get_path(start):
    """
    Given a starting value, return the path.
    
    Args:
        start (int): Positive or negative starting value
    Returns:
        List of integers representing the path
    """
    
    nums = [start]
    num = start

    while num not in [1, -1, -5, -17, 0]:  # list of stopping values

        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    
        nums.append(num)
    
    return nums


# ends in a loop of 4, 2, 1
get_path(10)


# ends in a loop of -2, -1
get_path(-3)


# ends in a loop of -14, -7, -20, -10, -5
get_path(-9)


# ends in a loop of 18 numbers from -50 to -17
get_path(-200)


get_path(0)

