                    ####### If Statements #########
# ---------------------------------------------------------------------------- #
# Simple if
# if conditional test:
#     do something:

# if-else Statements:
# if conditional test:
#     do something:
# else:
#     do something:

# if-elif-else Chain
# if conditional test_1:
#     do something
# elif conditonal test_2:
#     do something
# elif conditional test_3:
#     ...
# else:
#     do something
# example:
age = 12
if age < 4:
    print("Your admission cost is 0.")
elif age < 18:
    print('Your admission cost is 25.')
else:
    print('Your admission cost is 40.')

# simplify:
# the purpose of the if-elif-else chain is narrower.
# more efficient and easier to modify
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
# use multiple elif blocks
elif age < 65:
    price = 40
else:
    price = 20
# you can omit the else block
# Use a elif test when you have a specific final condtion.
# elif age >= 65:
#     price = 20 

print(f"Your admission cost is {price}.")

# When multiple condtions could be True
# And you want to act on every condtion that is True.
# Use a series of simple if statements

