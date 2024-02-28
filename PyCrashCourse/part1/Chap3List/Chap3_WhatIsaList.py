                ####### What Is a List ? #########
# ---------------------------------------------------------------------------- #
# A list is a collection of items in a particular order
    # Make the name of list plural
    # square brackets indicate a list, seperate by commas
bicycles = ['trek', 'cannondale','redline','specialized']
print(bicycles)
# ---------------------------------------------------------------------------- #
# Accessing Elements in a List
    # lists are ordered collections
    # acceess by 'index'
print(bicycles[0])
    # Also use string method
print(bicycles[0].title())
# ---------------------------------------------------------------------------- #
# Index Positions Start at 0, not 1
# Special syntax for accessing the last element
print(bicycles[-1])
# -2 represent the second item from the end of the list, and so forth
print(bicycles[-3])
# ---------------------------------------------------------------------------- #
# Using individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
