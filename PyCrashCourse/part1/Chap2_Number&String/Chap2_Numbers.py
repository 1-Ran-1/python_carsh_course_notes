                        ####### Numbers #########
# ---------------------------------------------------------------------------- #
# Intergers
print("---- Integers ----")
print(2 + 3)
print(2 ** 4)
    # add(+) subtract(-) multiply(*) divide(/) exponent(**)
print(2 + 3 * 4)
    # Python support the order of operations
    # Always use spaces helps you more quickly spot the operations
# ---------------------------------------------------------------------------- #
# Floats
    # Python calls any number with a decimal point a float
print("---- Floats ----")
print(2 * 0.1)
print(0.2 + 0.1)
# ---------------------------------------------------------------------------- #
# Intergers and Floats
print("---- Integers and Floats ----")
    # When you divide any two numbers, you'll always get a float
print(4 / 2)
print(2 * 2.0)
    # Python default to a float in any operation that use a float
    # even if the output is a whole number
# ---------------------------------------------------------------------------- #
# Underscores in Numbers
print("---- Underscores in Numbers ----")
    # Using underscores to make large numbers more readable
universe_age = 14_000_000_000
print(universe_age)
    # Python ingore _ when storing these values
# ---------------------------------------------------------------------------- #
# Multiple Assignment
print("---- Multiple Assignment ----")    
x, y, z = 0, 0, 0
print(x, y, z)
# ---------------------------------------------------------------------------- #
# Constants
print("---- Constants ----")
# Python doesn't have built-in constant types
# All capital letters indicate a variable as a constant and never changed
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
