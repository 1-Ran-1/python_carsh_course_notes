# A Simple Disctionary
alien_0 = {'color': 'green', 'point': 5}

print(alien_0['color'])
print(alien_0['point'])

# Working with Dictionaries
# A dictionary in Python is a "collection of key-value pairs".
# alien_0 = {'color': 'green'}
# dictionary_name = {key: value}

# Accessing Values in a Dictionary
# print(alien_0['color'])
# dictionary_name[key]
new_points = alien_0['point']
print(f'You just earned {new_points} points!')
# ---------------------------------------------------------------------------- #
# Adding New Key-Value Pairs
print("---- Adding New Key-Values Pairs ----")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# ---------------------------------------------------------------------------- #
# Starting with an Empty Dictonary
print('---- Start from empty dictionary ----')
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
# ---------------------------------------------------------------------------- #
# Moving Values
print('---- Moving Values ----')
alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Example: track the position of an alien
print('---- eg: track position ----')
alien_0 = {'x_position' : 0,
           'y_position' : 25,
           'speed' : 'medium',}

# alien_0['speed'] = 'fast'

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position + increment.
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")

# ---------------------------------------------------------------------------- #
# Removing Key-Value Pairs
print('---- Removing Key-Value Pairs ----')
# use del statement

alien_0 = {'color' : 'green',
           'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# ---------------------------------------------------------------------------- #
# A Dictionary of Similar Objects
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")
    
# Use get() to Access Values
alien_0 = {'color': 'green',
           'speed': 'slow'}
# print(alien_0['points'])
# This results in traceback a 'KeyError'
# get(key, value_if_key_doesnt_exist)

point_value = alien_0.get('points', 'No point value assiged.')

# if key exist -> return value
# if key not exist -> set value

print(point_value)
