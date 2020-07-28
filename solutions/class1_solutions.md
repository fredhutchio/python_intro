# Intro to Python
# Class 1 Solutions

## Challenge-numbers

What happens when you execute `numbers[1] = 5`?

The value at index position 1 is replaced with 5.

## Challenge-add

What google search could you use to determine a method for adding multiple values to a list?

Google search: "append multiple items to list python pandas"

One reasonable response is first answer from [this StackOverflow post](https://stackoverflow.com/questions/16621498/how-to-append-multiple-items-in-one-line-in-python):

```python
numbers.extend([5, 6, 7])
print(numbers)
```

## Challenge-remove

How do you remove items from a list?

The following code removes the first instance of 5 as it appears in the list:

```python
numbers.remove(5)
print(numbers)
```

If you wanted to remove all occurences of an element from a list,
there are multiple solutions from [this StackOverflow post](https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list)

```
# create vector with duplicate 5
numbers = [1, 2, 3, 4, 5, 6, 5, 6, 5]
# __ne__ is a special operator meaning "is not equal to"
list(filter((5).__ne__, numbers))
# lambda creates an anonymous function that appends what follows the :
list(filter(lambda a: a != 5, numbers))

# the solutions above do not modify the original list, but this one does:
# slice assignment with list comprehension
numbers[:] = (value for value in numbers if value != 5)
print(numbers)
```

## Challenge-tuple

What happens when you execute `a_tuple[2] = 5`,
and why?

The error reports "tuples are immutable",
meaning once a tuple is created,
it can't be altered.

## Challenge-applesauce

```python
# print only the values of the rev dictionary to the screen
for value in rev.values():
    print(value)
# Reassign the second value (in the key value pair) so that it no longer reads “two” but instead “apple-sauce”
rev[2] = 'applesauce'
# Print the values of rev to the screen again to see if the value has changed
for value in rev.values():
    print(value)
```

## Challenge-function

Define a new function called `subtract_function` that subtracts d from c and test on numbers of your choice.

```python
# define function
def sub_function(c, d):
    result = c - d
    return result
# test function
sub_function(100, 1)
# can reorder numbers if assigned variables
sub_function(d = 1, c = 100)
```
