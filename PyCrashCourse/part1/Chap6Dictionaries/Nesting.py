# Nesting
    # store multiple dictionaries in a list
    # store a list of items as a value in a dictionary
    
# A List of Dictionaries

# A realistic example
# Make an empty list for storing aliens
aliens = []

# Make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points' : 5, 'speed': 'slow'}
    aliens.append(new_alien)

# modify values
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
 
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}\n")

# A List in a Dictionary
# Example: Store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
    
# Example: favourite languages

favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages: 
                print(f"\t{language.title()}")
                
# DO NOT NEST LISTS AND DICTIONARY TOO DEEPLY.

# A Dictionary in a Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")