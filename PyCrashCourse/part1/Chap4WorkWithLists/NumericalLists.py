            ####### Making Numerical List #########
# ---------------------------------------------------------------------------- #
# Using the range() Function
print('---- range() Function ----')
for value in range(1, 5):
    # Start from 1, end before 5
    print(value)
# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)
    # Skip numbers
    # Start from 2, end before 11, add 2 repeatedly.
print('---- Skip numbers ----')
even_numbers = list(range(2, 11,2))
print(even_numbers)
    # using range() create square numbers list
print('---- squares ----')
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)
print(squares)
# ---------------------------------------------------------------------------- #
# Simple Statistics with a List of Numbers
print('---- Simple statistics ----')
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# List Comprehensions
# A list comprehension combines the for loop and creation of new elements
# into 1 line of code, and automaticlly appends each new element.
print('---- List Comprehensions ----')
squares = [value ** 2 for value in range(1, 11)]
print(squares)
    # To use this syntax : 
        # begin with a descriptive name for the list
        # open a set of square brackets
        # define th eexpression for the values u want to store in the new list
        # write a for loop to generate values
        # close square brackets