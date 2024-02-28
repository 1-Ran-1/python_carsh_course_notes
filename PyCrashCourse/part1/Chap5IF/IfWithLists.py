            ####### Using if Statements with Lists #########
# ---------------------------------------------------------------------------- #
# Checking for special Items
print('---- Check for special Items & empty list')
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
#requested_toppings = []

# Checking that a list is not empty
# if list_name return True if the list contains at least 1 item.
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f'Adding {requested_topping}.')
    print('\nFinished.')
else:
    print("Are you sure you want a plain pizza?")
# ---------------------------------------------------------------------------- #
# Using Multiple lists
print("---- Multiple tests ----")

available_toppings =  ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished.")
