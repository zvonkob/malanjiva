#!/usr/bin/env python
# coding: utf-8

# # Course: Python Essentials for Data Scientists
# 
# https://courses.dataschool.io/view/courses/python-essentials-for-data-scientists
# 
# © 2021 Data School. All rights reserved.

# # Basic Data Types

# assignment statement
x = 4


# change the value of x
x = 5


# inner function runs first, outer function runs second
print(type(x))


# return value prints out automatically
type(x)


# integer
type(5)


# floating point
type(5.0)


# string
type('five')


# string
type("five")


# use double quotes outside in order to use single quotes inside
type("we've been here")


# boolean
type(True)


# boolean
type(False)


# # Lists

# create a list
nums = [5, 5.0, 'five']


# prints out the same way you input it
nums


# check the type
type(nums)


# count the number of elements
len(nums)


# get help on a function
help(len)


# get the first element
nums[0]


# change the first element
nums[0] = 6


# lists are mutable
nums


# check the type of the third element
type(nums[2])


# check the length of the third element
len(nums[2])


# append is a list method
nums.append(7)


# list was modified without an assignment statement
nums


# get help on a list method
help(list.append)


# get help on all list methods
help(list)


# extend is a list method
nums.extend([8, 9])


# list was modified without an assignment statement
nums


# plus sign means additions for numbers
1 + 2


# plus sign means concatenation for lists
nums + [10, 11]


# list was not modified
nums


# object can be on both sides of an assignment statement
nums = nums + [10, 11]


# list was modified through an assignment statement
nums


# # Exercise: Lists
# 
# 1. Create a list of the first names of your family members.
# 2. Print the name of the last person in the list.
# 3. Print the length of the name of the first person in the list.
# 4. Change one of the names from their real name to their nickname.
# 5. Append a new person to the list.
# 6. Change the name of the new person to lowercase using the string method 'lower'.
# 
# After each change, check that it worked.

# # Solution: Lists

# exercise 1
names = ['Wesley', 'Larry', 'Wan']


# exercise 2
names[2]


# exercise 2 using negative indexing
names[-1]


# exercise 3
len(names[0])


# exercise 4
names[0] = 'Wes'
names


# exercise 5
names.append('Annie')
names


# exercise 6 using negative indexing
names[-1] = names[-1].lower()
names


# # Comparisons & Conditional Statements

x = 5


# comparisons return True or False
x > 0


# check for equality
x == 0


# you can use logical operators: and, or, not
x > 0 or x == 0


# check for inequality
x != 0


# you can chain comparisons together
0 < x < 3


# conditional statements respond to conditions
if x > 0:
    print('positive')


# first and third lines will always run, second line will run if condition is True
if x > 0:
    print('positive')
print('done checking')


x = -1


# second line doesn't run since condition is False
if x > 0:
    print('positive')
print('done checking')


x = 5


# vertical whitespace and within-line whitespace don't matter
if x>0:
    print('positive')

print('done checking')


# else statement shouldn't have a condition
if x >= 0:
    print('positive')
    print('or possibly zero')
else:
    print('negative')


# you can include multiple elif statements
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')


# second condition wasn't checked since the first condition was True
if x > 0:
    print('positive')
elif x > 1:
    print('more than 1')
else:
    print('negative')


# # Functions

nums = [3, 5, 4]


# return the list in ascending order
sorted(nums)


# reverse is a parameter, True is an argument
sorted(nums, reverse=True)


# key and reverse parameters have default values
help(sorted)


# define a function with no parameters
def give_me_five():
    return 5


# run the function, which prints out the return value
give_me_five()


# save the return value, thus it doesn't print out
num = give_me_five()


num


# define a function with three parameters
def calc(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    else:
        return None


# run the function without including parameter names
calc(5, 3, 'add')


# run the function with parameter names
calc(a=5, b=3, operation='add')


calc(5, 3, 'subtract')


# returns None
calc(5, 3, 'multiply')


# error since only two arguments were provided
calc(5, 3)


# provide a default value for operation
def calc(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    else:
        return None


calc(5, 3, 'add')


calc(5, 3, 'subtract')


calc(5, 3, 'multiply')


# does not error since operation has a default value
calc(5, 3)


# display the function signature
help(calc)


x = 8
y = 2


# you can pass other variables into a function
calc(x, y)


# a and b only exist within the function
a


# # Exercise: Functions
# 
# Write a function that takes two arguments (hours and hourly_rate) and returns the total pay. If the hourly rate is not specified, it should default to 100.

# # Solution: Functions

# hourly_rate has a default value, but hours does not
def compute_pay(hours, hourly_rate=100):
    return hours * hourly_rate


# positional arguments
compute_pay(30, 50)


# keyword arguments
compute_pay(hours=30, hourly_rate=50)


# uses default hourly_rate of 100
compute_pay(30)


# # Exercise: Functions & Conditional Statements
# 
# Update the function to provide 1.5 times the hourly rate for hours worked above 40 hours. Return the total pay.
# 
# (In other words: The regular hourly rate should be used for the **first 40 hours**, and 1.5 times the hourly rate should be used for **any additional hours**.)

# # Solution: Functions & Conditional Statements

# use parentheses within your code to control order of operations
def compute_pay(hours, hourly_rate=100):
    if hours <= 40:
        return hours * hourly_rate
    else:
        base_pay = hourly_rate * 40
        overtime_pay = (hours - 40) * (hourly_rate * 1.5)
        return base_pay + overtime_pay


# 30 * 100
compute_pay(30)


# 40 * 100
compute_pay(40)


# 40 * 100 + 10 * 150
compute_pay(50)


# 40 * 10 + 10 * 15
compute_pay(50, 10)


# # Naming Objects

# this is allowed, but isn't a good idea
list = 5


type(list)


# delete an object
del list


type(list)


# # Writing Comments

def compute_pay(hours, hourly_rate=100):
    """
    Compute total pay for permanent employees
    
    example: xyz
    """
    if hours <= 40:
        return hours * hourly_rate
    else:
        # overtime pay is 1.5x and starts at 40 hours
        base_pay = hourly_rate * 40
        # print(base_pay)
        overtime_pay = (hours - 40) * (hourly_rate * 1.5)   # don't include temp workers
        # print(overtime_pay)
        return base_pay + overtime_pay
    
    """
    Note: Fix this to exclude temp workers
    Overtime rate will change to 1.6x in 2020
    """
    
    # multi-line
    # comments


# includes the function signature and the docstring
help(compute_pay)


# # List Slicing

weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']


# get the first element
weekdays[0]


# get the last element
weekdays[-1]


# get elements 0 through 2
weekdays[0:3]


# get elements 0 through 2
weekdays[:3]


# get elements 3 through 4
weekdays[3:5]


# get element 3 through the end of the list
weekdays[3:]


# get all elements
weekdays[:3] + weekdays[3:]


# get all elements
weekdays[:2] + weekdays[2:]


# get elements 0 through 2 with a step size of 1
weekdays[0:3:1]


# get elements 0 through 2 with a step size of 2
weekdays[0:3:2]


# get all elements with a step size of 2
weekdays[::2]


# traverse the list backwards
weekdays[::-1]


# save a slice of weekdays
early_week = weekdays[:3]
early_week


# weekdays list was not affected
weekdays


# # Strings

# strings are ordered containers of characters
word = 'hello'


# count the number of characters
len(word)


# get the first character
word[0]


# get characters 1 through 2
word[1:3]


# get the last character
word[-1]


# plus sign means concatenation for strings
word + ' there'


# concatenation requires the same data types
5 + ' is a number'


# convert an integer to a string
str(5)


# concatenate two strings
str(5) + ' is a number'


# convert a string to an integer
int('5')


# error since strings are immutable
word[0] = 'H'


# return a titlecased version of the string
word.title()


# get help on a string method
help(str.title)


# get help on all string methods
help(str)


# error since lists don't have a title method
weekdays.title()


# error since strings don't have an append method
word.append('a')


# # Exercise: Strings & Slicing
# 
# Write a function that accepts a string and returns a modified string:
# 
# - If the original string is at least 4 characters long, return a string made of its first 2 and last 2 characters.
# - Otherwise, return an empty string.
# 
# Example:
# 
# - 'python' returns 'pyon'
# - 'list' returns 'list'
# - 'abc' returns ''

# # Solution: Strings & Slicing

def string_slicer(string):
    if len(string) >= 4:
        return string[:2] + string[-2:]
    else:
        return ''


string_slicer('python')


string_slicer('list')


string_slicer('abc')


# # For Loops

nums = [1, 2, 3, 4, 5]


# iterate through nums, each integer becomes num one time
for num in nums:
    print(num)


# name of the temporary variable doesn't matter
for x in nums:
    print(x)


word = 'hello'


# iterate through word, each character becomes letter one time
for letter in word:
    print(letter)


# inappropriate variable names make your code less readable
for num in word:
    print(num)


# don't access the object you are iterating through within the loop
for letter in word:
    print(word)


# for loop body runs 5 times, last line runs 1 time
for letter in word:
    print(letter)
    print('end of loop')
print('complete')


# # Exercise: For Loops
# 
# Create a list called 'fruits' that contains 'apple', 'banana', and 'cherry'. Then, write a for loop that prints:
# 
# ```
# APPLE
# BANANA
# CHERRY
# ```

# # Solution: For Loops

fruits = ['apple', 'banana', 'cherry']


# fruit is a string, upper is a string method
for fruit in fruits:
    print(fruit.upper())


# comment out code to preserve it without running it
# help(str)


# you can include conditional statements within a for loop
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit.upper())


# # List Comprehensions

nums


for num in nums:
    print(num * 2)


# store the results in a list instead of printing them
doubled = []
for num in nums:
    doubled.append(num * 2)


doubled


# equivalent list comprehension
doubled = [num * 2 for num in nums]


doubled


# resulting list does not need to be assigned a name
[num * 2 for num in nums]


# # Exercise: List Comprehensions
# 
# Create a list called 'fruits' that contains 'apple', 'banana', and 'cherry'.
# 
# 1. Write a list comprehension that returns `['APPLE', 'BANANA', 'CHERRY']`
# 2. Write a list comprehension that returns `['a', 'b', 'c']`

# # Solution: List Comprehensions

fruits = ['apple', 'banana', 'cherry']


# rewrite this for loop for exercise 1
for fruit in fruits:
    print(fruit.upper())


# exercise 1: use the upper method on each fruit
[fruit.upper() for fruit in fruits]


# exercise 2: get the first letter from each fruit
[fruit[0] for fruit in fruits]


# # Dictionaries

# dictionaries contain key-value pairs
family = {'dad':'Homer', 'mom':'Marge', 'size':2}


# keys are separated from values by a colon
family


# count the number of key-value pairs
len(family)


# use a key to look up a value
family['dad']


# you can't use a value to look up a key
family['Homer']


# add a new key-value pair to the dictionary
family['cat'] = 'Snowball'


# dictionaries are ordered as of Python 3.7
family


# you can't look up values by position
family[0]


# keys must be unique, so this overwrites the original value
family['cat'] = 'Snowball II'


family


# delete a key-value pair
del family['cat']


family


# # Lists vs. Dictionaries

# lists | dictionaries
# --- | ---
# contain elements | contain key-value pairs
# accessed by position | accessed by key
# can contain duplicates | keys must be unique
# use brackets | use braces
# designed for flexibility | designed for performance

# # Exercise: Dictionaries
# 
# 1. Create a dictionary of your own family (called 'my_family'), similar to the Simpsons dictionary.
# 2. Check the dictionary length.
# 3. Use a key to look up a value.
# 4. Add a new person to the family.
# 5. Change the value of 'size' to reflect the new person.

# # Solution: Dictionaries

# exercise 1
my_family = {'dad':'Larry', 'mom':'Wan', 'brother':'Wes', 'size':4}


# exercise 2
len(my_family)


# exercise 3
my_family['dad']


# exercise 4
my_family['wife'] = 'Annie'
my_family


# exercise 5
my_family['size'] = 5
my_family


# # Nested Data

family


# add a new key-value pair
family['kids'] = ['bart', 'lisa']


# dictionary value can be any data type, including a list
family


# count the number of key-value pairs
len(family)


# value is a list
family['kids']


# get the first element of the list
family['kids'][0]


type(family['kids'])


type(family['kids'][0])


# # Exercise: Nested Data
# 
# Before starting this exercise, the 'family' dictionary should contain the following:

family


# 1. Get the name of the girl from the kids list.
# 2. Print the length of the kids list.
# 3. Add 'Maggie' to the kids list.
# 4. Fix 'bart' and 'lisa' so that the first letter of each is capitalized (using one or more assignment statements).
# 5. Now change all three kids' names to UPPERCASE using a for loop or list comprehension.

# # Solution: Nested Data

# exercise 1
family['kids'][1]


# exercise 2
len(family['kids'])


# exercise 3
family['kids'].append('Maggie')
family


# exercise 4
family['kids'][0] = 'Bart'
family['kids'][1] = family['kids'][1].title()
family


# exercise 5 using a list comprehension
family['kids'] = [kid.upper() for kid in family['kids']]
family


# exercise 5 using a for loop
kids_uppercase = []
for kid in family['kids']:
    kids_uppercase.append(kid.upper())
family['kids'] = kids_uppercase
family


# # Nested Data & Tuples

family


# return a list-like object containing the keys
family.keys()


# return a list-like object containing the values
family.values()


# convert it to a list
vals = list(family.values())


# list within a list
vals


# get the inner list
vals[-1]


# get the first element of the inner list
vals[-1][0]


# return a list-like object containing the keys and values
family.items()


# convert it to a list
items = list(family.items())


# list of 4 tuples
items


# get the first tuple
items[0]


# get the second tuple
items[1]


# get the first element of the tuple
items[1][0]


# error since tuples are immutable
items[1][0] = 'MOM'


# # Exercise: Nested Data & Tuples (Part 1)
# 
# Here is a data structure:

vals


# Without running the code, figure out what each of these functions would return:
# 
# 1. `len(vals)`
# 2. `len(vals[3])`
# 3. `len(vals[1])`

# # Solution: Nested Data & Tuples (Part 1)

# exercise 1: length of the outer list
len(vals)


# exercise 2: length of the inner list
len(vals[3])


# exercise 3: length of 'Marge'
len(vals[1])


vals[1]


# # Exercise: Nested Data & Tuples (Part 2)
# 
# Here is another data structure:

items


# Without running the code, figure out what each of these functions would return:
# 
# 1. `len(items[0])`
# 2. `len(items[-1][-1][-1])`

# # Solution: Nested Data & Tuples (Part 2)

# exercise 1: length of the first tuple
len(items[0])


items[0]


# exercise 2: length of 'MAGGIE'
len(items[-1][-1][-1])


items[-1]


items[-1][-1]


items[-1][-1][-1]


items[-1][-1][-1][-1]


# # Imports

# error since sqrt function has not been imported
sqrt(49)


# import a module from the Python standard library
import math


# use the sqrt function from the math module
math.sqrt(49)


# append is an available method because nums is a list
nums.append(6)


# define an alias for math
import math as xyz


# use the sqrt function from the math module via an alias
xyz.sqrt(49)


# import a single function from the math module
from math import sqrt


# use the sqrt function without typing the module name
sqrt(49)

