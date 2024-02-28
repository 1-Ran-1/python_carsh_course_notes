# Passing Arguments

# A function call may need multiple arguments.

# ways to pass arguments
    # positional arguments
        # need to be in the SAME ORDER the parameters were written.
    # keyword arguments
        # each arguments consists of a variable name and a value;
        # and lists and dictionaries of values.

# - Positional Arguments -

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# Multiple Function Calls
describe_pet('dog', 'willie')

# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')
# Always check the order of params to match.

# - Keyword Arguments -
# use name-value pair to pass a argument

describe_pet(animal_type='hamster', pet_name='harry')

# - Default value
# set a default value for a param when define
# def describe_pet(pet_name, animal_type='dog')
# 'dog' is the default value for animal_type

# Note:
# make sure params with default value need to be listed AFTER ALL 
# params that don't have default value.
# This allows Python to interpreting positional arguments correctly.

# Equivalent Function Calls
# if output is correct:
# the way you call the function doesn't matter

# Avoiding Argument Errors.
# - Missing arguments
# - too many arguments
