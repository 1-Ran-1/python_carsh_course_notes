                    ####### If Statement #########
# ---------------------------------------------------------------------------- #
# A Simple Example
print('---- emample ----')
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# ---------------------------------------------------------------------------- #
# Ingoring Case When Checking for Equality
# Note that testing for equality is case sensitive in Python.
# Two values with different capitalization are not considered equal:
print("---- equlity ----")
car = 'Audi'
print(car == 'audi')    
print(car.lower() == 'audi')
# ---------------------------------------------------------------------------- #
# Check for Inequality
# inequality operator !=
print("---- inequlity ----")
requested_topping = 'mushrooms'

if requested_topping != 'archovies':
    print("Hold the anchovies!")
# ---------------------------------------------------------------------------- #
# Numerical Comparisons
print('---- Numerical Comparisons ----')
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# you can include various methematical comparisons in conditional statement
# <, >, <=, >=
# ---------------------------------------------------------------------------- #
# Checking Multiple Conditions
print('---- Multiple Conditions ----')
    # Using 'and' to check multiple conditons:
    # only 11 True, 00/01/10 False
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age >= 21)
    # Using or
    # 10,01,11 True, 00 False
print(age_0 >= 21 or age_1 >= 21)
# ---------------------------------------------------------------------------- #
# Checking Whether a Value Is in a List
print('---- check if element in a list ----')
# Using 'in'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
# Using 'not in'
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
# ---------------------------------------------------------------------------- #
# Boolean Expressions / Conditional Test
# Boolean Values: True, False



