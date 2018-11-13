#### Intro to Python: week 1 exercises ####

# Introduction to Python and Jupyter Notebooks

# Objectives:
#   Python and jupyter notebooks
#   operators, functions, and data types
#   sequences and dictionaries
#   defining functions

#### In-class exercises ####

## Challenge: what google search could you use to determine a method for adding multiple values to a list?
# search "append multiple items to list python pandas"
# one reasonable response is first answer from here: https://stackoverflow.com/questions/16621498/how-to-append-multiple-items-in-one-line-in-python
numbers.extend([5, 6, 7]) # parentheses will also work instead of square brackets
print(numbers)
## Challenge: how do you remove items from a list?
numbers.remove(5) # removes first instance of 5 as it appears in the list
print(numbers)

## Challenge:
# What happens when you execute:
numbers[1] = 5 # replaces index position 1 with 5
#a_tuple[2] = 5 # error: tuples are immutable

## Challenge:
# print only the values of the rev dictionary to the screen
for value in rev.values():
    print(value)
# Reassign the second value (in the key value pair) so that it no longer reads “two” but instead “apple-sauce”
rev[2] = 'applesauce'
# Print the values of rev to the screen again to see if the value has changed
for value in rev.values():
    print(value)

## Challenge: define a new function called subtract_function that subtracts d from c and test on numbers of your choice
# define function
def sub_function(c, d):
    result = c - d
    return result
# test function
sub_function(100, 1)
# can reorder numbers if assigned variables
sub_function(d = 1, c = 100)

#### Extra exercises ####
