# Storing your functions in modules

# which mean store your function in a seperate file
# a < module >
# and then < import > that module into your main program.

# Use import and store functions as modules
# hide details and focus on higher level logic.

# -- Approach 1 --
# import entire module

# open the file pizza.py and copy all function from it.
import pizza

# use module_name . function_name to call the functioon
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -- Approach 2 --
# import specific function

# from module_name import function_name
from pizza import make_pizza

# directly call the function
make_pizza(16, 'pepperoni')

# -- Approach 3 --
# using as to give an alias

# from module_name import function_name as alias
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# -- Approach 4 --
# using as to give module an alias

# import module_name as alias
import pizza as p
p.make_pizza(16, 'pepperoni')

# -- Approach 5 --
# import all functions from a module

# from module_name import *
from pizza import *

