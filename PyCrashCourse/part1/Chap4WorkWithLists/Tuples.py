                            ####### Tuples #########
# ---------------------------------------------------------------------------- #
# Python refers to values that cannot change as immutable
# an immutable list is called a tuple
# Defining a Tuple
# A tuple looks just like a list, except u use parentheses instead of brackets

# Tuples are technically defined by the presence of a COMMA(,)
# The parentheses make them look neater and more readable.
# Include a trailing comma to define a tuple with one element:
# my_t = (3,)
# This can happen when tuples are generated automatically
print('---- Basic Concept of a Tuple ----')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250
# this code will result in a type error
# ---------------------------------------------------------------------------- #
# Looping through All Values in a Tuple
print('---- Looping through a tuple -----')
for dimension in dimensions:
    print(dimension)
# ---------------------------------------------------------------------------- #
# Writing Over a Tuple
print('---- Writing Over a Tuple ----')
# You can assign a new value to a variable that represents a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

