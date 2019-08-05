#!/usr/bin/env python3

#### Intro to Python and Jupyter Notebooks ####

#### Before class ####

# share URL to hack.md
# check learners have installed Anaconda

#### Welcome ####

# instructor introduction
# overview of fredhutch.io
# sign in using link on HackMD page
# learner introductions and motivation
# overview course philosophy:
#   designed for
# course objectives:
#   intro to python syntax (use of words/symbols to represent things)
#   importing and manipulating data
#   creating publication-quality data visualizations
#   by the end of this course, you should be able to work on processing your own spreadsheet-style data

#### Objectives ####

# Today:
#   Python and jupyter notebooks
#   operators, functions, and data types
#   sequences and dictionaries
#   defining functions

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
#   example notebook (link on hackmd):
#       https://github.com/rasilab/machkovech_2018/blob/master/scripts/NA43_competition.ipynb

# Intro to Jupyter
#   open Anaconda Navigator, then Jupyter notebook
#   on Mac: terminal window must stay open, this is kernel (running python)
#   web browser is how you interact with notebook
#   this is not actually interacting with the internet; note "localhost" in URL
# setting up a project directory
#   navigate to location where you'd like to save files for this class
#   click "New" in upper right hand corner, then "Folder"
#   name new directory/folder "intro_python": this is your project directory
#   a project contains all the work for a manuscript, chapter of a thesis, monthly report, etc
#   keep data, analyses, and text in single folder
#   click on folder; should be empty
#   click "New" in upper right hand, then select "Python3"
#   creates notebook (*.ipynb, or ipython notebook file)
#   autosaves, or can save manually
#   click on title to rename; name this notebook "week1"
# executing code in a jupyter notebook (demo on basic math below)
#   enter code in cell and execute by pressing Shift + Return/enter
#   output is printed directly below cell, prefaced by Out[ ]:
#   add new cell with + button
#   can add Markdown cells with nicely formatted text
#   add title in Markdown cell as # Intro to Python
#   in code cells, comments prefaced with # (not read/executed by python)
#   commands and output saved in notebook
#   talk about other menu options and buttons to remove/add/run cells

#### Operators, functions, and data types ####

# operators (mathematical calculations)
4 + 5
4+5 # spaces are optional, but easier to read
3 > 4 # comparisons, logic

# built-in data types: strings, integers, floats
number = 42
pi_value = 3.1415
text = "Fred Hutch"

# find type of each using function (type)
type(number) # integer
type(pi_value) # float
type(text) # string: characters (letters, numbers, punctuation, emoji)

# convert float to integer
int(pi_value) # decimals removed
type(pi_value) # type hasn't changed!
pi_value = int(pi_value) # convert original object
type(pi_value)

# convert integer to float
float(number) # decimals added

# see value of something (required to display output in a script)
print(text)

# print and type are built in functions; there can also be methods (subset of functions) and user-defined functions

# find help on a function
help(print)

#### Sequences ####

# lists: data structure that holds sequence of elements
# surrounded by square brackets
numbers = [1, 2, 3]

# reference one part of a list
numbers[0] # indexing starts at 0

# find help on an object (can also check under help menu)
?numbers # can also use help(numbers), but may not be useful to you right now

# add number to end of list
numbers.append(4) # append() is an attribute
print(numbers)
# can use tab complete in notebook to see other options
?numbers.append # find help for attribute

# lists can be string data as well
organs = ["lung", "breast", "prostate"]

## Challenge: what google search could you use to determine a method for adding multiple values to a list?
## Challenge: how do you remove items from a list?

# tuple: list with ordered sequence of elements; cannot be modified
# surrounded by parentheses
a_tuple = (1, 2, 3)

## Challenge:
# What happens when you execute:
#numbers[1] = 5
#a_tuple[2] = 5

# Traceback is a multi-line error block printed
# includes information on what error and where in code
# comment out code error if you want to keep it for notes

# sequences can include more than just one data type
mix_tuple = ("lung", 200, "chromosome 1") # can apply to lists, but they're more often one data type

# for loop to access elements in list, tuple, or other data structure one at a time
for num in mix_tuple:
    print(num)

#### Dictionaries ####

# dictionary: container holding a pair of objects, key and value
translation = {"one": 1, "two": 2}
translation["one"]
# example use of dictionary in biology: base pair matching when reverse-complementing DNA

# can include lists as values
list_value = {"yes": [1, 2, 3]}

# cannot include lists as keys
#list_key = {[1, 2, 3]: "nope"}

# add items to dictionaries by assigning new value to key
rev = {1: "one", 2: "two"} # different data types can be key, value
rev[3] = "three"
rev

# two different approaches for printing key/value pairs in a dictionary
# access each element using rev.keys
for key in rev.keys():
    print(key, "->", rev[key])

# access each element using rev.items
for key, value in rev.items():
    print(key, "->", value)

## Challenge:
# print only the values of the rev dictionary to the screen
# Reassign the second value (in the key value pair) so that it no longer reads “two” but instead “apple-sauce”
# Print the values of rev to the screen again to see if the value has changed

#### Functions ####

# define a chunk of code as function
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)

## Challenge: define a new function called subtract_function that subtracts d from c and test on numbers of your choice

#### Wrapping up ####

# make sure work is saved
# review how to get back into notebook
# review objectives
# we won't be writing any more loops or functions in this course, but they are useful for understanding how python works!
# preview next week's objectives
# remind to sign in
