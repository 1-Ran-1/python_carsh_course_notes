# Passing an arbitrary number of arguments

# build pizza example

def make_pizza(*toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# *toppings tells Python to make a tuple called toppings.

# Mixing Positional and Aribitrary Aruguments
# the param that accepts an arbitrary number of args must be placed
# LAST in the function.
# Positional args >= Keyword args > Arbitrary args

# e.g. def make_pizza(size, *toppings):
#          ...
# make_pizza(12, 'mushrooms', 'green pepers', 'extra cheese')

# 12 will be treat as positional args.
# the rest args will be treat as arbitrary args and form a tuple.

# Using Arbitrary Keyword Args
# also refered as **kwargs

def build_profile(first, last, **user_info):
    """
    Buidl a dictionary containing everything we know about a user.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

userprofile = build_profile('albert', 'einstein',
                            location='princeton',
                            fiele='physics')
print(userprofile)

# the double asterisks **
# cause Python to create a dictionary called user_info containing all 
# the extra name-value pairs the function receives.

# Try to use different types of args correctly
# know when to use each type
# use the simplest approach that gets the job done.

