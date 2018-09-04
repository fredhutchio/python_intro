#!/usr/bin/env python3

#### Intro to Python and Jupyter Notebooks ####

#### Before class ####

# share URL to hack.md
# check installation of python and jupyter notebooks

#### Welcome ####

# instructor introduction
# overview of fredhutch.io
# sign in sheet
# overview course philosophy, how to stay engaged
# course objectives: overview of basic functionality of python (syntax, data manipulation, visualization)

#### Objectives ####

# Today:
# Python and jupyter notebooks
# operators, functions, and data types
# sequences and dictionaries
# defining functions

#### Orientation to Python and projects ####

# ask about previous experience with Python or other programming languages
# overview course philosophy, how to stay engaged
# motivation for Python: programming language, reproducibility, open source
# many ways to interact with Python
#   python in terminal
#   ipython in terminal
#   save script in text editor
#   IDE like spyder
#   notebook: web application that combines code, graphs, and text
#   interactive mode in terminal, chevrons (>>>) is prompt, waiting for input
#   scripting mode: save commands in file (ends in .py), execute entire file at once
# about our tools
#   Anaconda: distribution (way of obtaining) Python;
#       includes extra packages like ipython, spyder
#   conda: package manager that comes with Anaconda, installs/updates packages
#   jupyter notebook: installed with Anaconda

# setting up a project directory
# create new directory called python_project
# keep data, analyses, and text in single folder (directory)
# scripts and text files in folder relate to relative places in the directory
# suggested directories to go with project:
#   data/ which may include separate directories for raw and processed data
#   documents/ for outlines, drafts, and other text
#   scripts/ for scripts related to data cleaning, analysis, plotting

# setting up Notebooks
#   open Terminal (Mac) or Command Prompt (Windows)
#   execute `jupyter notebook`
#   terminal window must stay open, this is kernel (running python)
#   web browser is how you interact with notebook
#   navigate to project directory
#   click "New" in upper right hand, then select "Python3"
#   creates notebook (*.ipynb)
#   click on title to rename
# executing code in a jupyter notebook:
#   enter code in cell and execute by pressing Shift + Return/enter
#   output is printed directly below cell, prefaced by Out[ ]:
#   add new cell with + button
#   commands and output saved in notebook

#### Operators, functions, and data types ####

# operators (mathematical calculations)
4 + 5 # spaces are optional, but easier to read
4+5
6 * 7
2 ** 16 # power
3 > 4 # comparisons, logic
True and True # statements of identity
True or False
True and False

# built-in data types: strings, integers, floats
text= "Data Carpentry"
number = 42
pi_value = 3.1415

# find type of each using function
type(text) # string: characters (letters, numbers, punctuation, emoji)
type(number) # integer
type(pi_value) # float

# see value of something (required to display output in a script)
print(text)
print(11)

#### Sequences ####

# lists: data structure that holds sequence of elements
# can be referened by index (starts at 0)
# surrounded by square brackets
numbers = [1, 2, 3]
numbers[0]

# add number to end of list
numbers.append(4)
print(numbers)

# for loop to access elements in list (or other data structure) one at a time
for num in numbers:
    print(num)

# find help
help(numbers) # on object
numbers.append? # on function

# tuple: list with ordered sequence of elements; cannot be modified
# surrounded by parentheses
a_tuple = (1, 2, 3)
another_tuple = ('blue', 'green', 'red')

## Challenge

#### Dictionaries ####

# dictionary: container holding a pair of objects, key and value
translation = {'one': 1, 'two': 2}
translation['one']

# can't include lists
bad = {[1, 2, 3]: 3}
# Traceback is a multi-line error block printed out

# add items to dictionaries by assigning new value to key
rev = {1: 'one', 2: 'two'}
rev[3] = 'three'
rev

# access each element one at a time with item
for key, value in rev.items():
    print(key, '->', value)

# access each element by key
for key in rev.keys():
    print(key, '->', rev[key])

## Challenge:

#### Functions ####

# define a chunk of code as function
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)

#### Wrapping up ####

# review objectives
# preview next week's objectives
