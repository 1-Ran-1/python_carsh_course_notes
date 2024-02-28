# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# the function loops through the list.

# Modifying a List in a Function

# 3D printed models example
# move items between lists

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, unitl none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# every function should have one specific job
# use functions to keep your code organized and easier to extend.

# Preventing a Function from Modifying a List
# use a copy of a list 

# function_name(list_name[:])
# the [:] makes a copy of the list

# call print_models() like this:
# print_models(unprinted_designs[:], completed_models)
# unprinted_designs will remain the same after the function.

# YOU SHOULD PASS THE ORIGINAL LIST
# UNLESS YOU HAVE A SPECIFIC REASON TO PASS A COPY.
# it's more efficient to work with a existing list.

